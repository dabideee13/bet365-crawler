from typing import Optional
from logging import Logger

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By

from src.utils import sleep


class BasePage:

    def __init__(self, driver: WebDriver, logger: Optional[Logger] = None) -> None:
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 30)
        self.sleep = sleep

    def click(self, by_locator: tuple[By, str], driver: Optional[WebDriver] = None) -> None:
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator: tuple[By, str], text: str):
        return self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def check_presence(self, by_locator: tuple[By, str], driver: Optional[WebDriver] = None) -> None:
        self.wait.until(EC.presence_of_element_located(by_locator))

    def select_value(self, by_locator: tuple[By, str], value: str) -> None:
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        Select(element).select_by_value(value)

    def select_text(self, by_locator: tuple[By, str], text: str) -> None:
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        Select(element).select_by_visible_text(text)

    def extract_links(self, by_locator: tuple[By, str]) -> list[str]:
        selectors = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        return [selector.get_attribute('href') for selector in selectors]

    def extract_data(self, by_locator: tuple[By, str]) -> str:
        selector = self.wait.until(EC.presence_of_element_located(by_locator))
        return selector.text

    def extract_multiple_data(self, by_locator: tuple[By, str]) -> list[str]:
        selectors = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        return [selector.text for selector in selectors]