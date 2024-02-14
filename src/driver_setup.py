import time
from typing import Optional
from logging import Logger

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from src import settings


class DriverSetup:

    def __init__(self, max_retries: int = 5, wait_time: int = 10, logger: Optional[Logger] = None) -> None:
        self.logger = logger
        self.max_retries = max_retries
        self.wait_time = wait_time
        self.driver = self.create_driver()

    def create_driver(self) -> WebDriver:
        self.logger.info(f'Initializing driver')

        for retry_count in range(self.max_retries):
            try:
                chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument('--headless')

                # chrome_options.add_argument(f'user-agent={settings.USER_AGENT}')
                chrome_options.add_argument('--start-fullscreen')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--window-size=1920,1080')
                chrome_options.add_argument('--ignore-certificate-errors')

                driver = webdriver.Chrome(
                    service=Service(executable_path=ChromeDriverManager().install()),
                    options=chrome_options
                )
                driver.wait = WebDriverWait(driver, self.wait_time)
                return driver

            except Exception as err:
                self.logger.error(f'Failed to initialize WebDriver (Attempt {retry_count + 1}/{self.max_retries}): {str(err)})')
                if retry_count < self.max_retries - 1:
                    time.sleep(self.wait_time)
                else:
                    raise

    def close_driver(self) -> None:
        self.logger.info('Closing WebDriver')
        self.driver.quit()