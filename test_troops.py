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
    driver.close()

def test_login(firefox_driver):
    firefox_driver.maximize_window()
    firefox_driver.implicitly_wait(5)
    firefox_driver.get('https://app-dev.troops.online/')
    #firefox_driver.find_element(By.ID,'_username').send_keys('interim_director0@troops.online')
    WebElements.USERNAME_FIELD.get_web_el(firefox_driver).send_keys(Credentials.username)
    #firefox_driver.find_element(By.ID,'_password').send_keys('interim_director0@troops.online')
    WebElements.USERNAME_FIELD.get_web_el(firefox_driver).send_keys(Credentials.userpassword)
    firefox_driver.find_element(By.XPATH,"//button[@class='primary large']").click()
    sleep(3)
    firefox_driver.find_element(By.XPATH, "//li[@data-testid = 'TEACandidatesListLink']").click()
    firefox_driver.find_element(By.XPATH, "//app-ui-button-text[@id = 'candidates-list_add-candidate-button']/button[@class='primary large']").click()
    firefox_driver.find_elements(By.XPATH,'//troops-selector[@class="ng-star-inserted"]')[0].click()
    assert \
        firefox_driver.find_elements(By.XPATH,
                                        "//div[contains(@class,'text') and contains(@class,'ng-tns-c545-1')]")[0].text, 'Add talents'


