cd %CM_CURRENT_SCRIPT_PATH%

%CM_C_COMPILER_WITH_PATH% -O1 susan.c

a.exe data.pgm data_edges.pgm -c

cd %CM_CURRENT_PATH%


rem -c
rem -e
rem -s

