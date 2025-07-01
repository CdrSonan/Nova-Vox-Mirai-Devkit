@echo off
setlocal

set VENV_DIR=venv

if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Creating Python virtual environment...
    python -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Failed to create virtual environment.
        exit /b 1
    )
    echo Installing requirements...
    "%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
    "%VENV_DIR%\Scripts\python.exe" -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install requirements.
        exit /b 1
    )
)

call "%VENV_DIR%\Scripts\activate.bat"
python app.py

endlocal