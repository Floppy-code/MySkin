#Runs Training on k folds
$TrainingFileName = "NeuralNetworkTrainingEfficientNetV2M.py"
$TrainingScriptPath = "C:\Users\juraj\source\repos\MySkin\myskin-training\training\$TrainingFileName"
$PythonEnviromentPath = "C:\Users\juraj\source\enviroments\MySkinTraining\Scripts\python.exe"

Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 0"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 1"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 2"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 3"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 4"