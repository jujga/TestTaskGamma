import pytest
from selenium import webdriver
from webdriver_manager import firefox
from selenium.webdriver.common.by import By
from time import sleep
from enum import Enum


class WebElements(Enum):
    USERNAME_FIELD = (By.ID, "_username")
    USERPASSWORD_FIELD = (By.ID, "_password")
    SE_BUTTON = (By.XPATH,"//button[@class='primary large']")
    TALENTS_LINK = (By.XPATH, "//li[@data-testid = 'TEACandidatesListLink']")
    ADD_BUTTON = (By.XPATH, "//app-ui-button-text[@id = 'candidates-list_add-candidate-button']/button[@class='primary large']")
    CHEF_BUTTON = (By.XPATH,'//troops-selector[@class="ng-star-inserted"]')
    POPUP_TITLE = (By.XPATH, "//div[contains(@class,'text') and contains(@class,'ng-tns')]")

    def __init__(self, location_strategy, locator):
        self.location_strategy = location_strategy
        self.locator = locator

    def get_web_el(self, driver):
        return driver.find_element(self.location_strategy, self.locator)

    def get_web_els(self, driver):
        return driver.find_elements(self.location_strategy, self.locator)


class Credentials:
    username = 'interim_director0@troops.online'
    userpassword = 'interim_director0@troops.online'

@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox(executable_path=firefox.GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.close()

def test_adding_talants_title(firefox_driver):
    class ExpectedResults:
        popup_title = 'Add talents'
    firefox_driver.get('https://app-dev.troops.online/')
    #fill Credentials
    WebElements.USERNAME_FIELD.get_web_el(firefox_driver).send_keys(Credentials.username)
    WebElements.USERPASSWORD_FIELD.get_web_el(firefox_driver).send_keys(Credentials.userpassword)
    # click on the Se connecter button
    WebElements.SE_BUTTON.get_web_el(firefox_driver).click()
    #click on the Talents link. Sometimes test is failed. sleep(1) helps.
    WebElements.TALENTS_LINK.get_web_el(firefox_driver).click()
    #click on the Add button
    WebElements.ADD_BUTTON.get_web_el(firefox_driver).click()
    #click on the Chef actuel
    WebElements.CHEF_BUTTON.get_web_els(firefox_driver)[0].click()
    assert WebElements.POPUP_TITLE.get_web_els(firefox_driver)[0].text == ExpectedResults.popup_title, 'Заголовок окна выбора способа добавления талантов не совпал'


