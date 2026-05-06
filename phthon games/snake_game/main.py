# -*- coding: utf-8 -*-
"""
Modern Snake Game - UI/UX Enhanced Edition
Professional arcade game with modern aesthetics, smooth animations, and polished UI.
"""

import pygame
import random
import math
import os
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod

# ==================== INITIALIZATION ====================
pygame.init()

# ==================== CONSTANTS ====================
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors - Modern Neon Palette
class Colors:
    BLACK = (10, 10, 20)
    DARK_BG = (15, 15, 35)
    DARK_PANEL = (25, 25, 60)
    GRID_COLOR = (40, 40, 80)
    
    # Neon Colors
    NEON_GREEN = (0, 255, 150)
    NEON_CYAN = (0, 200, 255)
    NEON_PINK = (255, 0, 127)
    NEON_PURPLE = (150, 50, 255)
    NEON_YELLOW = (255, 255, 0)
    NEON_BLUE = (50, 150, 255)
    
    # UI Colors
    TEXT_PRIMARY = (255, 255, 255)
    TEXT_SECONDARY = (150, 150, 200)
    ACCENT = NEON_CYAN
    SUCCESS = NEON_GREEN
    WARNING = NEON_PINK
    
    # Gradients
    GRADIENT_START = (20, 10, 40)
    GRADIENT_END = (10, 30, 50)


# ==================== ENUMS ====================
class GameState(Enum):
    MENU = 1
    SETTINGS = 2
    PLAYING = 3
    PAUSED = 4
    GAME_OVER = 5
    LOADING = 6


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


# ==================== DATA CLASSES ====================
@dataclass
class Vector2:
    x: float
    y: float
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        if isinstance(other, Vector2):
            return abs(self.x - other.x) < 0.01 and abs(self.y - other.y) < 0.01
        return False


# ==================== UI COMPONENTS ====================
class Button:
    """Modern button with animations and hover effects"""
    
    def __init__(self, x: float, y: float, width: float, height: float, 
                 text: str, primary_color: Tuple = Colors.NEON_CYAN, 
                 secondary_color: Tuple = Colors.NEON_GREEN):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.is_hovered = False
        self.scale = 1.0
        self.glow_intensity = 0
        self.rect = pygame.Rect(x - width/2, y - height/2, width, height)
    
    def update(self, mouse_pos: Tuple[int, int], delta_time: float):
        """Update button state"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        target_scale = 1.05 if self.is_hovered else 1.0
        self.scale += (target_scale - self.scale) * 0.1
        self.glow_intensity += (1.0 if self.is_hovered else -0.5) * delta_time
        self.glow_intensity = max(0, min(1, self.glow_intensity))
        scaled_width = self.width * self.scale
        scaled_height = self.height * self.scale
        self.rect = pygame.Rect(self.x - scaled_width/2, self.y - scaled_height/2, 
                               scaled_width, scaled_height)
    
    def draw(self, surface: pygame.Surface, font: pygame.font.Font):
        """Draw button with glow effect"""
        if self.glow_intensity > 0:
            glow_color = tuple(int(c * self.glow_intensity) for c in self.primary_color)
            pygame.draw.rect(surface, glow_color, self.rect.inflate(10, 10), 2)
        pygame.draw.rect(surface, self.primary_color, self.rect, 2)
        pygame.draw.rect(surface, self.secondary_color if self.is_hovered else self.primary_color, 
                        self.rect, 0)
        text_surface = font.render(self.text, True, Colors.BLACK if self.is_hovered else Colors.TEXT_PRIMARY)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def is_clicked(self, event: pygame.event.EventType) -> bool:
        """Check if button is clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False


class Slider:
    """Modern slider for settings"""
    
    def __init__(self, x: float, y: float, width: float, min_val: float, 
                 max_val: float, default: float = None):
        self.x = x
        self.y = y
        self.width = width
        self.min = min_val
        self.max = max_val
        self.value = default if default else min_val
        self.dragging = False
        self.height = 8
    
    def update(self, mouse_pos: Tuple[int, int], mouse_pressed: bool):
        """Update slider"""
        handle_x = self.x + (self.value - self.min) / (self.max - self.min) * self.width
        handle_rect = pygame.Rect(handle_x - 10, self.y - 10, 20, 20)
        if mouse_pressed:
            if handle_rect.collidepoint(mouse_pos) or self.dragging:
                self.dragging = True
                self.value = self.min + (mouse_pos[0] - self.x) / self.width * (self.max - self.min)
                self.value = max(self.min, min(self.max, self.value))
        else:
            self.dragging = False
    
    def draw(self, surface: pygame.Surface):
        """Draw slider"""
        pygame.draw.line(surface, Colors.GRID_COLOR, (self.x, self.y), 
                        (self.x + self.width, self.y), self.height)
        progress_width = (self.value - self.min) / (self.max - self.min) * self.width
        pygame.draw.line(surface, Colors.NEON_CYAN, (self.x, self.y), 
                        (self.x + progress_width, self.y), self.height)
        handle_x = self.x + (self.value - self.min) / (self.max - self.min) * self.width
        pygame.draw.circle(surface, Colors.NEON_CYAN, (int(handle_x), int(self.y)), 10)
        pygame.draw.circle(surface, Colors.NEON_GREEN if self.dragging else Colors.TEXT_PRIMARY, 
                          (int(handle_x), int(self.y)), 8)


