#!/bin/bash

CUR_DIR=$PWD

echo "******************************************************"
echo "Cloning LLVM from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."

if [ ! -d "llvm" ]; then
  git clone -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} llvm
  if [ "${?}" != "0" ]; then exit 1; fi
fi

mkdir -p install
mkdir -p build

INSTALL_DIR="${CUR_DIR}/install"

echo "******************************************************"

cd build

cmake ../llvm/llvm \
    -DLLVM_ENABLE_PROJECTS=clang \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}" \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_INSTALL_UTILS=ON \
    ../llvm/
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
CM_HOST_CPU_NUMBER_OF_PROCESSORS=${CM_HOST_CPU_NUMBER_OF_PROCESSORS:-2}

cmake --build . --target install -j${CM_HOST_CPU_NUMBER_OF_PROCESSORS}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory (too large)
cd ${CUR_DIR}
rm -rf build

echo "******************************************************"
echo "LLVM was built and installed to ${INSTALL_DIR} ..."
