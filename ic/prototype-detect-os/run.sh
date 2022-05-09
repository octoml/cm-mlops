uname -m > tmp-run.out
uname -a >> tmp-run.out

echo "CM_HOST_OS_TEST=$pwd" > tmp-run-env.out
echo "CM_HOST_OS_VER=`uname -r`" >> tmp-run-env.out
