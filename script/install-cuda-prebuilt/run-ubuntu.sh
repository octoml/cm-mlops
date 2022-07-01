if [[ ${USE_PACKAGE_MANAGER_INSTALL} == "yes" ]]; then
  sudo apt-get install nvidia-cuda-toolkit
else
  . ${CM_TMP_CURRENT_SCRIPT_PATH}/run.sh
fi
