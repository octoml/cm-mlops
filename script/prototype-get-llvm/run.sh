#!/bin/bash

${CM_LLVM_CLANG_BIN} --version > tmp-ver.out
test $? -eq 0 || exit 1
