# Snake Game

A modern Snake Game built with **Python** and **Pygame**.

## Features

- Smooth snake movement and growth
- Score and persistent high-score tracking
- Collision-based game over (wall and self)
- Pause menu and game over screen
- Fullscreen toggle support

## Requirements

- Python 3.7+
- `pygame` 2.x

## Project Structure

```text
Snake-game/
├── README.md
└── phthon games/
    └── snake_game/
        ├── main.py
        ├── test.py
        ├── highscore.txt
        ├── setup.sh
        ├── setup.bat
        └── docs/
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/PrashantRanjan-2006/Snake-game.git
   cd Snake-game
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install pygame
   ```

## Run the Game

```bash
cd "phthon games/snake_game"
python main.py
```

## Controls

- **Arrow Keys / WASD**: Move snake
- **P**: Pause/Resume
- **ESC**: Back to menu
- **F11**: Toggle fullscreen
- **Close Window**: Quit

## Verify Installation

```bash
cd "phthon games/snake_game"
python test.py
```

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

This project is currently provided as-is.
