CM_CURRENT_IC_PATH=${CM_CURRENT_IC_PATH:-$PWD}

${CM_PYTHON_BIN} ${CM_CURRENT_IC_PATH}/code.py
test $? -eq 0 || exit $?

echo "CM_NEW_VAR_FROM_RUN=$MLPERF_XYZ" > tmp-run-env.out
