#!/bin/bash

CM_PYTHON_BIN=${CM_PYTHON_BIN:-python3}
if [ -n ${CM_VERSION} ]; then
    VERSION_STRING="==${CM_VERSION}"
elif [ -n ${CM_VERSION_MIN}  and -n ${CM_VERSION_MAX} ]; then
    VERSION_STRING=">=${CM_VERSION_MIN},<=${CM_VERSION_MAX}"
elif [ -n ${CM_VERSION_MAX} ]; then
    VERSION_STRING="<=${CM_VERSION_MAX}"
else
    VERSION_STRING=""
fi

${CM_PYTHON_BIN} -m pip install tensorflow${VERSION_STRING}
test $? -eq 0 || exit 1
