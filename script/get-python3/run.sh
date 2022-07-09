#!/bin/bash
if [[ ${CM_INSTALL_PYTHON} != "yes" ]]; then
  ${CM_PYTHON_BIN_WITH_PATH} --version > tmp-ver.out
  test $? -eq 0 || exit 1
  exit 0
fi

CUR_DIR=$PWD

echo "***********************************************************"
export PYTHON_VERSION=${CM_VERSION}
CM_WGET_URL="${CM_WGET_URL//"[PYTHON_VERSION]"/"$PYTHON_VERSION"}"

echo "CM_WGET_URL=${CM_WGET_URL}" >> tmp-run-env.out
echo "wget Python src from ${CM_WGET_URL} for version ${PYTHON_VERSION}..."

CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_NUMBER_OF_PROCESSORS}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

if [[ ${CM_SHARED_BUILD} == "yes" ]]; then
  SHARED_BUILD_FLAGS=" --enable-shared --enable-ssl"
else
  SHARED_BUILD_FLAGS=""
fi
if [[ ${CM_ENABLE_SSL} == "yes" ]]; then
  EXTRA_FLAGS=" --enable-ssl"
else
  EXTRA_FLAGS=""
fi

if [ "${?}" != "0" ]; then exit 1; fi
#rm -rf install
#rm -rf src

if [ ! -d "src" ]; then
  mkdir src
  cd src
  wget -nc ${CM_WGET_URL}
  tar xzf Python-${PYTHON_VERSION}.tgz && \
  rm -f Python-${PYTHON_VERSION}.tgz
  cd Python-${PYTHON_VERSION} && \
  ./configure --enable-optimizations ${SHARED_BUILD_FLAGS} ${EXTRA_FLAGS} --with-ensurepip=install --prefix=${CUR_DIR}/install
  if [ "${?}" != "0" ]; then exit 1; fi
  cd ${CUR_DIR}
fi

if [ ! -d "${CUR_DIR}/install" ]; then
  mkdir ${CUR_DIR}/install
  cd src/Python-${PYTHON_VERSION}
  make -j${CM_MAKE_CORES} install && \
  cd ${CUR_DIR}/install/bin && ln -s python3 python
  cd ${CUR_DIR} 
  #rm -rf src
fi

if [ "${?}" != "0" ]; then exit 1; fi

echo "CM_TMP_PATH=${CUR_DIR}/install/bin" >> tmp-run-env.out
echo "CM_TMP_FAIL_IF_NOT_FOUND=yes" >> tmp-run-env.out
if [ "${?}" != "0" ]; then exit 1; fi
echo "********************************************************"
echo "Python was built and installed to ${CUR_DIR}/install ..."


