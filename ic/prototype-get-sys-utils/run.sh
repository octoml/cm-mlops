CM_APT_TOOL=${CM_APT_TOOL:-apt}

${CM_SUDO} ${CM_APT_TOOL} update && \
    ${CM_SUDO} ${CM_APT_TOOL} install -y --no-install-recommends \
           apt-utils \
           git wget zip bzip2 libz-dev libbz2-dev cmake curl unzip \
           openssh-client vim mc tree \
           gcc g++ autoconf autogen libtool make libc6-dev build-essential patch \
           gfortran libblas-dev liblapack-dev \
           libsndfile1-dev libssl-dev libbz2-dev libxml2-dev libtinfo-dev libffi-dev \
           python3 python3-pip python3-dev \
           libtinfo-dev \
           python-is-python3 \
           sudo
