#!/usr/bin/env python
"""Quick test to verify the game code is valid"""

import sys
import os

# Add the snake_game directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Testing Snake Game Code...")
print("-" * 40)

try:
    print("✓ Importing pygame...", end=" ")
    import pygame
    pygame.init()
    print("OK")
    
    print("✓ Importing main module...", end=" ")
    with open(os.path.join(os.path.dirname(__file__), 'main.py'), 'r') as f:
        code = f.read()
    
    # Check for basic syntax
    compile(code, 'main.py', 'exec')
    print("OK")
    
    print("✓ Checking key classes...", end=" ")
    # Check for new classes
    assert 'class Button:' in code, "Button class not found"
    assert 'class Particle:' in code, "Particle class not found"
    assert 'class ParticleSystem:' in code, "ParticleSystem class not found"
    assert 'class Snake:' in code, "Snake class not found"
    assert 'class Food:' in code, "Food class not found"
    assert 'class Game:' in code, "Game class not found"
    print("OK")
    
    print("\n" + "=" * 40)
    print("✓ All checks passed!")
    print("=" * 40)
    print("\nYou can now run the game:")
    print("    python main.py")
    print("\n")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("Please check main.py for issues")
    sys.exit(1)

