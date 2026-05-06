# 🐍 Modern Snake Game

A feature-rich, modern Snake game built with Python and Pygame featuring beautiful neon UI, particle effects, sound system, and multiple difficulty levels.

## 🎮 Game Features

### Core Gameplay
- **Snake Movement**: Control with Arrow Keys or WASD
- **Growing Mechanic**: Snake grows when eating food
- **Collision Detection**: Prevents moving through walls or itself
- **Smooth Movement**: Fast, responsive controls
- **Pause Feature**: Press `P` to pause/resume

### Advanced Features
- **Main Menu** with animated buttons
- **Difficulty Levels**: 15 levels that automatically increase as you score
- **Score System**: Real-time score display
- **High Score Saving**: Persistent high score tracking
- **Particle Effects**: Visual feedback when eating food
- **Animated Snake Eyes**: Snake head shows animation
- **Neon Visual Style**: Modern, attractive UI design
- **Grid Background**: Clean, professional look
- **Game Over Screen**: Shows final score and high score
- **Fullscreen Support**: Press `F11` to toggle fullscreen

## 📋 Requirements

- Python 3.7+
- Pygame 2.0+

## ⚙️ Installation

### Step 1: Install Python
Make sure you have Python 3.7 or higher installed:
```bash
python --version
```

### Step 2: Install Pygame
Install Pygame using pip:
```bash
pip install pygame
```

Or if you're using Python 3:
```bash
pip3 install pygame
```

### Step 3: Verify Installation
Test if Pygame is installed correctly:
```bash
python -c "import pygame; print('Pygame installed successfully!')"
```

## 🚀 How to Run

### Simple Method
1. Navigate to the `snake_game` folder
2. Double-click `main.py` (on Windows)
3. Or run from terminal:
```bash
python main.py
```

### From Command Line
```bash
cd path/to/snake_game
python main.py
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| **Arrow Keys** | Move snake (Up/Down/Left/Right) |
| **WASD** | Alternative movement controls |
| **P** | Pause/Resume game |
| **ESC** | Return to main menu |
| **F11** | Toggle fullscreen mode |
| **Click** | Select menu options |

## 📊 Game Mechanics

### Scoring
- **Base Points**: 10 points per food eaten
- **Progression**:
  - Level 1: Speed 10
  - Level 2: Speed 12 (50 points)
  - Level 3: Speed 14 (100 points)
  - ... continues up to Level 15

### Difficulty
- Game speed increases every 5 points
- Maximum speed capped at 25 FPS
- Snake moves faster with each level

### Collisions
- **Wall Collision**: End of game if snake hits screen edge
- **Self Collision**: End of game if snake hits itself
- **Food Detection**: Automatic when snake head touches food

## 📁 Project Structure

```
snake_game/
├── main.py                          # Main game file (all-in-one)
├── highscore.txt                    # High score storage (auto-created)
├── README.md                        # This file
├── assets/
│   ├── sounds/                      # Sound effects (optional)
│   │   ├── eat.wav                  # Eating sound
│   │   ├── gameover.wav             # Game over sound
│   │   └── click.wav                # Button click sound
│   ├── images/                      # Image assets (optional)
│   └── fonts/                       # Custom fonts (optional)
└── INSTALLATION_GUIDE.md            # Detailed setup guide
```

## 🔊 Adding Custom Sounds

The game looks for sound files in the `assets/sounds/` directory:

### Supported Formats
- WAV files (.wav)
- MP3 files (.mp3)
- OGG files (.ogg)

### How to Add Sounds
1. Create sound files or download them
2. Place them in the appropriate folder:
   - `assets/sounds/eat.wav` - Sound when eating food
   - `assets/sounds/gameover.wav` - Sound when game ends
   - `assets/sounds/click.wav` - Sound for button clicks

3. Restart the game

**Note**: If sound files are not found, the game will run without sound (graceful degradation).

## 🎨 Adding Custom Fonts

1. Place TTF font files in `assets/fonts/`
2. Add a file named `font.ttf` to override the default font
3. Restart the game

Recommended free fonts:
- Press Start 2P (retro look)
- Orbitron (sci-fi look)
- Roboto Mono (modern look)

Download from: https://fonts.google.com/

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'pygame'"
**Solution**: Install Pygame
```bash
pip install pygame
```

### "No module named 'pygame'" in IDE
**Solution**: Make sure you're using the correct Python environment:
```bash
# Check which Python is being used
python -m pip list | grep pygame

# Install in current environment
python -m pip install pygame
```

### Game runs but no sound
**Info**: This is normal if sound files aren't in the `assets/sounds/` folder. The game continues without sound.

### Game is too fast/slow
**Note**: Game speed scales based on your level. Starting speed should be manageable.

### Game crashes on startup
**Solution**: 
1. Make sure Pygame is installed: `pip install pygame`
2. Make sure Python version is 3.7+
3. Check that main.py is in the snake_game folder

## 📈 Tips and Tricks

### Getting High Scores
1. **Focus on growth early**: Eat consistently to build length and score multipliers
2. **Plan your moves**: Anticipate the snake's movement a couple steps ahead
3. **Use the edges**: Create patterns that efficiently cover the playing area
4. **Stay calm**: The game gets faster gradually, so you have time to adapt

### Game Rules
- You can't move directly backwards (e.g., from right to left instantly)
- The snake must have room to turn (collision detection is exact)
- Food always spawns where the snake isn't occupying
- Speed increases every time you reach a new level (50 points)

## 🔧 Advanced Configuration

Edit the top of `main.py` to customize:

```python
SCREEN_WIDTH = 1000          # Game window width
SCREEN_HEIGHT = 700          # Game window height
GRID_SIZE = 20               # Size of each grid cell
INITIAL_SPEED = 10           # Starting game speed (FPS)
MAX_SPEED = 25               # Maximum game speed
DIFFICULTY_INCREASE_INTERVAL = 5  # Points between level increases
```

### Color Customization
All colors are defined at the top of `main.py`:
```python
COLOR_GREEN = (0, 255, 100)
COLOR_NEON_BLUE = (0, 150, 255)
# ... modify these RGB values
```

## 📝 Code Structure

The game is organized into well-commented sections:

- **Constants**: All game settings in one place
- **Enums**: Direction and GameState enums
- **SoundManager**: Handles audio
- **ParticleSystem**: Manages visual effects
- **Snake Class**: Snake logic and rendering
- **Food Class**: Food spawning and animation
- **Game Class**: Main game loop and state management

## 🎓 Learning Points

This game demonstrates:
- Object-oriented programming with Python
- Pygame graphics and event handling
- Game state management
- Collision detection
- File I/O (saving scores)
- Animation techniques
- UI/UX design principles
- Event-driven programming

## 📄 License

This game is provided as-is for educational purposes.

## 🤝 Contributing

Feel free to:
- Add new features
- Improve the UI
- Add more sound effects
- Create better art
- Optimize the code

## 📧 Support

If you encounter any issues:
1. Check the Troubleshooting section above
2. Verify Pygame is installed correctly
3. Make sure all files are in the correct locations
4. Check that Python version is 3.7+

## 🎉 Enjoy!

Have fun playing and modifying the game! This is a great starting point for learning game development with Python.

---

**Made with ❤️ using Python & Pygame**
