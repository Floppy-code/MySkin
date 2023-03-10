#Runs Training on k folds
$TrainingScriptPath = "C:\Users\juraj\source\repos\MySkin\myskin-training\training\NeuralNetworkTraining.py"
$PythonEnviromentPath = "C:\Users\juraj\source\enviroments\MySkinTraining\Scripts\python.exe"

Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 0"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 1"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 2"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 3"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 4"