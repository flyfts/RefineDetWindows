root_dir="F:/Caffe/RefineDetClean"
cd $root_dir

redo=1
data_root_dir="$root_dir/data/VOC0712/"
dataset_name="VOC0712"
mapfile="$root_dir/data/$dataset_name/labelmap_voc.prototxt"

echo data_root_dir $data_root_dir
echo dataset_name $dataset_name
echo mapfile $mapfile

anno_type="detection"
db="lmdb"
min_dim=0
max_dim=0
width=512
height=512

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ]
then
  extra_cmd="$extra_cmd --redo"
fi
for subset in trainval test
do
  python $root_dir/scripts/create_annoset.py --anno-type=$anno_type --label-map-file=$mapfile --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height --check-label $extra_cmd $data_root_dir $root_dir/data/$dataset_name/$subset.txt $data_root_dir/$dataset_name/$dataset_name"_"$subset"_"$db examples/$dataset_name
done

read -p "press any key to continue"
echo continue
