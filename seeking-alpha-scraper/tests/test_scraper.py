import unittest
from src.scraper.selenium_driver import SeleniumDriver
from src.scraper.seeking_alpha_scraper import SeekingAlphaScraper

class TestSeekingAlphaScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumDriver()
        cls.scraper = SeekingAlphaScraper(cls.driver)

    def test_login(self):
        result = self.scraper.login('your_username', 'your_password')
        self.assertTrue(result)

    def test_scrape_analysis(self):
        self.scraper.login('your_username', 'your_password')
        analysis_data = self.scraper.scrape_analysis('some_ticker')
        self.assertIsNotNone(analysis_data)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()