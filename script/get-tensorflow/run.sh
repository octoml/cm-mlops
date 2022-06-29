#!/bin/bash

CM_PYTHON_BIN_WITH_PATH=${CM_PYTHON_BIN_WITH_PATH:-python3}
${CM_PYTHON_BIN_WITH_PATH} -c '
try:
    import tensorflow as tf
    print(tf.__version__)
except ImportError as e:
    from sys import stderr
'  > tmp-ver.out
test $? -eq 0 || exit 1
