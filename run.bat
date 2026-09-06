@echo off
python project.py
if errorlevel 1 (
    echo Попытка запустить через py...
    py project.py
)
pause