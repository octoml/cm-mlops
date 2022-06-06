#!/bin/bash

git clone --recursive https://github.com/apache/tvm tvm
test $? -eq 0 || exit 1

cd tvm 
mkdir build

cp cmake/config.cmake build

cd build

if [[ ${CM_TVM_USE_LLVM} == "yes" ]]; then
    sed -i.bak 's/set(USE_LLVM OFF)/set(USE_LLVM ON)/' config.cmake
fi

if [[ ${CM_TVM_USE_OPENMP} == "yes" ]]; then
    sed -i.bak 's/set(USE_OPENMP none)/set(USE_OPENMP gnu)/' config.cmake
fi

cmake ..
test $? -eq 0 || exit 1

make -j4
test $? -eq 0 || exit 1

cd ../../

echo "TVM_HOME=$PWD/tvm" > tmp-run-env.out
