from .settings import *

# init the grid for area drawing
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            if (j * PIXEL_SIZE) <= (WIDTH - TOOLBAR_WIDTH):
                pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1): # draw some horizontal lines
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), ((WIDTH - TOOLBAR_WIDTH) , i * PIXEL_SIZE)) # (surface, color, start position, end position)

        for i in range(COLS + 1): # draw some vertical lines
            if (i * PIXEL_SIZE) <= (WIDTH - TOOLBAR_WIDTH):
                pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT))

# fill the grid for our screen
def draw(win, grid, buttons_1, buttons_2, buttons_3):
    # win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons_1:
        button.draw(win)

    for button in buttons_2:
        button.draw(win)

    for button in buttons_3:
        button.draw(win)

    pygame.draw.rect(win, BLACK, (WIDTH - TOOLBAR_WIDTH, 0, TOOLBAR_WIDTH, TOOLBAR_HEIGHT), 5)

    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE # return row and col index
    col = x // PIXEL_SIZE

    if col >= COLS:
        raise IndexError

    return row, col

    # example: (9, 4), pixel_size = 5
    # 9 // 5 = 1
    # 4 // 5 = 0


