from src.pages.base_page import BasePage
from src.urls import HOME_PAGE_URL
from src.locators import HomePageLocators


class HomePage(BasePage):
    
    def send_request(self) -> None:
        try:
            self.logger.info(f'Sending request to {HOME_PAGE_URL}')
            self.driver.get(HOME_PAGE_URL)
        
        except Exception as err:
            self.logger.error(f'Failed to send request to {HOME_PAGE_URL}: {str(err)}')
            self.driver.quit()

    def click_basketball_page(self) -> None:
        self.logger.info('Clicking basketball page')
        self.click(HomePageLocators.BASKETBALL_PAGE)