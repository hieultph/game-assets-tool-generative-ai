import sys, os
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename
from utils import *
import pyperclip

# FONT = pygame.font.Font(None, 50)
grid_line = False
rows, cols = 50, 50 # for each pixel inside our area drawing

email = "LeHieuTester@gmail.com"
password = 'Tester666!'

def monster_mash_window():
    pygame.display.set_caption("Stable Diffusion App - Monster Mash")
    while True:
        screen.blit(mm_background_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        buttons = []
        
        open_button = MyButton(image_path='./images/assets/Play Rect.png', pos = (640, 200), text_input="OPEN MONSTER MASH",
                                font=get_font(75), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10)

        back_button = MyButton(image_path='./images/assets/Play Rect.png', pos=(640, 460), text_input="Back", 
                                font=get_font(75), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10)
        
        buttons.append(open_button)
        buttons.append(back_button)
        
        for button in buttons:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                background_sound.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    main_menu()
                if open_button.checkForInput(mouse_pos):
                    # minimized window (ugly hack)
                    pygame.display.set_mode((1, 1))
                    try:
                        ucChrome = GoogleColab()
                        ucChrome.open_link('https://monstermash.zone/')
                    except Exception as e:
                        print(e)
                    finally: 
                        pygame.display.set_mode((WIDTH, HEIGHT))
                        
        pygame.display.update()

def mini_paint_window():
    pygame.display.set_caption("Stable Diffusion App - Mini Paint")
    screen.fill('white')
    grid = Grid(rows, cols, grid_line=grid_line)
    drawing_color = BLACK
    mouse_pos = pygame.mouse.get_pos()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                background_sound.stop()
                pygame.quit()
                sys.exit()
            
            if pygame.mouse.get_pressed()[0]: # left mouse click
                pos = pygame.mouse.get_pos()
                try:
                    row, col = grid.get_row_col_from_pos(pos)
                    grid.grid[row][col] = drawing_color
                except IndexError:
                    for button in buttons_color_1:
                        if not button.clicked(pos):
                            continue
                        
                        drawing_color = button.color

                    for button in buttons_color_2:
                        if not button.clicked(pos):
                            continue

                        drawing_color = button.color

                    for button in buttons_tool:
                        if not button.clicked(pos):
                            continue

                        if button.text == "CLEAR":
                            grid = Grid(rows, cols, grid_line=grid_line)
                            drawing_color = BLACK
                        elif button.text == "ERASE":
                            drawing_color = button.color
                        elif button.text == "MORE COLORS":
                            color = colorchooser.askcolor()[0] # get the rgb color
                            if color is None: continue
                            else: drawing_color = color
                        elif button.text == "BACK":
                            main_menu()

        grid.draw(screen, buttons_color_1, buttons_color_2, buttons_tool)
        
        pygame.display.update()
        clock.tick(FPS)

def stable_diffusion_window():
    pygame.display.set_caption("Stable Diffusion App - Stable diffusion")
    buttons = []
    model_buttons = []
    
    run_script_button_1 = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH*1/6, HEIGHT*1/6), text_input="SD - v1.5", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10,
                                   href="https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/nightly/stable_diffusion_1_5_webui_colab.ipynb")
    run_script_button_2 = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH*3/6, HEIGHT*1/6), text_input="SD - v2.1", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10,
                                   href="https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/nightly/stable_diffusion_v2_1_webui_colab.ipynb")
    run_script_button_3 = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH*5/6, HEIGHT*1/6), text_input="WAIFU v1.5", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10,
                                   href="https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/nightly/waifu_diffusion_v1_5_webui_colab.ipynb")
    run_script_button_4 = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH*1/6, HEIGHT*2/6), text_input="ANYTHING v3", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10,
                                   href="https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/nightly/anything_3_webui_colab.ipynb")
    run_script_button_5 = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH*3/6, HEIGHT*2/6), text_input="CHILLOUTMIX", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10,
                                   href="https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/nightly/chillout_mix_webui_colab.ipynb")
    run_script_button_6 = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH*5/6, HEIGHT*2/6), text_input="OPENJOURNEY", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10,
                                   href="https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/nightly/openjourney_v2_diffusion_webui_colab.ipynb")
    
    back_button = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH/2, HEIGHT*5/6), text_input="BACK", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10)
    
    run_script_with_link_option_button = MyButton(image_path='./images/assets/Play Rect.png', pos=(WIDTH/2, HEIGHT*3/6), text_input="RUN SCRIPT WITH LINK OPTION", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_cover_text=True, border=10)
    
    model_buttons.append(run_script_button_1)
    model_buttons.append(run_script_button_2)
    model_buttons.append(run_script_button_3)
    model_buttons.append(run_script_button_4)
    model_buttons.append(run_script_button_5)
    model_buttons.append(run_script_button_6)
    
    buttons.append(back_button) 
    buttons.append(run_script_with_link_option_button)
    
    user_input = inputbox.InputBox(run_script_with_link_option_button.text_rect.bottomleft[0]-20, run_script_with_link_option_button.text_rect.bottomleft[1]+20,
                                        run_script_with_link_option_button.text.get_width()+20, run_script_with_link_option_button.text.get_height()+20,
                                        text="TYPE YOUR GOOGLE COLAB LINK HERE (HIT ENTER TO DELETE ALL): ")

    copy_button = ColorButton(user_input.rect.bottomleft[0], user_input.rect.bottomleft[1], user_input.width/3, user_input.height/3, "white", "COPY", "green")
    paste_button = ColorButton(user_input.rect.bottomleft[0]+copy_button.width, user_input.rect.bottomleft[1], user_input.width/3, user_input.height/3, "white", "PASTE", "green")
    erase_button = ColorButton(user_input.rect.bottomleft[0]+copy_button.width*2, user_input.rect.bottomleft[1], user_input.width/3, user_input.height/3, "white", "ERASE", "green")

    while True:
        screen.blit(sd_background_image, (0, 0))
        sd_mouse_pos = pygame.mouse.get_pos()

        for button in model_buttons:
            button.changeColor(sd_mouse_pos)
            button.update(screen)

        for button in buttons:
            button.changeColor(sd_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                for button in model_buttons:
                    if button.checkForInput(sd_mouse_pos):
                        try:
                            gcolab = GoogleColab()
                            pygame.display.set_mode((1, 1))
                            # gcolab.signin_manual()
                            gcolab.signin(email, password)
                            time.sleep(3)
                            gcolab.run_gc_by_link(button.href)
                        except Exception as e:
                            print(e)
                        pygame.display.set_mode((WIDTH, HEIGHT))
                
                if copy_button.clicked(sd_mouse_pos):
                    pyperclip.copy(user_input.text)
                elif paste_button.clicked(sd_mouse_pos):
                    user_input.text += pyperclip.paste()
                elif erase_button.clicked(sd_mouse_pos):
                    user_input.text = ""
                elif run_script_with_link_option_button.checkForInput(sd_mouse_pos):    
                    try:
                        gcolab = GoogleColab()
                        pygame.display.set_mode((1, 1))
                        # gcolab.signin_manual()
                        gcolab.signin(email, password)
                        time.sleep(3)
                        gcolab.run_gc_by_link(user_input.text)
                    except Exception as e:
                        print(e)
                    pygame.display.set_mode((WIDTH, HEIGHT))
                        
                elif back_button.checkForInput(sd_mouse_pos):
                    main_menu()

                user_input.update()

            user_input.handle_event(event)
        
        # user_input.update()
        user_input.draw(screen)

        copy_button.draw(screen)
        paste_button.draw(screen)
        erase_button.draw(screen)

        pygame.display.flip()

        clock.tick(60)

def main_menu():
    pygame.display.set_caption("Stable Diffusion App - Main Menu")
    load_sound_gif = Gif('./gif_images/guydance.gif')
    setting_gif = Gif('./gif_images/catguitar.gif', 0.2)
    while True:
        screen.blit(menu_background_image, (0, 0))
        load_sound_gif.draw(screen, (1000, 500))
        setting_gif.draw(screen, (0, 0))
        
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = MyButton(image_path="./images/assets/Play Rect.png", pos=(640, 100), text_input="STABLE TOOL", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING)
        menu_text.update(screen)

        monster_mash_button = MyButton(image_path="./images/assets/Play Rect.png", pos=(320, 250), text_input="M-MASH", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING)
        mini_paint_button = MyButton(image_path="./images/assets/Play Rect.png", pos=(960, 250), 
                            text_input="M-PAINT", font=get_font(50), base_color="#d7fcd4", hovering_color=TEXT_COLOR_HOVERING)
        stable_diffusion_button = MyButton(image_path="./images/assets/Play Rect.png", pos=(320, 450), 
                            text_input="S-Diffusion", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING)

        quit_button = MyButton(image_path="./images/assets/Play Rect.png", pos=(960, 450), 
                            text_input="QUIT", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING)

        for button in [monster_mash_button, mini_paint_button, stable_diffusion_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                background_sound.stop()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if monster_mash_button.checkForInput(menu_mouse_pos):
                    monster_mash_window()
                if mini_paint_button.checkForInput(menu_mouse_pos):
                    mini_paint_window()
                if stable_diffusion_button.checkForInput(menu_mouse_pos):
                    stable_diffusion_window()
                if quit_button.checkForInput(menu_mouse_pos):
                    background_sound.stop()
                    pygame.quit()
                    sys.exit()
                        
                if pygame.mouse.get_pressed()[0]:
                    if load_sound_gif.isClicked(menu_mouse_pos):
                        sound_path = askopenfilename(defaultextension=".mp3", initialdir='./sounds', title="Choose your favorite sound and enjoy!!",
                                                    filetypes=(("audio files", "*.mp3"),
                                                                ("all files", "*.*")))
                        if sound_path == "":
                            pass
                        else:
                            try:
                                pygame.mixer.quit()
                                pygame.mixer.init()
                                background_sound = pygame.mixer.Sound(sound_path)
                                background_sound.play(-1)
                                sound_path = None
                            except Exception:
                                pass
                if setting_gif.isClicked(menu_mouse_pos):
                    setting_menu()
                            
        pygame.display.update()
        clock.tick(FPS)

def setting_menu():
    pygame.display.set_caption("Stable Diffusion App - Setting Menu")
    global grid_line, rows, cols
    buttons = []
    title_buttons = []
    display_buttons = []
    mp_buttons = []
    
    back_button = MyButton(pos=(WIDTH/2, HEIGHT*5/6), text_input="BACK", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_path='./images/assets/Play Rect.png', image_cover_text=True, border=10)
    buttons.append(back_button)
    
    display_button = MyButton(pos=(WIDTH*1/3, HEIGHT*1/6), text_input="DISPLAY", font=get_font(50), base_color=TEXT_COLOR, image_path='./images/assets/Play Rect.png', image_cover_text=True, border=10)
    mp_button = MyButton(pos=(WIDTH*2/3, HEIGHT*1/6), text_input="M-PAINT", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_path='./images/assets/Play Rect.png', image_cover_text=True, border=10)
    title_buttons.append(display_button)
    title_buttons.append(mp_button)

    fullscreen_button = MyButton(pos=(WIDTH*1/3, HEIGHT*2/6), text_input="fullscreen", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_path='./images/assets/Play Rect.png', image_cover_text=True, border=10)
    p720 = MyButton(pos=(WIDTH*1/3, HEIGHT*3/6), text_input="1280x720", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_path='./images/assets/Play Rect.png', image_cover_text=True, border=10)
    display_buttons.append(fullscreen_button)
    display_buttons.append(p720)
    
    grid_mode_button = MyButton(pos=(WIDTH*2/3, HEIGHT*2/6), text_input="grid mode", font=get_font(50), base_color=TEXT_COLOR, hovering_color=TEXT_COLOR_HOVERING, image_path='./images/assets/Play Rect.png', image_cover_text=True, border=10)
    mp_buttons.append(grid_mode_button)
    
    while True:
        screen.blit(setting_background_image, (0, 0))
        setting_mouse_pos = pygame.mouse.get_pos()
        
        for button in buttons:
            button.changeColor(setting_mouse_pos)
            button.update(screen)
        
        for button in title_buttons:
            button.update(screen)
    
        for button in display_buttons:
            button.update(screen)
            
        for button in mp_buttons:
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                background_sound.stop()
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                if back_button.checkForInput(setting_mouse_pos):
                    main_menu()
                if fullscreen_button.checkForInput(setting_mouse_pos):
                    fullscreen_button.changeColor(setting_mouse_pos)
                    pygame.display.toggle_fullscreen()
                if p720.checkForInput(setting_mouse_pos):
                    p720.changeColor(setting_mouse_pos)
                    pygame.display.set_mode((1280, 720))
                if grid_mode_button.checkForInput(setting_mouse_pos):
                    if grid_line:
                        grid_line = False
                    else:
                        grid_line = True
                        grid_mode_button.changeColor(setting_mouse_pos)
        pygame.display.update()
        clock.tick(60)
            
def intro(time_stop):
    time_cur = 0
    intro_video.set_sound()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                intro_video.close()
                background_sound.play(-1)
                main_menu()

        intro_video.draw(screen, (0, 0), scale=1000)
        pygame.display.update()
        
        time_cur += 1
        if time_stop * FPS_VIDEO == time_cur:
            intro_video.close()
            background_sound.play(-1)
            main_menu()
        
        clock.tick(FPS_VIDEO)

# pos_x = pygame. / 2 - window_width / 2
# pos_y = screen_height - window_height
# os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon_image = pygame.image.load("./images/logo.png")
menu_background_image = pygame.image.load("./images/background/air (2).png")
mm_background_image = pygame.image.load('./images/background/air (1).png')
sd_background_image = pygame.image.load('./images/background/air (3).png')
setting_background_image = pygame.image.load("./images/background/air (4).png")

intro_video = Video('./videos/intro.mp4', './musics/intro.mp3')

pygame.display.set_caption("Create Models Tool - LTP Hieu")
pygame.display.set_icon(icon_image)
clock = pygame.time.Clock()
app_active = True

main_menu_sound = pygame.mixer.Sound("./musics/RapidAW.mp3")
monster_mash_sound = pygame.mixer.Sound("./musics/yoimiya.mp3")
mini_paint_sound = pygame.mixer.Sound("./musics/Im still alive today.mp3")
background_sound = pygame.mixer.Sound("./musics/maou_bgm_piano26.mp3")

intro(5.1)
