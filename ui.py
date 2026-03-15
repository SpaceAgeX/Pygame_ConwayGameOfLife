import pygame

from config import (
    BORDER_COLOR,
    BUTTON_ACTIVE_COLOR,
    BUTTON_ACTIVE_TEXT,
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
    TEXT_COLOR,
)


class Button:
    def __init__(self, rect, label):
        self.rect = pygame.Rect(rect)
        self.label = label

    def draw(self, surface, font, mouse_pos, active=False):
        hovered = self.rect.collidepoint(mouse_pos)
        fill = BUTTON_ACTIVE_COLOR if active else BUTTON_HOVER_COLOR if hovered else BUTTON_COLOR
        text_color = BUTTON_ACTIVE_TEXT if active else TEXT_COLOR

        pygame.draw.rect(surface, fill, self.rect, border_radius=8)
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, width=2, border_radius=8)

        text = font.render(self.label, True, text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )
