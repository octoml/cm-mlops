rem Compile

echo.
echo Compiling program ...
echo.

cd %CM_CURRENT_SCRIPT_PATH%

%CM_C_COMPILER_WITH_PATH% -O3 susan.c
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem Return to the original path obtained in CM

echo.
echo Running program ...
echo.

cd %CM_CURRENT_PATH%

IF NOT DEFINED CM_INPUT SET CM_INPUT=%CM_CURRENT_SCRIPT_PATH%\data.pgm
IF NOT DEFINED CM_OUTPUT SET CM_OUTPUT=output_image_with_edges.pgm

%CM_CURRENT_SCRIPT_PATH%\a.exe %CM_INPUT% %CM_OUTPUT% -c
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem -c
rem -e
rem -s

