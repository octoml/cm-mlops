#!/bin/bash

${CM_BAZEL_BIN_WITH_PATH} --version  > tmp-ver.out
test $? -eq 0 || exit 1
