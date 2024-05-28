import pygame
import numpy as np
from button import Button

# Constants
WIDTH, HEIGHT = 800, 800
N = 100  # Grid size
CELL_SIZE = WIDTH // N
FPS = 10  # Frames per second, controls the update speed

# Colors
DEAD = (0, 0, 0)
ALIVE = (255, 255, 255)

# Button initialization
start = 40
play_button = Button((0, 255, 0), 650, start + 60, 100, 50, 'Play')
pause_button = Button((255, 255, 0), 650, start + 60*2, 100, 50, 'Pause')
reset_button = Button((212, 112, 78), 650, start + 60*3, 100, 50, 'Reset')
close_button = Button((78, 172, 212), 650, start + 60*4, 100, 50, 'Close')

# Initialize Pygame
pygame.init()

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Grid setup
grid = np.zeros((N, N), dtype=int)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            color = ALIVE if grid[y // CELL_SIZE][x // CELL_SIZE] else DEAD
            pygame.draw.rect(screen, color, rect)

def update_grid():
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Calculate the number of alive neighbors
            total = sum([grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                        grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                        grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                        grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]])
            if grid[i, j] == 1:
                # Apply the rules for live cells
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            elif total == 3:
                # Apply the rule for dead cells
                new_grid[i, j] = 1
    return new_grid

# Control variable
running = True
paused = True
right_mouse_button_down = False

# Game loop
while running:
    screen.fill(DEAD)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              paused = not paused
        if event.type == pygame.MOUSEBUTTONDOWN and paused:
            x, y = pygame.mouse.get_pos()
            x, y = x // CELL_SIZE, y // CELL_SIZE
            grid[y][x] = not grid[y][x]
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:  # Left mouse button
              if play_button.is_over(pos):
                  paused = False
              elif pause_button.is_over(pos):
                  paused = True
              elif reset_button.is_over(pos):
                  grid = np.zeros((N, N), dtype=int)  # Reset the grid
              elif close_button.is_over(pos):
                  running = False  # Close the application
          elif event.button == 3:  # Right mouse button
              right_mouse_button_down = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:  # Right mouse button
                right_mouse_button_down = False

        if right_mouse_button_down:
            x, y = pos
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:  # Ensure within bounds
                grid_x = x // CELL_SIZE
                grid_y = y // CELL_SIZE
                grid[grid_y][grid_x] = 1  # Set cell alive when right mouse is down and moving

    if not paused:
        grid = update_grid()


    draw_grid()
    play_button.draw(screen, (0, 0, 0))
    pause_button.draw(screen, (0, 0, 0))
    reset_button.draw(screen, (0, 0, 0))
    close_button.draw(screen, (0, 0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()