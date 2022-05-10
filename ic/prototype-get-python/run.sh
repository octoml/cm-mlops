CM_PYTHON_BIN=${CM_PYTHON_BIN:-python3}

echo ${CM_PYTHON_BIN_WITH_PATH}
${CM_PYTHON_BIN} --version > tmp-ver.out
