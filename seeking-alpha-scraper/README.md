# Seeking Alpha Scraper

This project is a web scraper designed to extract analysis data from the Seeking Alpha website using Selenium. It automates the login process and retrieves the desired information for further analysis.

## Project Structure

```
seeking-alpha-scraper
├── src
│   ├── main.py                # Entry point for the scraper application
│   ├── scraper
│   │   ├── __init__.py        # Marks the scraper directory as a package
│   │   ├── selenium_driver.py  # Manages the Selenium WebDriver setup and teardown
│   │   └── seeking_alpha_scraper.py  # Contains methods for logging in and scraping data
│   ├── config
│   │   ├── __init__.py        # Marks the config directory as a package
│   │   └── settings.py        # Configuration settings including credentials
│   └── utils
│       ├── __init__.py        # Marks the utils directory as a package
│       └── helpers.py         # Utility functions for data processing and formatting
├── tests
│   ├── __init__.py            # Marks the tests directory as a package
│   └── test_scraper.py        # Unit tests for the scraper functionality
├── requirements.txt           # Lists project dependencies
├── .env.example               # Example of environment variables needed for the project
├── .gitignore                 # Specifies files and directories to ignore by Git
└── README.md                  # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd seeking-alpha-scraper
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables by copying `.env.example` to `.env` and filling in the necessary credentials.

## Usage

To run the scraper, execute the following command:
```
python src/main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.