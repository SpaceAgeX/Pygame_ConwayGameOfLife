# Conway's Game of Life in Pygame

A simple interactive implementation of Conway's Game of Life built with Python and Pygame.

## Features

- Start with a random board state
- Pause and resume the simulation
- Clear the board with `Reset Blank`
- Generate a new random layout with `Reset Random`
- When paused, use `Draw` and `Erase` tools to edit cells by clicking or dragging

## Controls

- `Pause` / `Play`: stop or continue the simulation
- `Reset Blank`: clear every cell
- `Reset Random`: create a new random arrangement
- `Draw`: while paused, paint live cells onto the grid
- `Erase`: while paused, remove live cells from the grid

## Requirements

- Python 3.10+
- `pygame`

## Installation

```bash
pip install pygame
```

## Run

```bash
python main.py
```

## Project Structure

- `main.py`: app entrypoint
- `app.py`: main game loop and event handling
- `life.py`: Conway simulation rules and grid helpers
- `ui.py`: reusable UI button class
- `config.py`: window settings, layout values, and colors
