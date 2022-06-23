if [ -n ${CM_VERSION} ]; then
    VERSION_STRING=">=${CM_VERSION}"
elif [ -n ${CM_VERSION_MIN}  and -n ${CM_VERSION_MAX} ]; then
    VERSION_STRING=">=${CM_VERSION_MIN},<=${CM_VERSION_MAX}"
elif [ -n ${CM_VERSION_MAX} ]; then
    VERSION_STRING="<=${CM_VERSION_MAX}"
else
    VERSION_STRING=""
fi
pip3 install --upgrade pip
pip3 install setuptools testresources wheel h5py --user --upgrade --ignore-installed
curl https://sh.rustup.rs -sSf -o tmp.sh
sh tmp.sh -y 
export PATH=$PATH:$HOME/.cargo/bin
pip3 install tensorflow-aarch64${VERSION_STRING} -f https://tf.kmtea.eu/whl/stable.html --user
test $? -eq 0 || exit 1
