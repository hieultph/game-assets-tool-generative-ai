import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from .settings import *

import os
cmd = "wmic path Win32_VideoController get CurrentVerticalResolution,CurrentHorizontalResolution"
size_tuple = tuple(map(int,os.popen(cmd).read().split()[-2::]))

class GoogleColab:
    def __init__(self):
        self.options = uc.ChromeOptions()
        # self.options.headless=True
        # self.options.add_argument('--headless')
        self.options.add_argument("--disable-renderer-backgrounding")
        self.options.add_argument("--disable-backgrounding-occluded-windows")
        # options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"')
        # if headless is True: self.options.add_argument('--headless')
        self.options.add_argument(f"--window-size={WIDTH},{HEIGHT}") 
        self.driver = uc.Chrome(options=self.options)
        self.driver.set_window_size(WIDTH + 50, HEIGHT + 50)
        self.driver.set_window_position(size_tuple(0) // 2 - (WIDTH // 2) - 25, size_tuple(1) // 2 - (HEIGHT // 2) - 40)
        #self.driver.set_window_position(GetSystemMetrics(0) // 2 - (WIDTH // 2) - 25, GetSystemMetrics(1) // 2 - (HEIGHT // 2) - 40)
        self.actions = ActionChains(self.driver)
        self.link_ui = None
        
    def signin_manual(self):
        self.driver.get('https://accounts.google.com/')
        self.driver.implicitly_wait(300)
        self.driver.find_element(By.XPATH, '//div[3]/div/div/header/h1')
            
    
    def signin(self, email, password):
        self.driver.get('https://accounts.google.com/')
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.XPATH, '//input[@id="identifierId"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//div[@id="identifierNext"]/div/button/span').click()

        self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()

    def run_gc_by_link(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(10)

        self.actions.key_down(Keys.CONTROL).perform()
        self.actions.send_keys(Keys.F9).perform()
        self.actions.key_up(Keys.CONTROL).perform()

        self.driver.find_element(By.XPATH, '/html/body/mwc-dialog/mwc-button[2]').click()

        self.driver.implicitly_wait(6000)
        self.link_ui = self.driver.find_element(By.XPATH, '//pre/a[contains(@href, "gradio.app")]').get_attribute("href")
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//pre/a[contains(@href, "gradio.app")]').click()
    
    def open_link(self, link):
        self.driver.get(link)
    
    def close(self):
        self.driver.close()

def main_run_automate():
    gcolab = GoogleColab()
    gcolab.signin("sprclot@gmail.com", "Hieu748664")
    time.sleep(5)
    gcolab.run_gc_by_link("https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/openjourney_v2_diffusion_webui_colab.ipynb")
    if gcolab.link_ui is not None:
        print(gcolab.link_ui)
    else:
        print("Time out")
    time.sleep(1000)

if __name__ == "__main__":
    main_run_automate()

        