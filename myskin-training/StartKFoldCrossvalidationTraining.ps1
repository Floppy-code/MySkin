#Runs Training on k folds
$TrainingFileName = "NeuralNetworkTrainingVGG19.py"
$TrainingScriptPath = "C:\Users\juraj\source\repos\MySkin\myskin-training\training\$TrainingFileName"
$PythonEnviromentPath = "C:\Users\juraj\source\enviroments\MySkinTraining\Scripts\python.exe"

$learning_rate = "7"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 0 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 1 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 2 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 3 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 4 $learning_rate"

$learning_rate = "6"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 0 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 1 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 2 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 3 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 4 $learning_rate"

$learning_rate = "5"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 0 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 1 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 2 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 3 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 4 $learning_rate"

$learning_rate = "4"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 0 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 1 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 2 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 3 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 4 $learning_rate"

$learning_rate = "3"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 0 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 1 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 2 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 3 $learning_rate"
Start-Process -Wait -NoNewWindow $PythonEnviromentPath "$TrainingScriptPath 4 $learning_rate"