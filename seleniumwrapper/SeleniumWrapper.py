from selenium import webdriver


class SeleniumWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs): # setting wrapper instance
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, host="http://phptravels.com/demo"): # connecting to the base page, driver and window maximizing
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = host
        return self.driver