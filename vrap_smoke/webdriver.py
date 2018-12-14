from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Driver:

    def __init__(self):
        # self.instance = webdriver.Chrome()
        opts = Options()
        opts.headless = True
        self.instance = webdriver.Firefox(options = opts) #need to add geckodriver to root dir

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)

        else:
            raise TypeError('URL must be a string')
