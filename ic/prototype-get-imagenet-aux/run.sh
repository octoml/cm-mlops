wget -nc http://dl.caffe.berkeleyvision.org//caffe_ilsvrc12.tar.gz --no-check-certificate
mkdir data
tar -C data -xvzf caffe_ilsvrc12.tar.gz
rm -rf caffe_ilsvrc12.tar.gz

echo "CM_DATASET_AUX_PATH=$PWD/data" > tmp-run-env.out
