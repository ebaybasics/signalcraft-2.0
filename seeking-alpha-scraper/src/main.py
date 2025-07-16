# main.py

from scraper.selenium_driver import SeleniumDriver
from scraper.seeking_alpha_scraper import SeekingAlphaScraper
from config.settings import USERNAME, PASSWORD

def main():
    # Initialize the Selenium driver
    driver = SeleniumDriver()
    driver.setup()

    try:
        # Create an instance of the SeekingAlphaScraper
        scraper = SeekingAlphaScraper(driver)
        
        # Log in to Seeking Alpha
        scraper.login(USERNAME, PASSWORD)
        
        # Scrape the desired analysis data
        analysis_data = scraper.scrape_analysis()
        
        # Process or save the analysis data as needed
        print(analysis_data)

    finally:
        # Teardown the Selenium driver
        driver.teardown()

if __name__ == "__main__":
    main()