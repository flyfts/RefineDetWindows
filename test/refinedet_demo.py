'''
In this example, we will load a RefineDet model and use it to detect objects.
'''

import argparse
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import glob

# Make sure that caffe is on the python path:
caffe_root = 'C:/RefineDetWindows/'
os.chdir(caffe_root)
sys.path.insert(0, os.path.join(caffe_root, 'python'))
import caffe
import time
import datetime
from google.protobuf import text_format
from caffe.proto import caffe_pb2

def get_labelname(labelmap, labels):
    num_labels = len(labelmap.item)
    labelnames = []
    if type(labels) is not list:
        labels = [labels]
    for label in labels:
        found = False
        for i in xrange(0, num_labels):
            if label == labelmap.item[i].label:
                found = True
                labelnames.append(labelmap.item[i].display_name)
                break
        assert found == True
    return labelnames

def ShowResults(img, image_file, results, labelmap, threshold=0.6, save_fig=False):
    plt.clf()
    plt.imshow(img)
    plt.axis('off')
    ax = plt.gca()

    num_classes = len(labelmap.item) - 1
    colors = plt.cm.hsv(np.linspace(0, 1, num_classes)).tolist()

    for i in range(0, results.shape[0]):
        score = results[i, -2]
        if threshold and score < threshold:
            continue

        label = int(results[i, -1])
        name = get_labelname(labelmap, label)[0]
        color = colors[label % num_classes]

        xmin = int(round(results[i, 0]))
        ymin = int(round(results[i, 1]))
        xmax = int(round(results[i, 2]))
        ymax = int(round(results[i, 3]))
        coords = (xmin, ymin), xmax - xmin, ymax - ymin
        ax.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=3))
        display_text = '%s: %.2f' % (name, score)
        ax.text(xmin, ymin, display_text, bbox={'facecolor':color, 'alpha':0.5})
    if save_fig:
        dir_name = os.path.dirname(image_file)+'/out/'
        filename = os.path.basename(image_file)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        plt.savefig(dir_name + filename[:-4] + '_dets.jpg', bbox_inches="tight")
        print('Saved: ' + dir_name + filename[:-4] + '_dets.jpg')
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu_id', type=int, default=-1)
    parser.add_argument('--save_fig', default='true')
    args = parser.parse_args()

    # gpu preparation
    if args.gpu_id >= 0:
        caffe.set_device(args.gpu_id)
        caffe.set_mode_gpu()

    # load labelmap
    labelmap_file = caffe_root+'data/VOC0712/labelmap_voc.prototxt'
    file = open(labelmap_file, 'r')
    labelmap = caffe_pb2.LabelMap()
    text_format.Merge(str(file.read()), labelmap)

    # load model
    model_def = caffe_root+'models/VGGNet/refinedet_vgg16_512x512/deploy.prototxt'
    model_weights = caffe_root+'models/VGGNet/refinedet_vgg16_512x512/VOC0712_refinedet_vgg16_512x512_final.caffemodel'
    net = caffe.Net(model_def, model_weights, caffe.TEST)
    # image preprocessing
    if '320' in model_def:
        img_resize = 320
    else:
        img_resize = 512
    time.sleep(5)
    net.blobs['data'].reshape(1, 3, img_resize, img_resize)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))
    transformer.set_mean('data', np.array([104, 117, 123]))  # mean pixel
    transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
    transformer.set_channel_swap('data', (2, 1, 0))  # the reference model has channels in BGR order instead of RGB

    image_files = glob.glob(caffe_root+'examples/images/*.jpg')
    time_now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    print(time_now,image_files)
    for image_file in image_files:
        image = caffe.io.load_image(image_file)
        transformed_image = transformer.preprocess('data', image)
        net.blobs['data'].data[...] = transformed_image

        detections = net.forward()['detection_out']
        det_label = detections[0, 0, :, 1]
        det_conf = detections[0, 0, :, 2]
        print("det_conf:",sorted(det_conf))
        det_xmin = detections[0, 0, :, 3] * image.shape[1]
        det_ymin = detections[0, 0, :, 4] * image.shape[0]
        det_xmax = detections[0, 0, :, 5] * image.shape[1]
        det_ymax = detections[0, 0, :, 6] * image.shape[0]
        result = np.column_stack([det_xmin, det_ymin, det_xmax, det_ymax, det_conf, det_label])

        # show result
        ShowResults(image, image_file, result, labelmap, 0.5, save_fig=args.save_fig)