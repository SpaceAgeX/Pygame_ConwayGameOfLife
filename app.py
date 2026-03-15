import sys

import pygame

from config import BG_COLOR, FPS, TEXT_COLOR, TOP_BAR_COLOR, TOP_BAR_HEIGHT, WINDOW_HEIGHT, WINDOW_WIDTH
from life import apply_tool, draw_grid, make_grid, step_grid
from ui import Button


def run():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("segoeui", 24)
    small_font = pygame.font.SysFont("segoeui", 20)

    play_button = Button((14, 14, 110, 42), "Pause")
    blank_button = Button((136, 14, 145, 42), "Reset Blank")
    random_button = Button((293, 14, 160, 42), "Reset Random")
    draw_button = Button((465, 14, 95, 42), "Draw")
    erase_button = Button((572, 14, 95, 42), "Erase")

    grid = make_grid(randomize=True)
    running = True
    paused = False
    tool_mode = "draw"
    dragging = False

    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif play_button.is_clicked(event):
                paused = not paused
                dragging = False

            elif blank_button.is_clicked(event):
                grid = make_grid(randomize=False)
                dragging = False

            elif random_button.is_clicked(event):
                grid = make_grid(randomize=True)
                dragging = False

            elif paused and draw_button.is_clicked(event):
                tool_mode = "draw"

            elif paused and erase_button.is_clicked(event):
                tool_mode = "erase"

            elif paused and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[1] >= TOP_BAR_HEIGHT:
                    dragging = True
                    apply_tool(grid, event.pos, tool_mode)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False

            elif paused and event.type == pygame.MOUSEMOTION and dragging:
                apply_tool(grid, event.pos, tool_mode)

        if not paused:
            grid = step_grid(grid)

        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, TOP_BAR_COLOR, (0, 0, WINDOW_WIDTH, TOP_BAR_HEIGHT))
        draw_grid(screen, grid)

        play_button.label = "Play" if paused else "Pause"
        play_button.draw(screen, font, mouse_pos, active=False)
        blank_button.draw(screen, small_font, mouse_pos, active=False)
        random_button.draw(screen, small_font, mouse_pos, active=False)

        if paused:
            draw_button.draw(screen, font, mouse_pos, active=tool_mode == "draw")
            erase_button.draw(screen, font, mouse_pos, active=tool_mode == "erase")

            hint = small_font.render("Paused Simulation...", True, TEXT_COLOR)
            screen.blit(hint, (690, 25))
        else:
            status = small_font.render("Running Simulation...", True, TEXT_COLOR)
            screen.blit(status, (690, 25))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
