from selenium import webdriver


class SeleniumWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, host="http://phptravels.net/admin"):
        self.driver = webdriver.Chrome()
        self.base_url = host
        return self.driver