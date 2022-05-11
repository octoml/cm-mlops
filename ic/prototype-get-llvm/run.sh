CM_LLVM_CLANG_BIN=${CM_LLVM_CLANG_BIN:-clang}

echo ${CM_LLVM_CLANG_BIN_WITH_PATH}
${CM_LLVM_CLANG_BIN} --version > tmp-ver.out
