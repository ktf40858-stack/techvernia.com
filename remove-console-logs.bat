@echo off
REM ==============================================
REM TechVernia - Remove Console Logs (Windows)
REM ==============================================

echo.
echo ===================================
echo TechVernia Console Log Remover
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.x from https://www.python.org/
    pause
    exit /b 1
)

REM Check if script exists
if not exist "remove-console-logs.py" (
    echo ERROR: remove-console-logs.py not found
    echo Please ensure the script is in the current directory
    pause
    exit /b 1
)

REM Run with dry-run first
echo Running in DRY-RUN mode first...
echo.
python remove-console-logs.py --dry-run --directory techvernia.com\js

echo.
echo.
echo ===================================
set /p CONFIRM="Apply these changes? (y/n): "

if /i "%CONFIRM%"=="y" (
    echo.
    echo Applying changes...
    python remove-console-logs.py --directory techvernia.com\js
    echo.
    echo Done! Backup files created with .backup extension
) else (
    echo.
    echo Cancelled. No files were modified.
)

echo.
pause
