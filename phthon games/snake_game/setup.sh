#!/bin/bash
# Modern Snake Game - Setup Script for Mac/Linux

echo "============================================"
echo "Modern Snake Game - Setup"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

echo "Installing Pygame..."
pip3 install pygame

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install Pygame"
    echo "Try: sudo pip3 install pygame"
    exit 1
fi

echo ""
echo "✓ Setup complete!"
echo ""
echo "You can now run the game by typing:"
echo "    python3 main.py"
echo ""
