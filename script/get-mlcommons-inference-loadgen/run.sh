#!/bin/bash

CUR_DIR=$PWD

echo "******************************************************"
echo "Cloning Mlcommons from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."

if [ ! -d "inference" ]; then
  git clone -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} inference
  if [ "${?}" != "0" ]; then exit 1; fi
fi

mkdir -p install
mkdir -p build

INSTALL_DIR="${CUR_DIR}/install"

echo "******************************************************"

cd build

cmake \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}" \
    ../inference/loadgen
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_NUMBER_OF_PROCESSORS}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

cmake --build . --target install -j${CM_MAKE_CORES}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory (too large)
cd ${CUR_DIR}
rm -rf build

echo "******************************************************"
echo "Loadgen is built and installed to ${INSTALL_DIR} ..."
