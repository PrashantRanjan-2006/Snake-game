# Modern Snake Game - Complete Setup & Play Guide

## 🎮 WELCOME!

You now have a fully-featured, professional Snake Game ready to play!

---

## ⚡ Quick Start (30 seconds)

### Windows
1. Open Command Prompt
2. Navigate to the game folder: `cd path\to\snake_game`
3. Run: `python main.py`

### Mac/Linux
1. Open Terminal
2. Navigate to the game folder: `cd path/to/snake_game`
3. Run: `python3 main.py`

---

## 📦 What You Got

### Main File
- **main.py** - The complete game (1 file!)

### Documentation
- **README.md** - Full features and guide
- **QUICKSTART.md** - Fast setup guide
- **INSTALLATION_GUIDE.md** - Detailed installation help
- **ASSETS_GUIDE.md** - How to add sounds and fonts
- **FEATURES.md** - Complete feature checklist

### Setup Scripts (Optional)
- **setup.bat** - Windows automatic setup
- **setup.sh** - Mac/Linux automatic setup
- **test.py** - Verify game is working

### Data Storage
- **highscore.txt** - Your high scores (auto-created)

### Asset Folders
- **assets/sounds/** - Place sound effects here
- **assets/fonts/** - Place custom fonts here

---

## 🎮 GAME CONTROLS

| Input | Action |
|-------|--------|
| **↑ ↓ ← →** | Move snake |
| **W A S D** | Alternative move |
| **P** | Pause/Resume |
| **ESC** | Back to menu |
| **F11** | Toggle fullscreen |
| **Mouse Click** | Select menu buttons |

---

## 🚀 HOW TO PLAY

### 1. Start the Game
```bash
python main.py
```

### 2. Main Menu
- Click "START GAME" or press Enter to start
- Click "QUIT" to exit

### 3. Gameplay
- Use arrow keys to move the snake
- Eat the yellow food squares
- Each food gives 10 points
- Snake grows longer with each food
- Game speed increases with score

### 4. Game Over
- Game ends if you hit a wall or yourself
- Click "RESTART" to play again
- Click "MAIN MENU" to return to start
- Your high score is automatically saved

### 5. Winning Strategy
- Keep the snake away from walls
- Don't let the snake hit itself
- Plan moves ahead
- Try to beat your high score!

---

## 📊 GAME PROGRESSION

| Points | Level | Speed |
|--------|-------|-------|
| 0-49   | 1     | 10    |
| 50-99  | 2     | 12    |
| 100-149| 3     | 14    |
| 150-199| 4     | 16    |
| 200+   | 5+    | 18+   |

Maximum level: 15 (Speed: 25)

---

## 🔧 INSTALLATION TROUBLESHOOTING

### Problem: "Python not found"
**Solution:**
```bash
# Check if Python is installed
python --version

# If not, install from: https://www.python.org/downloads/
```

### Problem: "No module named pygame"
**Solution:**
```bash
# Install pygame
pip install pygame

# Then run the game
python main.py
```

### Problem: "Command not found" (Mac/Linux)
**Solution:**
```bash
# Use python3 instead
python3 -c "import pygame; print('OK')"
python3 main.py
```

### Problem: Game runs but very slow/fast
**Note:** Game speed increases with levels. Starting speed should be manageable.
**To adjust:**
1. Edit `main.py`
2. Change `INITIAL_SPEED = 10` to `INITIAL_SPEED = 5` (easier)
3. Save and restart

### Problem: No sound
**Note:** This is normal! Sound is optional.
**To add sounds:**
1. See [ASSETS_GUIDE.md](ASSETS_GUIDE.md)
2. Add .wav files to `assets/sounds/`
3. Filenames: `eat.wav`, `gameover.wav`, `click.wav`

---

## 🎨 CUSTOMIZATION

### Easy Customizations

**1. Change Difficulty**
Edit these lines in `main.py`:
```python
INITIAL_SPEED = 10      # Change to 5-7 for easier
MAX_SPEED = 25          # Change to 15-20 for slower
```

**2. Change Game Window Size**
```python
SCREEN_WIDTH = 1000     # Increase to 1280 or 1600
SCREEN_HEIGHT = 700     # Increase to 800 or 900
```

**3. Change Colors**
```python
COLOR_NEON_GREEN = (0, 255, 150)    # Change RGB values
COLOR_NEON_BLUE = (0, 150, 255)
# etc...
```

**4. Adjust Difficulty Increase Rate**
```python
DIFFICULTY_INCREASE_INTERVAL = 5    # Increase every 5 points
```

---

## 📱 GAME FEATURES

### Graphics
- Modern neon color scheme
- Smooth animations
- Grid background
- Particle effects on food eating
- Animated snake eyes
- Professional UI design

### Gameplay
- 15 difficulty levels
- Progressive speed increase
- Collision detection
- Food spawning system
- Smooth movement

### Audio (Ready)
- Eating sound support
- Game over sound support
- Button click sounds support
- (See ASSETS_GUIDE.md to add)

### Data
- High score tracking
- Score persistence
- Auto-save feature

### UI
- Main menu with buttons
- Pause screen
- Game over screen
- In-game HUD
- Fullscreen support

---

## 💡 ADVANCED TIPS

### Pro Strategies
1. **Pattern Play** - Create snake loops for efficient food catching
2. **Space Management** - Keep room to maneuver
3. **Anticipation** - Plan moves ahead of time
4. **Speed Adaptation** - Adjust to increasing speed gradually

### Settings for Different Preferences

**For Beginners:**
```python
INITIAL_SPEED = 5
MAX_SPEED = 15
```

**For Experienced Players:**
```python
INITIAL_SPEED = 15
MAX_SPEED = 30
```

**Large Screen:**
```python
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000
```

---

## 🐛 DEBUGGING

### Check if Game Works
```bash
python test.py
```

Expected output:
```
Testing Snake Game Code...
✓ All checks passed!
```

### Run with Debug Info
Edit `main.py` and add after imports:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📚 DOCUMENTATION MAP

| Document | Purpose |
|----------|---------|
| **README.md** | Complete feature guide |
| **QUICKSTART.md** | 5-minute getting started |
| **INSTALLATION_GUIDE.md** | Detailed setup help |
| **ASSETS_GUIDE.md** | Add sounds and fonts |
| **FEATURES.md** | Feature checklist |
| **main.py** | The actual game code |

---

## 🎮 KEYBOARD SHORTCUTS SUMMARY

```
Game Controls:
  Arrow Keys / WASD - Move snake
  P                 - Pause/Resume
  ESC               - Return to menu
  F11               - Fullscreen toggle

Menu:
  Mouse Click       - Select option
  Enter             - Start game (menu)
```

---

## 📊 GAME STATISTICS

- **Game Size:** ~700 lines of clean Python code
- **Classes:** 9 well-organized classes
- **Difficulty Levels:** 15 progressive levels
- **Color Scheme:** Modern neon style
- **Performance:** 60 FPS capable
- **Customizable:** Yes (see customization section)

---

## 🎯 NEXT STEPS

1. **Run the game:** `python main.py`
2. **Play and have fun!**
3. **Check ASSETS_GUIDE.md** to add custom sounds
4. **Edit main.py** to customize difficulty/colors
5. **Challenge friends** for high scores!

---

## 🤝 SUPPORT

### Common Questions

**Q: How do I make the game easier?**
A: Change `INITIAL_SPEED = 10` to `INITIAL_SPEED = 5` in main.py

**Q: Can I play fullscreen?**
A: Yes! Press F11 while playing

**Q: Where is my high score saved?**
A: In `highscore.txt` in the game folder

**Q: Can I add my own sounds?**
A: Yes! See ASSETS_GUIDE.md for instructions

**Q: Is there multiplayer?**
A: No, but you can take turns and compete for high scores!

---

## ✅ WHAT'S INCLUDED

- ✓ Complete working game
- ✓ Clean, commented code
- ✓ Professional UI
- ✓ Score/high score system
- ✓ Difficulty progression
- ✓ Particle effects
- ✓ 4 documentation files
- ✓ Setup scripts
- ✓ No external dependencies beyond Pygame

---

## 🎉 YOU'RE ALL SET!

Everything is ready. Just run:

```bash
python main.py
```

And enjoy playing! 🐍

---

**Have fun and beat that high score!** 🏆

For more information, see README.md or other documentation files.
