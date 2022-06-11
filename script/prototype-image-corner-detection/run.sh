#!/bin/bash

# Compile

echo ""
echo "Compiling program ..."
echo ""

cd ${CM_CURRENT_SCRIPT_PATH}

${CM_C_COMPILER_WITH_PATH} -O3 -lm susan.c
test $? -eq 0 || exit 1

# Return to the original path obtained in CM

echo ""
echo "Running program ..."
echo ""

cd ${CM_CURRENT_PATH}

CM_INPUT=${CM_INPUT:-${CM_CURRENT_SCRIPT_PATH}/data.pgm}
CM_OUTPUT=${CM_OUTPUT:-output_image_with_corners.pgm}

${CM_CURRENT_SCRIPT_PATH}/a.out ${CM_INPUT} ${CM_OUTPUT} -c
test $? -eq 0 || exit 1
