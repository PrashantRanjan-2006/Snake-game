@echo off
REM Modern Snake Game - Setup Script for Windows
REM This script installs Pygame and sets up the game

echo ============================================
echo Modern Snake Game - Setup
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✓ Python found: 
python --version

echo.
echo Installing Pygame...
python -m pip install pygame

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install Pygame
    echo Try running Command Prompt as Administrator
    pause
    exit /b 1
)

echo.
echo ✓ Setup complete!
echo.
echo You can now run the game by typing:
echo     python main.py
echo.
pause
