if [[ ${CM_HOST_OS_FLAVOR} == "macos" ]]; then
    sysctl -a | grep machdep.cpu > tmp-lscpu.out
else
	echo  ${CM_HOST_OS_FLAVOR} 
    lscpu > tmp-lscpu.out
fi
