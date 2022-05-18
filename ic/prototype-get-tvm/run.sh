git clone --recursive https://github.com/apache/tvm tvm
test $? -eq 0 || exit 1

cd tvm 
mkdir build

cp cmake/config.cmake build

cd build

sed -i.bak 's/set(USE_LLVM OFF)/set(USE_LLVM ON)/' config.cmake

cmake ..
test $? -eq 0 || exit 1

make -j4
test $? -eq 0 || exit 1

cd ../../

echo "TVM_HOME=$PWD/tvm" > tmp-run-env.out
