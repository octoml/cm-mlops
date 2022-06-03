#!/bin/bash

CM_CURRENT_SCRIPT_PATH=${CM_CURRENT_SCRIPT_PATH:-$PWD}
cp -r ${CM_CURRENT_SCRIPT_PATH}/imagenet_helper $PWD/

echo "PYTHONPATH=${PYTHONPATH}:$PWD" > tmp-run-env.out
