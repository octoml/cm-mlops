#!/bin/bash

echo "************************************************"
echo "Installing some system dependencies via sudo apt"
echo "Enter skip to skip this step or press enter to continue:"
read DUMMY

if [[ "$DUMMY" == "skip" ]]; then exit 0; fi

brew update && \
     brew install \
           git \
           wget \
           curl \
           zip \
           unzip \
           bzip2 \
           vim \
           mc \
           tree \
           gcc \
           autoconf \
           autogen \
           libtool \
           make \
           cmake \
           python3
