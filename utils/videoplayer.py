import cv2
import numpy as np
import pygame

class Video:
    def __init__(self, path, path_sound=None):
        self.path = path
        if path_sound is not None:
            self.path_sound = path_sound
            self.sound = pygame.mixer.Sound(path_sound)
        else:
            pass
        self.cap = cv2.VideoCapture(self.path)

    def draw(self, win, pos, loop=False, scale=100):
        ret, frame = self.cap.read()

        if ret:
            # Convert the frame to a Pygame surface
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame, 3)
            frame = np.fliplr(frame)
            frame = pygame.surfarray.make_surface(frame)

            # Draw the frame on the screen
            win.blit(frame, pos)
        elif loop is True:
            self.cap = cv2.VideoCapture(self.path)
            ret, frame = self.cap.read()
        else:
            self.cap.release()

    def set_sound(self, loop=False, mute=False):
        if self.path_sound is not None:
            if mute is False:
                self.sound.play(-1 if loop is True else 1)
            else:
                pass
        else:
            pass
    
    def close(self):
        if self.path_sound is not None:
            self.sound.stop()
        else:
            pass
        self.cap.release()
