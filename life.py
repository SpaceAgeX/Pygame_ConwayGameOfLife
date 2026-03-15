import random

import pygame

from config import (
    ALIVE_COLOR,
    CELL_SIZE,
    COLS,
    DEAD_COLOR,
    GRID_BG_COLOR,
    GRID_HEIGHT,
    GRID_LINE_COLOR,
    GRID_WIDTH,
    ROWS,
    TOP_BAR_HEIGHT,
)


def make_grid(randomize=False):
    if randomize:
        return [[1 if random.random() < 0.24 else 0 for _ in range(COLS)] for _ in range(ROWS)]
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]


def step_grid(grid):
    next_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):
            neighbors = 0
            for y_offset in (-1, 0, 1):
                for x_offset in (-1, 0, 1):
                    if x_offset == 0 and y_offset == 0:
                        continue
                    n_row = row + y_offset
                    n_col = col + x_offset
                    if 0 <= n_row < ROWS and 0 <= n_col < COLS:
                        neighbors += grid[n_row][n_col]

            if grid[row][col] == 1 and neighbors in (2, 3):
                next_grid[row][col] = 1
            elif grid[row][col] == 0 and neighbors == 3:
                next_grid[row][col] = 1

    return next_grid


def draw_grid(surface, grid):
    grid_rect = pygame.Rect(0, TOP_BAR_HEIGHT, GRID_WIDTH, GRID_HEIGHT)
    pygame.draw.rect(surface, GRID_BG_COLOR, grid_rect)

    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = TOP_BAR_HEIGHT + row * CELL_SIZE
            color = ALIVE_COLOR if grid[row][col] else DEAD_COLOR
            pygame.draw.rect(surface, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, GRID_LINE_COLOR, (x, y, CELL_SIZE, CELL_SIZE), width=1)


def pos_to_cell(pos):
    x, y = pos
    if y < TOP_BAR_HEIGHT:
        return None

    col = x // CELL_SIZE
    row = (y - TOP_BAR_HEIGHT) // CELL_SIZE
    if 0 <= row < ROWS and 0 <= col < COLS:
        return row, col
    return None


def apply_tool(grid, pos, tool_mode):
    cell = pos_to_cell(pos)
    if cell is None:
        return

    row, col = cell
    if tool_mode == "draw":
        grid[row][col] = 1
    elif tool_mode == "erase":
        grid[row][col] = 0
