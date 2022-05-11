wget -nc https://www.dropbox.com/s/57s11df6pts3z69/ILSVRC2012_img_val_500.tar --no-check-certificate
mkdir images
tar -C images -xvf ILSVRC2012_img_val_500.tar
rm -rf ILSVRC2012_img_val_500.tar

echo "CM_DATASET_PATH=$PWD/images" > tmp-run-env.out