class Particle:
    """Visual particle effect"""
    
    def __init__(self, x: float, y: float, vx: float, vy: float, 
                 color: Tuple, lifetime: float, size: float = 5):
        self.pos = Vector2(x, y)
        self.vel = Vector2(vx, vy)
        self.color = color
        self.lifetime = lifetime
        self.age = 0
        self.size = size
        self.gravity = 50
    
    def update(self, delta_time: float):
        """Update particle"""
        self.pos += self.vel * delta_time
        self.vel.y += self.gravity * delta_time
        self.age += delta_time
        self.size = max(0.1, self.size * 0.98)
    
    def draw(self, surface: pygame.Surface):
        """Draw particle"""
        alpha = max(0, 1 - self.age / self.lifetime)
        color = tuple(int(c * alpha) for c in self.color)
        pygame.draw.circle(surface, color, (int(self.pos.x), int(self.pos.y)), int(self.size))
    
    def is_alive(self) -> bool:
        """Check if particle is alive"""
        return self.age < self.lifetime


class ParticleSystem:
    """Manages particle effects"""
    
    def __init__(self):
        self.particles: List[Particle] = []
    
    def emit(self, x: float, y: float, count: int = 20, color: Tuple = Colors.NEON_YELLOW,
             velocity_range: float = 200):
        """Emit particles"""
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0, velocity_range)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            particle = Particle(x, y, vx, vy, color, 0.8, random.uniform(3, 8))
            self.particles.append(particle)
    
    def update(self, delta_time: float):
        """Update all particles"""
        for particle in self.particles[:]:
            particle.update(delta_time)
            if not particle.is_alive():
                self.particles.remove(particle)
    
    def draw(self, surface: pygame.Surface):
        """Draw all particles"""
        for particle in self.particles:
            particle.draw(surface)


class AnimationManager:
    """Manages smooth animations"""
    
    def __init__(self):
        self.animations = {}
    
    def add(self, name: str, start: float, end: float, duration: float):
        """Add animation"""
        self.animations[name] = {
            'start': start,
            'end': end,
            'duration': duration,
            'elapsed': 0,
            'finished': False
        }
    
    def update(self, delta_time: float):
        """Update all animations"""
        for anim in self.animations.values():
            if not anim['finished']:
                anim['elapsed'] += delta_time
                if anim['elapsed'] >= anim['duration']:
                    anim['finished'] = True
                    anim['elapsed'] = anim['duration']
    
    def get_value(self, name: str) -> float:
        """Get current animation value"""
        if name not in self.animations:
            return 0
        anim = self.animations[name]
        progress = min(1, anim['elapsed'] / anim['duration'])
        progress = 1 - (1 - progress) ** 3
        return anim['start'] + (anim['end'] - anim['start']) * progress
    
    def is_finished(self, name: str) -> bool:
        """Check if animation finished"""
        return self.animations.get(name, {}).get('finished', True)


