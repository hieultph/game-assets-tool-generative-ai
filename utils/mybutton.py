import pygame, sys
from PIL import Image
from .settings import *

class MyButton:
    def __init__(self, pos, text_input, font, base_color, hovering_color="", image_path="", image_cover_text=False, border=0, href=""):
        self.href = href
        self.image = pygame.image.load(image_path)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.border = border
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        if image_cover_text:
            self.image = pygame.transform.scale(self.image, (self.text.get_width()+self.border, self.text.get_height()+self.border)) 
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if self.hovering_color=="":
                self.text = self.font.render(self.text_input, True, self.base_color)
            else:
                self.text = self.font.render(self.text_input, True, self.hovering_color)   
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            
def main_my_button():
    pygame.init()
    win = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    win.fill('pink')
    
    test_button = MyButton(pos=(500, 500), text_input="test gvuhdfsgiuhdsgiuhfgiuhfiugh", font=get_font(50), base_color='green', image_path='./images/assets/Play Rect.png', image_cover_text=True, border=0)
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        test_button.changeColor(mouse_pos)
        test_button.update(win)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(60)
        
if __name__ == '__main__':
    main_my_button()