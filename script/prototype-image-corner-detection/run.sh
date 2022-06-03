#!/bin/bash

CM_CURRENT_SCRIPT_PATH=${CM_CURRENT_SCRIPT_PATH:-$PWD}

pushd ${CM_CURRENT_SCRIPT_PATH}

${CM_C_COMPILER_WITH_PATH} -lm susan.c

./a.out data.pgm data_edges.pgm -c

popd
