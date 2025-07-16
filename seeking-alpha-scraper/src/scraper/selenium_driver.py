class SeleniumDriver:
    def __init__(self, options=None):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        self.options = options if options else webdriver.ChromeOptions()
        self.driver = None

    def initialize_driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def teardown_driver(self):
        if self.driver:
            self.driver.quit()