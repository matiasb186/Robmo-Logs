@echo off
:loop
start chrome "https://www.youtube.com"
timeout /t 5 /nobreak > nul
start chrome "https://www.youtube.com"
timeout /t 5 /nobreak > nul
goto loop
