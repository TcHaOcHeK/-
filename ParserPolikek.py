from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from MainPage import MainPage

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://omgtu.ru/")

# mainPage = MainPage(driver)
#
# mainPage.clickContactButton()


time.sleep(2)
menu = driver.find_element(By.XPATH, "//i[@class='mobile-nav__burger fa-solid fa-bars']")
menu.click()
time.sleep(1)
personalAccount = driver.find_element(By.XPATH, "/html/body/div/div/header/div[3]/div[4]/div/div[1]/ul/li[3]")
personalAccount.click()
time.sleep(1)
accountLogin = driver.find_element(By.XPATH, "//input[@name='USER_LOGIN']")
accountLogin.send_keys("Timofei_Tishchenko_9175")
accountPassword = driver.find_element(By.XPATH, "//input[@name='USER_PASSWORD']")
accountPassword.send_keys("84856b23")
regButton = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[2]/div/div[3]/div[3]/div[2] ")
regButton.click()
time.sleep(1)
addMenu = driver.find_element(By.XPATH, "//html/body/div/div/main/div/div[2]/div[2]/div/div[1]")
addMenu.click()
time.sleep(1)
loadWorks = driver.find_element(By.XPATH, "//a[@class='sidebar-menu__link'][@href='/ecab/vkr2.php']")
loadWorks.click()

time.sleep(5)
driver.quit()


