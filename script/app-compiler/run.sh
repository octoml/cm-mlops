#!/bin/bash

# Compile

BIN_NAME=${CM_BIN_NAME:-run.out}
rm -f ${BIN_NAME}

if [ -z "${CM_SRC_FOLDER_PATH}" ]; then
  echo "No source directory (CM_SRC_FOLDER_PATH} specified"
  exit 1
fi

if [[ -z "${CM_C_SOURCE_FILES}"  && -z "${CM_CXX_SOURCE_FILES}" && -z "${CM_F_SOURCE_FILES}" ]]; then
  echo "No source files specified"
  exit 1
fi

echo ""
echo "Checking compiler version ..."
echo ""

${CM_C_COMPILER_WITH_PATH} --version

echo ""
echo "Compiling source files ..."
echo ""

cd ${CM_SRC_FOLDER_PATH}
IFS=';' read -ra FILES <<< "${CM_C_SOURCE_FILES}"
for file in "${FILES[@]}"; do
  base_name=${file%.*}
  CMD="${CM_C_COMPILER_WITH_PATH} -c ${CM_C_COMPILER_FLAGS} ${CM_C_INCLUDE_DIR} $file -o $base_name.o"
  echo $CMD
  eval $CMD
  test $? -eq 0 || exit 1
done


echo ""
echo "Linking ..."
echo ""
CMD="${CM_C_COMPILER_WITH_PATH} ${CM_LINKER_FLAGS} *.o -o ${BIN_NAME} ${CM_LD_LIBRARY_PATHS}"
echo $CMD
eval $CMD
./$BIN_NAME

test $? -eq 0 || exit 1
