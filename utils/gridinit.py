# from settings import *
# from colorbutton import *
from .settings import *
import pygame, sys

class Grid:
    def __init__(self, rows, cols, color='white', grid_line=False):
        self.rows = rows
        self.cols = cols
        self.pixel_size = (WIDTH - TOOLBAR_WIDTH) // self.rows
        self.color = color
        # init the grid for area drawing
        self.grid = []
        for i in range(self.rows):
            self.grid.append([])
            for _ in range(self.cols):
                self.grid[i].append(self.color)

        self.grid_line = grid_line
        
    def draw_grid(self, win):
        for i, row in enumerate(self.grid):
            for j, pixel in enumerate(row):
                if (j * self.pixel_size) <= (WIDTH - TOOLBAR_WIDTH):
                    pygame.draw.rect(win, pixel, (j * self.pixel_size, i * self.pixel_size, self.pixel_size, self.pixel_size))

        if self.grid_line:
            for i in range(self.rows + 1): # draw some horizontal lines
                pygame.draw.line(win, 'black', (0, i * self.pixel_size), ((WIDTH - TOOLBAR_WIDTH) , i * self.pixel_size)) # (surface, color, start position, end position)

            for i in range(self.cols + 1): # draw some vertical lines
                if (i * self.pixel_size) <= (WIDTH - TOOLBAR_WIDTH):
                    pygame.draw.line(win, 'black', (i * self.pixel_size, 0), (i * self.pixel_size, HEIGHT))

    # fill the grid for our screen
    def draw(self, win, buttons_1, buttons_2, buttons_3):
        # win.fill(BG_COLOR)
        self.draw_grid(win)

        for button in buttons_1:
            button.draw(win)

        for button in buttons_2:
            button.draw(win)

        for button in buttons_3:
            button.draw(win)

        pygame.draw.rect(win, 'black', (WIDTH - TOOLBAR_WIDTH, 0, TOOLBAR_WIDTH, TOOLBAR_HEIGHT), 5)
        pygame.display.update()

    def get_row_col_from_pos(self, pos):
        x, y = pos
        row = y // self.pixel_size # return row and col index
        col = x // self.pixel_size

        if col >= self.cols:
            raise IndexError

        return row, col

        # example: (9, 4), pixel_size = 5
        # 9 // 5 = 1
        # 4 // 5 = 0
        
def main_grid():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    buttons_color_1 = []
    buttons_color_2 = []
    buttons_tool = []
    
    button_x = 0
    button_y = 0
    for i, color in enumerate(COLORS_1):
        if button_x < 8:
            buttons_color_1.append( ColorButton((button_x * 24) + (WIDTH - TOOLBAR_WIDTH), button_y * 24, 24, 24, color) )
            button_x += 1
        else:
            button_x = 0
            button_y += 1

    button_x = 0
    for i, color in enumerate(COLORS_2):
        if button_x < 8:
            buttons_color_2.append( ColorButton((button_x * 24 ) + (WIDTH - TOOLBAR_WIDTH), button_y * 24, 24, 24, color) )
            button_x += 1
        else:
            button_x = 0
            button_y += 1

    buttons_tool.append(ColorButton(WIDTH - TOOLBAR_WIDTH + 192, 0, 128, 60, WHITE, "ERASE", BLACK))
    buttons_tool.append(ColorButton(WIDTH - TOOLBAR_WIDTH + 192, 60, 128, 60, WHITE, "CLEAR", BLACK))
    buttons_tool.append(ColorButton(WIDTH - TOOLBAR_WIDTH + 192, 120, 128, 60, WHITE, "MORE COLORS", BLACK))
    buttons_tool.append(ColorButton(WIDTH - TOOLBAR_WIDTH, 660, 320, 60, WHITE, "BACK", BLACK))
    
    while True:
        win.fill('pink')
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        grid = Grid(50, 50, color='green', grid_line=True)
        grid.draw(win, buttons_color_1, buttons_color_2, buttons_tool)
                
        pygame.display.update()
        clock.tick(FPS)
        
if __name__ == '__main__':
    main_grid()

