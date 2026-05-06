# 🚀 Quick Start Guide

Get the Snake Game running in 5 minutes!

## One-Minute Setup (Windows)

### Option 1: Automatic (Easiest)
1. Open `setup.bat` (double-click)
2. Wait for it to finish
3. Run `python main.py`

### Option 2: Manual
1. Open Command Prompt (Win+R, type `cmd`)
2. Paste this and press Enter:
   ```
   pip install pygame && python main.py
   ```

## One-Minute Setup (Mac/Linux)

1. Open Terminal
2. Copy and paste this:
   ```bash
   pip3 install pygame && cd snake_game && python3 main.py
   ```

## Instant Verification

Run this to check if everything works:
```bash
python -c "import pygame; print('✓ Ready to play!')"
```

---

## 🎮 Playing the Game

### Main Menu
- Click "START GAME" or press Enter
- Click "QUIT" to exit

### During Gameplay
| Control | Action |
|---------|--------|
| ⬆️ ⬇️ ⬅️ ➡️ | Move snake |
| **W A S D** | Alternative controls |
| **P** | Pause/Resume |
| **ESC** | Return to menu |
| **F11** | Fullscreen |

### Game Over
- Click "RESTART" to play again
- Click "MAIN MENU" to return to menu
- Eat food to grow and score points
- Watch your level increase as you score!

---

## 📊 What to Expect

**First Run:**
- ✓ Main menu with glowing buttons
- ✓ Grid background with neon colors
- ✓ Snake moving smoothly
- ✓ Food appearing randomly
- ✓ Score tracking
- ✓ Levels that increase every 50 points

---

## 🆘 If It Doesn't Work

### "No module named 'pygame'"
```bash
pip install pygame
python main.py
```

### "Python not found"
- Download from: https://www.python.org/downloads/
- **Important**: Check "Add Python to PATH"

### Game runs but very slow/fast
- This is normal! Game speed increases with levels
- Starting speed should be playable

### Graphics glitchy
- Update your graphics drivers
- Use a different resolution (edit SCREEN_WIDTH/HEIGHT in main.py)

---

## 🎯 Scoring Tips

1. **Early game**: Build up a long snake for bigger scores
2. **Pattern play**: Create loops to efficiently catch food
3. **Space management**: Don't corner yourself
4. **Watch the level**: Each level gets progressively faster
5. **Aim high**: Best score wins! 🏆

---

## 📁 Files You'll See

- `main.py` - Main game (run this!)
- `highscore.txt` - Your best score (created automatically)
- `README.md` - Full documentation
- `INSTALLATION_GUIDE.md` - Detailed setup
- `ASSETS_GUIDE.md` - How to add sounds
- `assets/` - Sound and font folder (optional)

---

## ⚙️ Customization

### Difficulty Too Hard?
Edit `main.py`:
```python
INITIAL_SPEED = 10  # Change to 5-7 for easier
MAX_SPEED = 25      # Change to 15-20 for slower max
```

### Screen Too Small?
```python
SCREEN_WIDTH = 1000   # Increase to 1280 or 1600
SCREEN_HEIGHT = 700   # Increase to 800 or 900
```

---

## 🎉 You're Ready!

**Run the game:** `python main.py`

**Have fun!** 🐍

---

## 📚 Next Steps

- Read `README.md` for full features
- Check `ASSETS_GUIDE.md` to add sounds
- Modify `main.py` to customize colors/difficulty
- Challenge friends to beat your high score!

**Questions?** See the troubleshooting sections in README.md
