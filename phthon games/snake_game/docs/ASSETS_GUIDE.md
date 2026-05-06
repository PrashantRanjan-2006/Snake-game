# Assets Guide - Snake Game

This guide explains how to add custom sounds and images to the game.

## 📁 Asset Structure

```
assets/
├── sounds/
│   ├── eat.wav
│   ├── gameover.wav
│   └── click.wav
├── images/
│   └── (reserved for future use)
└── fonts/
    └── font.ttf
```

## 🔊 Adding Sound Effects

The game looks for WAV files in the `assets/sounds/` directory. The game gracefully handles missing sounds by skipping them.

### Required Sound Files

1. **eat.wav** - Plays when the snake eats food
   - Suggested: Short beep or chime (0.5-1 second)
   - Format: WAV or MP3
   - Suggested: 44100 Hz mono or 22050 Hz

2. **gameover.wav** - Plays when the game ends
   - Suggested: Sad/game over sound (1-2 seconds)
   - Format: WAV or MP3

3. **click.wav** - Plays when clicking buttons
   - Suggested: Soft click sound (0.2-0.5 seconds)
   - Format: WAV or MP3

### Where to Find Sound Effects

**Free Sound Libraries:**
- https://freesound.org - Largest free sound library
- https://www.zapsplat.com - Free game sounds
- https://www.soundly.com - Sound effects
- https://www.bfxr.net - Retro pixel game sounds (online generator)
- https://www.as3sfxr.com - Generate 8-bit sounds

### How to Use Downloaded Sounds

1. Download or create a sound file
2. Save as WAV format (recommended) or MP3
3. Rename according to the list above:
   - Eating sound → `eat.wav`
   - Game over → `gameover.wav`
   - Click sound → `click.wav`
4. Place in `assets/sounds/` folder
5. Run the game - it will automatically load them

### Creating Sounds Yourself

**Online Tools (No Installation):**
- https://www.bfxr.net - Press "export" to download WAV files
- https://www.as3sfxr.com - Similar tool for retro sounds

**Using Your Phone:**
- Record yourself making sounds
- Edit on your phone using free apps
- Export as WAV/MP3
- Place in assets/sounds/ folder

### Code to Generate Simple Sounds (Optional)

Add this to `main.py` to generate simple sounds without files:

```python
def generate_simple_sound(frequency=440, duration=0.2):
    """Generate a simple sine wave sound"""
    import numpy as np
    sample_rate = 44100
    samples = int(duration * sample_rate)
    t = np.linspace(0, duration, samples)
    wave = np.sin(2 * np.pi * frequency * t) * 0.3
    audio = ((wave + 0.5) * 255).astype(np.uint8)
    stereo = np.zeros((samples, 2), dtype=np.uint8)
    stereo[:, 0] = audio
    stereo[:, 1] = audio
    sound = pygame.sndarray.make_sound(stereo)
    return sound
```

## 🎨 Custom Fonts

### Adding a Custom Font

1. Find a font you like:
   - https://fonts.google.com (free, needs download)
   - https://www.dafont.com (free, various styles)
   - System fonts on your computer

2. Download the TTF file

3. Place in `assets/fonts/` folder

4. Rename to `font.ttf` (or edit the paths in `main.py`)

5. Run the game

### Recommended Fonts for Games

**Retro Style:**
- Press Start 2P (Google Fonts)
- Pixel Operator (DaFont)
- Pixels (DaFont)

**Modern Style:**
- Roboto Mono (Google Fonts)
- JetBrains Mono (Google Fonts)
- Inconsolata (Google Fonts)

**Futuristic:**
- Orbitron (Google Fonts)
- Audiowide (Google Fonts)
- Electrolize (Google Fonts)

## 🎵 Adding Background Music

The current game doesn't have background music, but you can add it:

1. Find an 8-bit/retro music file
2. Save as `assets/sounds/background.wav` or `.ogg`
3. Add to `SoundManager.load_sounds()`:

```python
def load_sounds(self):
    # ... existing code ...
    self.background_music = None
    if os.path.exists('assets/sounds/background.wav'):
        self.background_music = pygame.mixer.Sound('assets/sounds/background.wav')
```

4. In `Game.__init__()`:

```python
# Start background music
if self.sound.background_music:
    self.sound.background_music.play(-1)  # -1 loops forever
```

**Where to Find Background Music:**
- https://www.zapsplat.com (free game music)
- https://www.opengameart.org (free game assets)
- https://www.incompetech.com (free royalty-free music)

## 📝 Troubleshooting

### Sound file not playing
- Make sure it's in `assets/sounds/` folder
- Check filename matches exactly: `eat.wav`, `gameover.wav`, `click.wav`
- Try converting to WAV format if using MP3
- Verify file isn't corrupted

### Font not loading
- Place TTF file in `assets/fonts/`
- Rename to exactly `font.ttf`
- Make sure it's a valid TTF format
- Game will fall back to default if missing

### File Not Found errors
- Create the folders if they don't exist:
  - `assets/sounds/`
  - `assets/images/`
  - `assets/fonts/`
- Use the exact folder names (lowercase)

## 🎯 Quick Start

1. Download a sound from freesound.org
2. Convert to WAV if needed (online converter)
3. Copy to `assets/sounds/` and rename appropriately
4. Run the game!

The game will work perfectly without custom assets - it's just a bonus to enhance the experience.

## 📄 Asset Credits

If you use assets from others, consider:
- Giving credit where required
- Following the license restrictions
- Adding a credits.txt file to your project

---

**That's it! Enjoy customizing your game!** 🎮
