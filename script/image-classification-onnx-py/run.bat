rem echo %CM_PYTHON_BIN%
rem echo %CM_DATASET_PATH%
rem echo %CM_DATASET_AUX_PATH%
rem echo %CM_ML_MODEL_FILE_WITH_PATH%

rem connect CM intelligent components with CK env
set CK_ENV_ONNX_MODEL_ONNX_FILEPATH=%CM_ML_MODEL_FILE_WITH_PATH%
set CK_ENV_ONNX_MODEL_INPUT_LAYER_NAME=input_tensor:0
set CK_ENV_ONNX_MODEL_OUTPUT_LAYER_NAME=softmax_tensor:0
set CK_ENV_DATASET_IMAGENET_VAL=%CM_DATASET_PATH%
set CK_CAFFE_IMAGENET_SYNSET_WORDS_TXT=%CM_DATASET_AUX_PATH%\synset_words.txt
set ML_MODEL_DATA_LAYOUT=NCHW
set CK_BATCH_SIZE=%CM_BATCH_SIZE%
set CK_BATCH_COUNT=%CM_BATCH_COUNT%

IF NOT DEFINED CM_TMP_CURRENT_SCRIPT_PATH SET CM_TMP_CURRENT_SCRIPT_PATH=%CD%

IF DEFINED CM_INPUT SET CM_IMAGE=%CM_INPUT%

%CM_PYTHON_BIN% -m pip install -r %CM_TMP_CURRENT_SCRIPT_PATH%\requirements.txt

%CM_PYTHON_BIN% %CM_TMP_CURRENT_SCRIPT_PATH%\src\onnx_classify.py
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%