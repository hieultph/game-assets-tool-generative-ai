from PIL import Image, ImageSequence
import pygame, sys

class Gif:
    def __init__(self, gif_path, scale=1):
        self.gif_path = gif_path
        self.scale = scale
        self.pos = (0, 0)
        self.gif = Image.open(self.gif_path)
        counter = 0
        for frame in ImageSequence.Iterator(self.gif):
            counter += 1
        self.length = counter
        self.index = 0
        frame = ImageSequence.Iterator(self.gif)[self.index]
        self.width, self.height = int(frame.size[0]*self.scale), int(frame.size[1]*self.scale)
        
    def pilImageToSurface(self, gif):
        data, size, mode = gif.tobytes(), gif.size, gif.mode
        return pygame.image.fromstring(data, size, mode).convert_alpha()
    
    def draw(self, win, pos):
        self.pos = pos
        if self.index == self.length:
            self.index = 0
        if self.gif.format == 'GIF' and self.gif.is_animated:
            frame = ImageSequence.Iterator(self.gif)[self.index]
            size = (self.width, self.height)
            frame = frame.resize(size, resample=Image.LANCZOS)
            win.blit(self.pilImageToSurface(frame.convert('RGBA')), pos)
        else:
            win.blit(self.pilImageToSurface(self.gif))
        self.index += 1
    
    def isClicked(self, pos):
        if pos[0] in range(self.pos[0], self.pos[0]+self.width) and pos[1] in range(self.pos[1], self.pos[1]+self.height):
            return True
        
        return False
            
def main_gif_player():
    pygame.init()
    win = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    gif = Gif('gif_images/guydance.gif', 0.5)
    while True:
        win.fill('pink')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                if gif.isClicked(pygame.mouse.get_pos()):
                    print("You clicked")
                else: pass
                
        gif.draw(win, (500, 500))
        pygame.display.update()
        clock.tick(30)
    
if __name__ == "__main__":
    main_gif_player()