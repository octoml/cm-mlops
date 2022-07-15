#!/bin/bash

# Run

echo "Executing ${CM_RUN_COMMAND}..."
eval ${CM_RUN_COMMAND}

test $? -eq 0 || exit 1
