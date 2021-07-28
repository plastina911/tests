import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class Note:
    def __init__(self, driver):
        self.driver = driver

    def create_note_top_menu(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="navbar-right"]//li[4]')))
        button.click()

    def create_note_left_menu(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#/notes"]')))
        button.click()

    def note_title(self, note_title):
        self.driver.find_element_by_xpath('//textarea[@placeholder="Note Title..."]').send_keys(note_title)

    def note_text(self, note_text):
        self.driver.find_element_by_xpath('//textarea[@placeholder="Note Text..."]').send_keys(note_text)

    def add_client(self, client):
        self.driver.find_element_by_xpath('//div[@class="position-relative"]//button[4]').click()
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="off"]')))
        elem.send_keys(client)
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//ul[@role="listbox"]//li[3]')))
        elem.click()

    def add_phone(self):
        self.driver.find_element_by_xpath('//div[@class="position-relative"]//button[5]').click()
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Start Recording"]')))
        elem.click()

    def pinned_note(self):
        self.driver.find_element_by_xpath('//div[@class="position-relative"]//button[1]').click()

    def pinned_page(self):
        self.driver.find_element_by_xpath('//div[text()="Pinned"]').click()
        time.sleep(5)

    def add_file(self):
        self.driver.find_element_by_xpath('//div[@class="position-relative"]//button[3]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text()=" upload here"]')))
        self.driver.find_element_by_xpath('//input[@type="file"]').send_keys('C:/Users/User/Documents/Lightshot/Screenshot_01.png')
        time.sleep(2)

    def add_color(self):
        self.driver.find_element_by_xpath('//div[@class="position-relative"]//button[7]').click()
        self.driver.find_element_by_xpath('//div[@class="color-inside fef6e9"]').click()

    def open_check_list(self):
        self.driver.find_element_by_xpath('//div[@class="position-relative"]//button[8]').click()

    def fill_in_check_list(self):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Check List Group"]')))
        elem.click()
        self.driver.find_element_by_xpath('//input[@placeholder="Check List Group"]').send_keys("Test123")

    def open_check_list_item(self):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Add Check List Item"]')))
        elem.click()

    def chek_item(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class ="ant-col ant-col-1"]/label/span')))
        self.driver.find_element_by_xpath('//div[@class ="ant-col ant-col-1"]/label/span').click()

    def fill_in_check_list_item(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Check List Item"]')))
        self.driver.find_element_by_xpath('//input[@placeholder="Check List Item"]').send_keys("qwerty")
        self.driver.find_element_by_xpath('//input[@placeholder="Check List Item"]').click()

    def save_note(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Save Note"]/parent::button[@type="button"]')))
        button.click()
        time.sleep(5)

    def check_save_note(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#/notes"]')))
        button.click()
        time.sleep(10)






