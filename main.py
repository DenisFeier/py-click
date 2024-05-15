import pygame

pygame.init()

size = (500, 500)

window = pygame.display.set_mode(size)

rgb = (141, 34, 255)

window.fill(rgb)

clock = pygame.time.Clock()

card_color = (255, 0, 0)

border_color = (0, 255, 0)

text_color = (0, 0, 255)

font = pygame.font.SysFont('verdana', 20)

class Area():
    def _init_(self, x = 0, y = 0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
        self.shift_x = x + 10
        self.shift_y = height / 2 + y
        self.textArea = font.render("Click", True, text_color)

    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)
    
    def drawText(self):
        window.blit(self.textArea, (self.shift_x, self.shift_y))

cards = [
    Area(75, 150, 50, 100, card_color),
    Area(175, 150, 50, 100, card_color),
    Area(275, 150, 50, 100, card_color),
    Area(375, 150, 50, 100, card_color)
]

while True:
    pygame.display.update()

    for c in cards:
        c.fill()
        c.outline(border_color, 5)
        c.drawText()

    clock.tick(40)
