from  selenium import webdriver
from webdriver_manager import firefox
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from enum import Enum
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElements(Enum):
    USERNAME_FIELD = (By.ID, "_username")
    USERPASSWORD_FIELD = (By.ID, "_password")
    SE_BUTTON = (By.XPATH,"//button[@class='primary large']")
    TALENTS_LINK = (By.XPATH, "//li[@data-testid = 'TEACandidatesListLink']")
    POPUP_TITLE = (By.XPATH, "//div[contains(@class,'text') and contains(@class,'ng-tns')]")
    def __init__(self, location_strategy, locator):
        self.location_strategy = location_strategy
        self.locator = locator

    def get_web_el(self, driver):
        return driver.find_element(self.location_strategy, self.locator)

class Credentials:
    username = 'interim_director0@troops.online'
    userpassword = 'interim_director0@troops.online'

@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox(executable_path=firefox.GeckoDriverManager().install())
    yield driver
    #driver.close()

def test_login(firefox_driver):
    firefox_driver.maximize_window()
    firefox_driver.implicitly_wait(5)
    firefox_driver.get('https://app-dev.troops.online/')
    #fill Credentials
    WebElements.USERNAME_FIELD.get_web_el(firefox_driver).send_keys(Credentials.username)
    WebElements.USERPASSWORD_FIELD.get_web_el(firefox_driver).send_keys(Credentials.userpassword)
    WebElements.SE_BUTTON.get_web_el(firefox_driver).click() #click on the Se connecter button
    #click on the Talents link
    WebElements.TALENTS_LINK.get_web_el(firefox_driver).click()
    #click on the Add button
    firefox_driver.find_element(By.XPATH, "//app-ui-button-text[@id = 'candidates-list_add-candidate-button']/button[@class='primary large']").click()
    #click on the Chef actuel
    firefox_driver.find_elements(By.XPATH,'//troops-selector[@class="ng-star-inserted"]')[0].click()
    assert WebElements.POPUP_TITLE.get_web_el(firefox_driver)[0].text, 'Add talents'


