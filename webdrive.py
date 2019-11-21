# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Chrome_Open_Page(driver, html_path):
    driver.get(html_path)

def Chrome_Init(app_path):
    opts = Options()
    opts.add_argument("--disable-infobars")
    opts.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(executable_path = app_path, options=opts)
    return driver

#def Chrome_Screenshot():
#    driver.get(url)
#    time.sleep(5)
#    driver.save_screenshot(out)

class Webdriver:
    service: None
    driver: webdriver.chrome.webdriver.WebDriver
    options: Options
    website: str
    
    def __init__(self, service=None, path='chromedriver', options=[]):
        opts = Options()
        if isinstance(options, str):
            options = [options]
        
        if isinstance(options, list):
            for i in options:
                opts.add_argument(i)
        else:
            return None
        
        self.options = opts
        if isinstance(service, Service):
            self.service = service
            self.driver = webdriver.Remote(service.service_url, options=opts)
        else:
            self.driver = webdriver.Chrome(executable_path=path, options=opts)
    
    def open(self, website):
        self.website = website
        self.driver.get(website)
    
    def get_website(self):
        return self.website
    
    def check_condition(self, input_list, input_type='class'):
        if input_type == 'class':
            by_obj = By.CLASS_NAME
        elif input_type == 'id':
            by_obj = By.ID
        if isinstance(input_list, str):
            input_list = [input_list]
            
        item_available = False
        break_counter = 0
        while not(item_available) and break_counter < 3:
            for i in input_list:
                try:
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((by_obj, i))
                    )
                    item_available = True
                except:
                    item_available = False
                if not(item_available):
                    break
            break_counter += 1
            
        return item_available

    def screenshot(self, path):
#        self.driver.save_screenshot(path)
        self.driver.get_screenshot_as_file(path)