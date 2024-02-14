from selenium.webdriver.common.by import By


class HomePageLocators:
    BASKETBALL_PAGE = (By.XPATH, '//span[@class="wn-PreMatchItem_Text" and text() = "Basketball"]')


class BasketBallPageLocators:
    NBA_PANEL = (By.XPATH, '//div[@class="sm-SplashMarketGroupButton "]/div[text() = "NBA"]') 
    PLAYER_PROPS_PANEL = (By.XPATH, '//div[@class="sm-SplashMarket " and @role="button"]/div/div[text() = "Player Props"]')
    PLAYER_POINTS_PAGE = (By.XPATH, '//div[@class="sm-CouponLink " and @role="link"]/span[text() = "Player Points"]')