from src.logger import CustomLogger
from src.driver_setup import DriverSetup
from src.pages.basketball_page import BasketballPage
from src.pages.home_page import HomePage
from src.utils import sleep


class Bet365App:
    def __init__(self) -> None:
        self.logger = CustomLogger('bet365')
        self.driver_setup = DriverSetup(logger=self.logger)
        self.driver = self.driver_setup.driver
        self.home_page = HomePage(self.driver, self.logger)
        self.basketball_page = BasketballPage(self.driver, self.logger)

    def run_home_page(self):
        self.home_page.send_request()
        sleep()
        
        self.home_page.click_basketball_page()
        sleep()

    def run_basketball_page(self):
        self.basketball_page.click_nba_panel()
        sleep()

        self.basketball_page.click_player_props()
        sleep()

        self.basketball_page.click_player_points()
        sleep()

    def close(self):
        self.driver_setup.close_driver()


def main():
    app = Bet365App()

    try:
        CustomLogger.log_start_time()
        app.run_home_page()
        app.run_basketball_page()

    except Exception as err:
        raise Exception(f'An error occurred: {str(err)}')
    except KeyboardInterrupt:
        app.logger.info(f'Keyboard interrupt')
        app.close()
    finally:
        app.close()

    CustomLogger.log_end_time()


if __name__ == "__main__":
    main()