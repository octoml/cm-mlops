# 20220719
 * moved stable scripts to https://github.com/mlcommons/cm-mlops

# 20220718
 * fixed local_env_keys in get-python3
 * added new_env_only_keys to get-python3
 
# 20220712
 * added tags from deps (python, llvm)

# 20220708
 * various fixes to handle versions (min/max/default)

# 20220704
 * fixed get-python-venv

# 20220621
 * added prototype of get-virtual-env
 * added support for --quiet
 * changed CM_NEED_VERSION to CM_VERSION
 * added CM_VERSION_MIN, CM_VERSION_MAX
 * added support for local_env (remove from deps) - mainly version/min/max
 * added support in get-pytohn3 to detect min/max/correct versions

# 20220617
 * fixed logic to handle variations (-_): https://github.com/mlcommons/ck/issues/243

# 20220616
 * fixed TVM image classification workflow

# 20220615
 * major update of script (remove parallel env/new_env and state/new_state).
   keep global env & state and detect changes automatically
 * major simplification of "script"
 * removed "installed" to be more understandable
 * added "cached" to be more understandable

# 20220610
 * added "versions" key in script meta. 
   It is now possible to update env, new_env, deps from this dict using --version 
   or env CM_NEED_VERSION

# 20220608
 * deprecated "ic" automation. Use "script" instead!

# 20220606
 * Added prototype-test-deps-variations-tags to play with deps, variations, tags

# 20220603
 * Improved LLVM detection and installation
 * Added example of image corner detection
 * Added updated script entries

# 20220601
 * Updating mechanisms to install and/or detect LLVM
 * added support to install prebuilt LLVM for Linux, MacOs, Windows

# 20220525
 * Fixing basic IC to print hello world

# 20220517
 * Changed CM_PATH_LIST to +PATH
 * Added general support for +ENV that is expanded to ENV=val1;val2;...:${ENV}

# 20220511
 * Added prototype of ic::prototype-get-ml-model-resnet50-onnx with variations
 * Added prototype of ic::prototype-get-imagenet-val with variations
 * Added prototype of ic::prototype-get-imagenet-aux with variations
 * Added prototype of ic::prototype-get-llvm
 * Added prototype of ic::prototype-get-tvm
