from src.pages.base_page import BasePage
from src.urls import BASKETBALL_PAGE_URL
from src.locators import BasketBallPageLocators


class BasketballPage(BasePage):
    
    def send_request(self) -> None:
        try:
            self.logger.info(f'Sending request to {BASKETBALL_PAGE_URL}')
            self.driver.get(BASKETBALL_PAGE_URL)
        
        except Exception as err:
            self.logger.error(f'Failed to send request to {BASKETBALL_PAGE_URL}: {str(err)}')
            self.driver.quit()

    def click_nba_panel(self) -> None:
        self.logger.info('Clicking on NBA')
        self.click(BasketBallPageLocators.NBA_PANEL)

    def click_player_props(self) -> None:
        self.logger.info('Clicking on Player Props')
        self.click(BasketBallPageLocators.PLAYER_PROPS_PANEL)

    def click_player_points(self) -> None:
        self.logger.info('Clicking on Player Points')
        self.click(BasketBallPageLocators.PLAYER_POINTS_PAGE)