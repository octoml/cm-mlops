rem Compile

del a.exe

echo.
echo Checking clang version ...
echo.

clang --version

echo.
echo Compiling program ...
echo.

cd %CM_TMP_CURRENT_SCRIPT_PATH%

%CM_C_COMPILER_WITH_PATH% -O3 susan.c
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem Return to the original path obtained in CM

echo.
echo Running program ...
echo.

cd %CM_TMP_CURRENT_PATH%

IF NOT DEFINED CM_INPUT SET CM_INPUT=%CM_TMP_CURRENT_SCRIPT_PATH%\data.pgm
IF NOT DEFINED CM_OUTPUT SET CM_OUTPUT=output_image_with_corners.pgm

del %CM_OUTPUT%

%CM_TMP_CURRENT_SCRIPT_PATH%\a.exe %CM_INPUT% %CM_OUTPUT% -c
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem -c
rem -e
rem -s

