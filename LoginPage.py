from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_FIELD_LOCATION = "//a[@class='horizontal-menu__link'][@href='https://omgtu.ru/ecab/']"
    _FIELD_LOCATION = "//a[@class='horizontal-menu__link'][@href='https://omgtu.ru/ecab/']"
    LOGIN_FIELD_LOCATION = "//a[@class='horizontal-menu__link'][@href='https://omgtu.ru/ecab/']"
    def __init__(self, driver):
        self.driver = driver
    def clickContactButton(self):
        self.driver.find_element(By.XPATH, self.CONTACT_BUTTON_LOCATION).click()