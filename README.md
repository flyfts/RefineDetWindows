Single-Shot Refinement Neural Network for Object Detection
===========================================================
This is a windows version of RefineDet,please refer https://github.com/sfzhang15/RefineDet for more details.

This project was tested on Windows10 + Visual Studio 2013.The third party tools discribed as follows: <br>
*  boost.1.59.0.0(When you bulid your project,you should unzip the zip files in the folder \3rdparty\boost.1.59.0.0\lib first) <br>
*  gflags.2.0.1.0 <br>
*  glog.0.3.3.0 <br>
*  hdf5.1.8.15.2 <br>
*  LevelDB.1.2.0.0 <br>
*  lmdb.0.9.14.0 <br>
*  OpenBLAS.0.2.14.1 <br>
*  opencv2.4.11 <br>
*  protobuf-2.5.0 <br>
*  python2.7(You can bulid your own python3 version,the levelDB and boost should be rebuilt to support it)

1.Installation
------------------------------------------
git clone https://github.com/flyfts/RefineDetWindows.git


2.Preparation
------------------------------------------
This project was tested on Windows 10 + Visual Studio 2013.You should setup Visual Studio 2013 enviroment(also you can bulid the project on Visual Studio 2015 or other VS version,the corespond libs like boost should be re-compile to fit the VS version). <br>


3.Training
------------------------------------------
Please follow the part descibed in https://github.com/sfzhang15/RefineDet <br>


4.Evaluation
------------------------------------------
Check out test/refinedet_demo.py on how to detect objects using the RefineDet model and how to plot detection results.<br>
#For GPU Users<br>
python test/refinedet_demo.py<br>
#For CPU Users<br>
python test/refinedet_demo.py --gpu_id -1 <br>

5.Models
------------------------------------------
Please follow the part described in https://github.com/sfzhang15/RefineDet <br>
They have provided the models that are trained from different datasets. <br>

PASCAL VOC models (VGG-16): <br> 
* 07+12: [RefineDet320](https://drive.google.com/open?id=1rj6ikGCJg_rOlt0gUCXkjHzPkjpvzxXV), [RefineDet512](https://drive.google.com/open?id=10Fwymi1HizebH3qnyZmecXRvtBc1HCop)<br>
* 07++12: [RefineDet320](https://drive.google.com/open?id=1d1T_tTImZynD88CoB0OF0rdFXgp4E_le), [RefineDet512](https://drive.google.com/open?id=1h9IrfBHKnO1tQq3PWmo0TLhQcx7lUHhj) <br>
* COCO: [RefineDet320](https://drive.google.com/open?id=1dl-eyCZgDv_UwxGb2c1Usaqq2u2u7sqz), [RefineDet512](https://drive.google.com/open?id=1vJ8CZlOocsF5cASr3k2Or1vQx-hTfxs6) <br>
* 07+12+COCO: [RefineDet320](https://drive.google.com/open?id=1c8umLHI-x68uxT7CcCirFPhykPkyYUzC), [RefineDet512](https://drive.google.com/open?id=1-d4w152HsEaYgWY7v4_6zqxxQIijlHjX) <br>
* 07++12+COCO: [RefineDet320](https://drive.google.com/open?id=1pti47J-oE7Os02vNvO0JIrQp3_FQR70v), [RefineDet512](https://drive.google.com/open?id=1ZwnO_F1Pqdg1xyNSa-0XPEuh7knel9L_) <br>

COCO models: <br> 
* trainval35k (VGG-16): [RefineDet320](https://drive.google.com/open?id=1BIVvkSQM8DarpeqOpjgPpDxUoFq9ZxKM), [RefineDet512](https://drive.google.com/open?id=16j7gmHvd82LSog52kBXUUYyLx26mOV_6) <br>
* trainval35k (ResNet101): [RefineDet320](https://drive.google.com/open?id=1yrCfPIyKNsD9aBnn5iooFoX414FzXvzH), [RefineDet512](https://drive.google.com/open?id=1KWdfrowNIJqJF0j-ZxkQpkbAcPPbwAS1) <br>

Note: If you can not download pre-trained models through the above links, you can download them through BaiduYun.