# ==================== GAME OBJECTS ====================
class Snake:
    """Snake with modern visuals"""
    
    GRID_SIZE = 20
    
    def __init__(self):
        self.body = [(10, 10), (9, 10), (8, 10)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.growing = False
    
    def update(self):
        """Update snake"""
        if self.next_direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif self.next_direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif self.next_direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif self.next_direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
    
    def set_direction(self, direction: Direction):
        """Set next direction"""
        self.next_direction = direction
    
    def grow(self):
        """Grow snake"""
        self.growing = True
    
    def check_collision_wall(self) -> bool:
        """Check wall collision"""
        x, y = self.body[0]
        return x < 0 or x >= 40 or y < 0 or y >= 30
    
    def check_collision_self(self) -> bool:
        """Check self collision"""
        return self.body[0] in self.body[1:]
    
    def draw(self, surface: pygame.Surface):
        """Draw snake with smooth segments"""
        for i, (x, y) in enumerate(self.body):
            screen_x = 150 + x * self.GRID_SIZE + 5
            screen_y = 100 + y * self.GRID_SIZE + 5
            
            if i == 0:  # Head
                pygame.draw.circle(surface, Colors.NEON_GREEN, (screen_x + 5, screen_y + 5), 12)
                pygame.draw.circle(surface, Colors.NEON_CYAN, (screen_x + 5, screen_y + 5), 10)
                pygame.draw.rect(surface, Colors.NEON_GREEN, 
                               (screen_x, screen_y, self.GRID_SIZE - 2, self.GRID_SIZE - 2))
                self._draw_eyes(surface, screen_x, screen_y)
            else:
                brightness = max(50, 200 - i * 10)
                color = (0, brightness, 100)
                pygame.draw.rect(surface, color, 
                               (screen_x + 1, screen_y + 1, self.GRID_SIZE - 4, self.GRID_SIZE - 4))
                pygame.draw.circle(surface, color, (screen_x + 2, screen_y + 2), 2)
    
    def _draw_eyes(self, surface: pygame.Surface, x: int, y: int):
        """Draw animated eyes"""
        eye_size = 2
        direction = self.direction
        positions = {
            Direction.UP: [(x + 5, y + 5), (x + 13, y + 5)],
            Direction.DOWN: [(x + 5, y + 13), (x + 13, y + 13)],
            Direction.LEFT: [(x + 5, y + 8), (x + 5, y + 12)],
            Direction.RIGHT: [(x + 13, y + 8), (x + 13, y + 12)]
        }
        for pos in positions.get(direction, positions[Direction.RIGHT]):
            pygame.draw.circle(surface, (255, 255, 255), pos, eye_size)
            pygame.draw.circle(surface, (0, 0, 0), pos, 1)


class Food:
    """Food with visual effects"""
    
    GRID_SIZE = 20
    
    def __init__(self, snake: Snake):
        self.pos = None
        self.snake = snake
        self.animation_time = 0
        self.color = Colors.NEON_YELLOW
        self.spawn()
    
    def spawn(self):
        """Spawn food"""
        while True:
            x = random.randint(0, 39)
            y = random.randint(0, 29)
            if (x, y) not in self.snake.body:
                self.pos = (x, y)
                self.color = random.choice([
                    Colors.NEON_YELLOW,
                    Colors.NEON_CYAN,
                    Colors.NEON_PINK
                ])
                self.animation_time = 0
                break
    
    def update(self, delta_time: float):
        """Update animation"""
        self.animation_time += delta_time
    
    def draw(self, surface: pygame.Surface):
        """Draw food with bounce animation"""
        if not self.pos:
            return
        
        x = 150 + self.pos[0] * self.GRID_SIZE + 5
        y = 100 + self.pos[1] * self.GRID_SIZE + 5
        
        bounce = math.sin(self.animation_time * 3) * 2
        y += bounce
        
        glow_size = 12 + math.sin(self.animation_time * 2) * 2
        pygame.draw.circle(surface, self.color, (x + 5, y + 5), int(glow_size))
        pygame.draw.rect(surface, self.color, (x, int(y), self.GRID_SIZE - 2, self.GRID_SIZE - 2))
        pygame.draw.rect(surface, (255, 255, 255), (x, int(y), self.GRID_SIZE - 2, self.GRID_SIZE - 2), 2)


# ==================== GAME CLASS ====================
class Game:
    """Main game"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
        pygame.display.set_caption("Modern Snake Game - Professional Edition")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU
        
        self.setup_fonts()
        
        self.snake = Snake()
        self.food = Food(self.snake)
        self.particles = ParticleSystem()
        self.animations = AnimationManager()
        
        self.score = 0
        self.high_score = self.load_high_score()
        self.level = 1
        self.game_speed = 5
        self.speed_timer = 0
        self.food_eaten = 0
        
        self.setup_ui()
    
    def setup_fonts(self):
        """Setup fonts"""
        try:
            self.font_title = pygame.font.Font("assets/fonts/font.ttf", 72)
            self.font_large = pygame.font.Font("assets/fonts/font.ttf", 48)
            self.font_medium = pygame.font.Font("assets/fonts/font.ttf", 32)
            self.font_small = pygame.font.Font("assets/fonts/font.ttf", 20)
        except:
            self.font_title = pygame.font.Font(None, 72)
            self.font_large = pygame.font.Font(None, 48)
            self.font_medium = pygame.font.Font(None, 32)
            self.font_small = pygame.font.Font(None, 20)
    
    def setup_ui(self):
        """Setup UI buttons"""
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        
        self.btn_play = Button(center_x, center_y - 100, 200, 60, "PLAY GAME", 
                              Colors.NEON_GREEN, Colors.NEON_CYAN)
        self.btn_settings = Button(center_x, center_y, 200, 60, "SETTINGS", 
                                  Colors.NEON_CYAN, Colors.NEON_GREEN)
        self.btn_quit = Button(center_x, center_y + 100, 200, 60, "QUIT", 
                              Colors.NEON_PINK, Colors.NEON_YELLOW)
        
        self.btn_resume = Button(center_x - 150, center_y, 150, 50, "RESUME", 
                                Colors.NEON_GREEN, Colors.NEON_CYAN)
        self.btn_menu = Button(center_x + 150, center_y, 150, 50, "MENU", 
                              Colors.NEON_CYAN, Colors.NEON_PINK)
        
        self.btn_restart = Button(center_x, center_y + 100, 200, 60, "RESTART", 
                                 Colors.NEON_GREEN, Colors.NEON_CYAN)
        self.btn_main_menu = Button(center_x, center_y + 180, 200, 60, "MAIN MENU", 
                                   Colors.NEON_BLUE, Colors.NEON_CYAN)
        
        self.slider_music = Slider(center_x - 100, center_y - 50, 200, 0, 100, 70)
        self.slider_sfx = Slider(center_x - 100, center_y + 50, 200, 0, 100, 80)
    
    def load_high_score(self) -> int:
        """Load high score"""
        try:
            if os.path.exists('highscore.txt'):
                with open('highscore.txt', 'r') as f:
                    return int(f.read().strip())
        except:
            pass
        return 0
    
    def save_high_score(self):
        """Save high score"""
        try:
            with open('highscore.txt', 'w') as f:
                f.write(str(self.high_score))
        except:
            pass
    
    def handle_events(self):
        """Handle input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.MENU
                    elif self.state == GameState.SETTINGS:
                        self.state = GameState.MENU
                
                if event.key == pygame.K_p and self.state == GameState.PLAYING:
                    self.state = GameState.PAUSED
                
                if self.state == GameState.PLAYING:
                    if event.key in [pygame.K_UP, pygame.K_w]:
                        self.snake.set_direction(Direction.UP)
                    elif event.key in [pygame.K_DOWN, pygame.K_s]:
                        self.snake.set_direction(Direction.DOWN)
                    elif event.key in [pygame.K_LEFT, pygame.K_a]:
                        self.snake.set_direction(Direction.LEFT)
                    elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                        self.snake.set_direction(Direction.RIGHT)
            
            if self.state == GameState.MENU:
                if self.btn_play.is_clicked(event):
                    self.start_game()
                elif self.btn_settings.is_clicked(event):
                    self.state = GameState.SETTINGS
                elif self.btn_quit.is_clicked(event):
                    self.running = False
            elif self.state == GameState.PAUSED:
                if self.btn_resume.is_clicked(event):
                    self.state = GameState.PLAYING
                elif self.btn_menu.is_clicked(event):
                    self.state = GameState.MENU
            elif self.state == GameState.GAME_OVER:
                if self.btn_restart.is_clicked(event):
                    self.start_game()
                elif self.btn_main_menu.is_clicked(event):
                    self.state = GameState.MENU
    
    def start_game(self):
        """Start game"""
        self.snake = Snake()
        self.food = Food(self.snake)
        self.score = 0
        self.level = 1
        self.game_speed = 5
        self.speed_timer = 0
        self.food_eaten = 0
        self.state = GameState.PLAYING
    
    def update(self, delta_time: float):
        """Update game"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        for btn in [self.btn_play, self.btn_settings, self.btn_quit, 
                   self.btn_resume, self.btn_menu, self.btn_restart, 
                   self.btn_main_menu]:
            btn.update(mouse_pos, delta_time)
        
        if self.state == GameState.SETTINGS:
            self.slider_music.update(mouse_pos, mouse_pressed)
            self.slider_sfx.update(mouse_pos, mouse_pressed)
        
        self.animations.update(delta_time)
        self.particles.update(delta_time)
        
        if self.state == GameState.PLAYING:
            self.speed_timer += delta_time
            if self.speed_timer >= 1.0 / self.game_speed:
                self.speed_timer = 0
                
                self.snake.update()
                self.food.update(delta_time)
                
                if self.snake.check_collision_wall() or self.snake.check_collision_self():
                    self.state = GameState.GAME_OVER
                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.save_high_score()
                
                if self.snake.body[0] == self.food.pos:
                    self.score += 10
                    self.food_eaten += 1
                    self.snake.grow()
                    self.food.spawn()
                    self.particles.emit(
                        150 + self.food.pos[0] * 20 + 15,
                        100 + self.food.pos[1] * 20 + 15,
                        30, self.food.color
                    )
                    
                    if self.food_eaten % 5 == 0:
                        self.level += 1
                        self.game_speed = min(10, 5 + self.level * 0.5)
        
        self.food.update(delta_time)
    
    def draw(self):
        """Draw game"""
        self.screen.fill(Colors.DARK_BG)
        self.draw_background()
        
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.SETTINGS:
            self.draw_settings()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_pause_screen()
        elif self.state == GameState.GAME_OVER:
            self.draw_game()
            self.draw_game_over_screen()
        
        pygame.display.flip()
    
    def draw_background(self):
        """Draw animated background"""
        for y in range(SCREEN_HEIGHT):
            progress = y / SCREEN_HEIGHT
            color = tuple(
                int(Colors.GRADIENT_START[i] + (Colors.GRADIENT_END[i] - Colors.GRADIENT_START[i]) * progress)
                for i in range(3)
            )
            pygame.draw.line(self.screen, color, (0, y), (SCREEN_WIDTH, y))
        
        for x in range(0, SCREEN_WIDTH, 50):
            pygame.draw.line(self.screen, Colors.GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, 50):
            pygame.draw.line(self.screen, Colors.GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 1)
    
    def draw_menu(self):
        """Draw main menu"""
        title = self.font_title.render("SNAKE GAME", True, Colors.NEON_GREEN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        subtitle = self.font_medium.render("Modern Pro Edition", True, Colors.NEON_CYAN)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 180))
        self.screen.blit(subtitle, subtitle_rect)
        
        self.btn_play.draw(self.screen, self.font_medium)
        self.btn_settings.draw(self.screen, self.font_medium)
        self.btn_quit.draw(self.screen, self.font_medium)
        
        hs_text = self.font_small.render(f"High Score: {self.high_score}", True, Colors.NEON_YELLOW)
        hs_rect = hs_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.screen.blit(hs_text, hs_rect)
    
    def draw_settings(self):
        """Draw settings menu"""
        title = self.font_large.render("SETTINGS", True, Colors.NEON_CYAN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        music_label = self.font_medium.render("Music Volume", True, Colors.TEXT_PRIMARY)
        self.screen.blit(music_label, (SCREEN_WIDTH // 2 - 200, 250))
        self.slider_music.draw(self.screen)
        
        sfx_label = self.font_medium.render("SFX Volume", True, Colors.TEXT_PRIMARY)
        self.screen.blit(sfx_label, (SCREEN_WIDTH // 2 - 200, 350))
        self.slider_sfx.draw(self.screen)
        
        inst = self.font_small.render("Press ESC to return", True, Colors.TEXT_SECONDARY)
        inst_rect = inst.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.screen.blit(inst, inst_rect)
    
    def draw_game(self):
        """Draw gameplay"""
        game_area = pygame.Rect(150, 100, 800, 600)
        pygame.draw.rect(self.screen, Colors.DARK_PANEL, game_area)
        pygame.draw.rect(self.screen, Colors.NEON_CYAN, game_area, 3)
        
        for x in range(0, 800, 20):
            pygame.draw.line(self.screen, Colors.GRID_COLOR, (150 + x, 100), (150 + x, 700), 1)
        for y in range(0, 600, 20):
            pygame.draw.line(self.screen, Colors.GRID_COLOR, (150, 100 + y), (950, 100 + y), 1)
        
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.particles.draw(self.screen)
        
        score_text = self.font_medium.render(f"Score: {self.score}", True, Colors.NEON_GREEN)
        self.screen.blit(score_text, (50, 150))
        
        level_text = self.font_medium.render(f"Level: {self.level}", True, Colors.NEON_CYAN)
        self.screen.blit(level_text, (50, 250))
        
        hs_text = self.font_medium.render(f"High: {self.high_score}", True, Colors.NEON_YELLOW)
        self.screen.blit(hs_text, (50, 350))
        
        speed_text = self.font_small.render(f"Speed: {self.game_speed:.1f}x", True, Colors.NEON_PINK)
        self.screen.blit(speed_text, (1000, 150))
        
        food_text = self.font_small.render(f"Food: {self.food_eaten}", True, Colors.NEON_YELLOW)
        self.screen.blit(food_text, (1000, 200))
    
    def draw_pause_screen(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_title.render("PAUSED", True, Colors.NEON_YELLOW)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(pause_text, pause_rect)
        
        self.btn_resume.draw(self.screen, self.font_medium)
        self.btn_menu.draw(self.screen, self.font_medium)
    
    def draw_game_over_screen(self):
        """Draw game over screen"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        gameover_text = self.font_title.render("GAME OVER", True, Colors.NEON_PINK)
        gameover_rect = gameover_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(gameover_text, gameover_rect)
        
        score_text = self.font_large.render(f"Score: {self.score}", True, Colors.NEON_GREEN)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.screen.blit(score_text, score_rect)
        
        if self.score == self.high_score and self.score > 0:
            new_record = self.font_medium.render("NEW RECORD!", True, Colors.NEON_YELLOW)
            new_record_rect = new_record.get_rect(center=(SCREEN_WIDTH // 2, 380))
            self.screen.blit(new_record, new_record_rect)
        
        self.btn_restart.draw(self.screen, self.font_medium)
        self.btn_main_menu.draw(self.screen, self.font_medium)
    
    def run(self):
        """Main game loop"""
        while self.running:
            delta_time = min(self.clock.tick(FPS) / 1000.0, 0.016)
            
            self.handle_events()
            self.update(delta_time)
            self.draw()
        
        pygame.quit()
        print("Thanks for playing!")


# ==================== MAIN ====================
if __name__ == "__main__":
    game = Game()
    game.run()


# ==================== PARTICLE SYSTEM ====================
class Particle:
    """Represents a single particle effect"""
    
    def __init__(self, x: int, y: int, vx: float, vy: float, color: Tuple, lifetime: int):
        """Initialize a particle"""
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.age = 0
        self.size = 5

    def update(self):
        """Update particle position and age"""
        self.x += self.vx
        self.y += self.vy
        self.age += 1
        # Fade out particle
        self.size = max(1, 5 * (1 - self.age / self.lifetime))

    def draw(self, screen: pygame.Surface):
        """Draw particle"""
        if self.age < self.lifetime:
            alpha = int(255 * (1 - self.age / self.lifetime))
            color = tuple(int(c * (1 - self.age / self.lifetime)) for c in self.color)
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), int(self.size))

    def is_alive(self) -> bool:
        """Check if particle is still alive"""
        return self.age < self.lifetime


class ParticleSystem:
    """Manages particle effects"""
    
    def __init__(self):
        """Initialize particle system"""
        self.particles: List[Particle] = []

    def emit(self, x: int, y: int, count: int = 10, color: Tuple = COLOR_NEON_YELLOW):
        """Emit particles at position"""
        for _ in range(count):
            angle = random.uniform(0, 2 * 3.14159)
            speed = random.uniform(1, 3)
            vx = speed * __import__('math').cos(angle)
            vy = speed * __import__('math').sin(angle)
            particle = Particle(x, y, vx, vy, color, 30)
            self.particles.append(particle)

    def update(self):
        """Update all particles"""
        for particle in self.particles[:]:
            particle.update()
            if not particle.is_alive():
                self.particles.remove(particle)

    def draw(self, screen: pygame.Surface):
        """Draw all particles"""
        for particle in self.particles:
            particle.draw(screen)


# ==================== SNAKE CLASS ====================
class Snake:
    """Represents the snake entity"""
    
    def __init__(self, x: int = 5, y: int = 5):
        """Initialize snake"""
        self.body: List[Vector2] = [
            Vector2(x, y),
            Vector2(x - 1, y),
            Vector2(x - 2, y)
        ]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.growing = False

    def update(self):
        """Update snake position"""
        # Handle direction change
        if self.next_direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif self.next_direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif self.next_direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif self.next_direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

        # Move snake
        head = self.body[0]
        dx, dy = self.direction.value
        new_head = Vector2(head.x + dx, head.y + dy)
        self.body.insert(0, new_head)

        # Handle growth
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def set_direction(self, direction: Direction):
        """Set next direction"""
        self.next_direction = direction

    def grow(self):
        """Grow snake by one segment"""
        self.growing = True

    def check_collision_with_self(self) -> bool:
        """Check if snake collided with itself"""
        head = self.body[0]
        return head in self.body[1:]

    def check_collision_with_wall(self) -> bool:
        """Check if snake collided with wall"""
        head = self.body[0]
        return (head.x < 0 or head.x >= SCREEN_WIDTH // GRID_SIZE or 
                head.y < 0 or head.y >= SCREEN_HEIGHT // GRID_SIZE)

    def draw(self, screen: pygame.Surface):
        """Draw snake"""
        for i, segment in enumerate(self.body):
            x = segment.x * GRID_SIZE
            y = segment.y * GRID_SIZE
            
            # Head is brighter
            if i == 0:
                pygame.draw.rect(screen, COLOR_NEON_GREEN, 
                                (x, y, GRID_SIZE - 2, GRID_SIZE - 2))
                # Draw eyes
                self._draw_eyes(screen, x, y)
            else:
                # Gradient effect for body
                color = tuple(max(0, c - i * 5) for c in COLOR_GREEN)
                pygame.draw.rect(screen, color, 
                                (x, y, GRID_SIZE - 2, GRID_SIZE - 2))

    def _draw_eyes(self, screen: pygame.Surface, x: int, y: int):
        """Draw eyes on snake head"""
        eye_size = 2
        dx, dy = self.direction.value
        
        if dx == 1:  # Right
            eye1_pos = (x + GRID_SIZE - 3, y + 3)
            eye2_pos = (x + GRID_SIZE - 3, y + GRID_SIZE - 5)
        elif dx == -1:  # Left
            eye1_pos = (x + 3, y + 3)
            eye2_pos = (x + 3, y + GRID_SIZE - 5)
        elif dy == 1:  # Down
            eye1_pos = (x + 3, y + GRID_SIZE - 3)
            eye2_pos = (x + GRID_SIZE - 5, y + GRID_SIZE - 3)
        else:  # Up
            eye1_pos = (x + 3, y + 3)
            eye2_pos = (x + GRID_SIZE - 5, y + 3)
        
        pygame.draw.circle(screen, COLOR_WHITE, eye1_pos, eye_size)
        pygame.draw.circle(screen, COLOR_WHITE, eye2_pos, eye_size)
        pygame.draw.circle(screen, COLOR_BLACK, eye1_pos, 1)
        pygame.draw.circle(screen, COLOR_BLACK, eye2_pos, 1)


# ==================== FOOD CLASS ====================
class Food:
    """Represents the food entity"""
    
    def __init__(self, snake: Snake):
        """Initialize food"""
        self.position = Vector2(0, 0)
        self.snake = snake
        self.spawn()
        self.animation_frame = 0

    def spawn(self):
        """Spawn food at random position not occupied by snake"""
        while True:
            self.position = Vector2(
                random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1),
                random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
            )
            # Ensure food doesn't spawn inside snake
            if self.position not in self.snake.body:
                break

    def update(self):
        """Update food animation"""
        self.animation_frame = (self.animation_frame + 1) % 20

    def draw(self, screen: pygame.Surface):
        """Draw food with animation"""
        x = self.position.x * GRID_SIZE
        y = self.position.y * GRID_SIZE
        
        # Pulsing animation
        size = GRID_SIZE - 4 + int(3 * __import__('math').sin(self.animation_frame * 0.3))
        offset = (GRID_SIZE - size) // 2
        
        pygame.draw.rect(screen, COLOR_NEON_YELLOW, 
                        (x + offset, y + offset, size, size))
        pygame.draw.rect(screen, COLOR_GOLD, 
                        (x + offset, y + offset, size, size), 2)


# ==================== GAME CLASS ====================
class Game:
    """Main game class"""
    
    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Modern Snake Game")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.state = GameState.MENU
        self.running = True
        self.fullscreen = False
        
        # Game objects
        self.snake = Snake()
        self.food = Food(self.snake)
        self.particles = ParticleSystem()
        self.sound = SoundManager()
        
        # Scoring
        self.score = 0
        self.high_score = self.load_high_score()
        self.level = 1
        self.game_speed = INITIAL_SPEED
        
        # UI
        self.try_load_fonts()
        self.button_states = {'start': False, 'quit': False, 'restart': False}
        
        # Menu animation
        self.menu_time = 0

    def try_load_fonts(self):
        """Try to load fonts, fall back to default"""
        try:
            self.font_large = pygame.font.Font("assets/fonts/font.ttf", 72)
            self.font_medium = pygame.font.Font("assets/fonts/font.ttf", 48)
            self.font_small = pygame.font.Font("assets/fonts/font.ttf", 32)
            self.font_tiny = pygame.font.Font("assets/fonts/font.ttf", 20)
        except:
            self.font_large = pygame.font.Font(None, 72)
            self.font_medium = pygame.font.Font(None, 48)
            self.font_small = pygame.font.Font(None, 32)
            self.font_tiny = pygame.font.Font(None, 20)

    def load_high_score(self) -> int:
        """Load high score from file"""
        try:
            if os.path.exists('highscore.txt'):
                with open('highscore.txt', 'r') as f:
                    return int(f.read().strip())
        except:
            pass
        return 0

    def save_high_score(self):
        """Save high score to file"""
        try:
            with open('highscore.txt', 'w') as f:
                f.write(str(self.high_score))
        except:
            print("[WARNING] Could not save high score")

    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                # Global hotkeys
                if event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING or self.state == GameState.PAUSED:
                        self.state = GameState.MENU
                    else:
                        self.running = False
                
                if event.key == pygame.K_F11:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 
                                                              pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                # State-specific handling
                if self.state == GameState.MENU:
                    self.handle_menu_input(event)
                elif self.state == GameState.PLAYING:
                    self.handle_game_input(event)
                elif self.state == GameState.GAME_OVER:
                    self.handle_gameover_input(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.state == GameState.MENU:
                    self.handle_menu_click(mouse_pos)
                elif self.state == GameState.GAME_OVER:
                    self.handle_gameover_click(mouse_pos)

    def handle_menu_input(self, event):
        """Handle menu input"""
        pass

    def handle_menu_click(self, pos: Tuple[int, int]):
        """Handle menu click"""
        start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 350, 200, 60)
        quit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 450, 200, 60)
        
        if start_button_rect.collidepoint(pos):
            self.start_game()
            self.sound.play_sound('click')
        elif quit_button_rect.collidepoint(pos):
            self.running = False
            self.sound.play_sound('click')

    def handle_game_input(self, event):
        """Handle game input"""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.snake.set_direction(Direction.UP)
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake.set_direction(Direction.DOWN)
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake.set_direction(Direction.LEFT)
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake.set_direction(Direction.RIGHT)
        elif event.key == pygame.K_p:
            self.state = GameState.PAUSED

    def handle_gameover_click(self, pos: Tuple[int, int]):
        """Handle game over click"""
        restart_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 450, 200, 60)
        menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 530, 200, 60)
        
        if restart_button_rect.collidepoint(pos):
            self.start_game()
            self.sound.play_sound('click')
        elif menu_button_rect.collidepoint(pos):
            self.state = GameState.MENU
            self.sound.play_sound('click')

    def handle_gameover_input(self, event):
        """Handle game over input"""
        pass

    def start_game(self):
        """Start or restart game"""
        self.snake = Snake()
        self.food = Food(self.snake)
        self.score = 0
        self.level = 1
        self.game_speed = INITIAL_SPEED
        self.state = GameState.PLAYING

    def update(self):
        """Update game state"""
        if self.state == GameState.MENU:
            self.menu_time += 1
        elif self.state == GameState.PLAYING:
            self.snake.update()
            self.food.update()
            self.particles.update()
            
            # Check food collision
            if self.snake.body[0] == self.food.position:
                self.score += 10
                self.snake.grow()
                self.food.spawn()
                self.sound.play_sound('eat')
                self.particles.emit(
                    self.food.position.x * GRID_SIZE + GRID_SIZE // 2,
                    self.food.position.y * GRID_SIZE + GRID_SIZE // 2,
                    count=15,
                    color=COLOR_NEON_YELLOW
                )
                
                # Update level and speed
                self.level = 1 + self.score // (DIFFICULTY_INCREASE_INTERVAL * 10)
                self.game_speed = min(INITIAL_SPEED + (self.level - 1) * 2, MAX_SPEED)
            
            # Check collisions
            if self.snake.check_collision_with_self() or self.snake.check_collision_with_wall():
                self.state = GameState.GAME_OVER
                self.sound.play_sound('gameover')
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.save_high_score()
        
        elif self.state == GameState.PAUSED:
            pass

    def draw(self):
        """Draw game"""
        self.screen.fill(COLOR_DARK_BG)
        
        # Draw grid
        self.draw_grid()
        
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_pause_screen()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()
        
        pygame.display.flip()

    def draw_grid(self):
        """Draw grid background"""
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y), 1)

    def draw_menu(self):
        """Draw main menu"""
        # Title
        title_surface = self.font_large.render("SNAKE GAME", True, COLOR_NEON_GREEN)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_surface, title_rect)
        
        # Subtitle with animation
        pulse = __import__('math').sin(self.menu_time * 0.05) * 10
        subtitle_surface = self.font_small.render("Modern Python Edition", True, COLOR_NEON_BLUE)
        subtitle_rect = subtitle_surface.get_rect(center=(SCREEN_WIDTH // 2, 200 + pulse))
        self.screen.blit(subtitle_surface, subtitle_rect)
        
        # Start button
        start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 350, 200, 60)
        pygame.draw.rect(self.screen, COLOR_NEON_GREEN, start_button_rect, 2)
        start_text = self.font_small.render("START GAME", True, COLOR_NEON_GREEN)
        start_text_rect = start_text.get_rect(center=start_button_rect.center)
        self.screen.blit(start_text, start_text_rect)
        
        # Quit button
        quit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 450, 200, 60)
        pygame.draw.rect(self.screen, COLOR_NEON_PINK, quit_button_rect, 2)
        quit_text = self.font_small.render("QUIT", True, COLOR_NEON_PINK)
        quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
        self.screen.blit(quit_text, quit_text_rect)
        
        # High score
        high_score_text = self.font_tiny.render(f"High Score: {self.high_score}", 
                                               True, COLOR_GOLD)
        self.screen.blit(high_score_text, (20, SCREEN_HEIGHT - 40))
        
        # Instructions
        ins_text = self.font_tiny.render("Arrow Keys/WASD to move | P to pause | ESC to menu | F11 for fullscreen", 
                                        True, COLOR_WHITE)
        ins_rect = ins_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
        self.screen.blit(ins_text, ins_rect)

    def draw_game(self):
        """Draw gameplay"""
        # Draw game objects
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self.particles.draw(self.screen)
        
        # Draw UI
        score_text = self.font_small.render(f"Score: {self.score}", True, COLOR_NEON_GREEN)
        self.screen.blit(score_text, (20, 20))
        
        level_text = self.font_small.render(f"Level: {self.level}", True, COLOR_NEON_BLUE)
        self.screen.blit(level_text, (20, 60))
        
        high_score_text = self.font_small.render(f"High: {self.high_score}", True, COLOR_GOLD)
        self.screen.blit(high_score_text, (20, 100))
        
        # Speed indicator
        speed_text = self.font_tiny.render(f"Speed: {self.game_speed}", True, COLOR_NEON_YELLOW)
        self.screen.blit(speed_text, (SCREEN_WIDTH - 200, 20))

    def draw_pause_screen(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(COLOR_BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_large.render("PAUSED", True, COLOR_NEON_YELLOW)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(pause_text, pause_rect)
        
        resume_text = self.font_small.render("Press P to Resume | ESC to Menu", True, COLOR_WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        self.screen.blit(resume_text, resume_rect)

    def draw_game_over(self):
        """Draw game over screen"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(COLOR_BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text
        gameover_text = self.font_large.render("GAME OVER", True, COLOR_NEON_PINK)
        gameover_rect = gameover_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(gameover_text, gameover_rect)
        
        # Score
        score_text = self.font_medium.render(f"Final Score: {self.score}", True, COLOR_NEON_GREEN)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
        self.screen.blit(score_text, score_rect)
        
        # High score
        high_text = self.font_medium.render(f"High Score: {self.high_score}", True, COLOR_GOLD)
        high_rect = high_text.get_rect(center=(SCREEN_WIDTH // 2, 330))
        self.screen.blit(high_text, high_rect)
        
        # New high score message
        if self.score == self.high_score and self.score > 0:
            new_high_text = self.font_small.render("*** NEW HIGH SCORE ***", True, COLOR_NEON_YELLOW)
            new_high_rect = new_high_text.get_rect(center=(SCREEN_WIDTH // 2, 400))
            self.screen.blit(new_high_text, new_high_rect)
        
        # Buttons
        restart_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 450, 200, 60)
        pygame.draw.rect(self.screen, COLOR_NEON_GREEN, restart_button_rect, 2)
        restart_text = self.font_small.render("RESTART", True, COLOR_NEON_GREEN)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        self.screen.blit(restart_text, restart_text_rect)
        
        menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 530, 200, 60)
        pygame.draw.rect(self.screen, COLOR_NEON_BLUE, menu_button_rect, 2)
        menu_text = self.font_small.render("MAIN MENU", True, COLOR_NEON_BLUE)
        menu_text_rect = menu_text.get_rect(center=menu_button_rect.center)
        self.screen.blit(menu_text, menu_text_rect)

    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.game_speed if self.state == GameState.PLAYING else FPS)
        
        self.quit()

    def quit(self):
        """Clean up and quit"""
        pygame.quit()
        print("Thanks for playing!")


# ==================== MAIN ====================
if __name__ == "__main__":
    game = Game()
    game.run()
