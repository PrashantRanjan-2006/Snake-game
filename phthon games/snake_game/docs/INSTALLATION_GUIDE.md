# Installation Guide - Modern Snake Game

## Windows Users

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click "Install Now"

### Step 2: Open Command Prompt
1. Press `Win + R`
2. Type `cmd` and press Enter
3. Or search for "Command Prompt" in Start Menu

### Step 3: Install Pygame
Type this command and press Enter:
```bash
pip install pygame
```

### Step 4: Run the Game
1. Navigate to the snake_game folder:
```bash
cd path\to\snake_game
```

2. Run the game:
```bash
python main.py
```

---

## Mac Users

### Step 1: Check Python Installation
Open Terminal and type:
```bash
python3 --version
```

### Step 2: Install Pygame
```bash
pip3 install pygame
```

Or using Homebrew:
```bash
brew install pygame
```

### Step 3: Run the Game
Navigate to the snake_game folder:
```bash
cd path/to/snake_game
python3 main.py
```

---

## Linux Users (Ubuntu/Debian)

### Step 1: Install Python and Pygame
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
pip3 install pygame
```

### Step 2: Run the Game
```bash
cd path/to/snake_game
python3 main.py
```

### For Fedora:
```bash
sudo dnf install python3 python3-pip
pip3 install pygame
```

---

## Using a Virtual Environment (Recommended)

### Creating a Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install pygame
python main.py
```

#### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install pygame
python3 main.py
```

---

## Automatic Setup Script (Windows)

Save this as `setup.bat` in the snake_game folder:

```batch
@echo off
echo Installing Snake Game...
echo Installing Pygame...
pip install pygame
echo Setup complete! You can now run: python main.py
pause
```

Double-click `setup.bat` to run.

---

## Quick Verification

Test that everything is working:

```bash
python -c "import pygame; print('✓ Pygame is installed!'); pygame.init(); print('✓ Pygame initialized successfully!')"
```

If you see both checkmarks, you're ready to play!

---

## Troubleshooting

### "pip: command not found"
- Python might not be in PATH
- Reinstall Python and check "Add Python to PATH"
- Or use: `python -m pip install pygame`

### "pygame module not found"
- Try: `python -m pip install pygame`
- Or: `pip3 install pygame` (if using Python 3)

### Permission Denied (on Mac/Linux)
- Use: `sudo pip3 install pygame`
- Or use a virtual environment

### SSL Certificate Error
- Try: `pip install --trusted-host pypi.python.org -i https://pypi.python.org/simple pygame`

---

## Getting Help

If installation fails:
1. Check Python is installed: `python --version`
2. Check pip works: `pip --version`
3. Update pip: `python -m pip install --upgrade pip`
4. Then retry: `pip install pygame`

---

**Still having issues?** The game will work with just Python - sound will be disabled if Pygame won't install, but the game will still run using Pygame's drawing functions.
