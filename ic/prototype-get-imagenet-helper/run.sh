CM_CURRENT_IC_PATH=${CM_CURRENT_IC_PATH:-$PWD}
cp -r ${CM_CURRENT_IC_PATH}/imagenet_helper $PWD/

echo "PYTHONPATH=${PYTHONPATH}:$PWD" > tmp-run-env.out
