from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""test123test"""
class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_email_login(self, email):
        self.driver.find_element_by_xpath('//input[@name="UserEmail"]').send_keys(email)

    def enter_password_login(self, password):
        self.driver.find_element_by_xpath('//input[@name="Password"]').send_keys(password)

    def enter_button_login(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        button.click()

    def message_wrong_login(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Email or Password is invalid"]')))

    def forgot_password(self):
        self.driver.find_element_by_xpath('//span[text()="Forgot your password?"]').click()

    def recovery_link(self, email):
        elem = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="UserName"]')))
        elem.send_keys(email)

    def send_recovery_link(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Send recovery link"]/parent::button')))
        button.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="We have sent you a recovery link to the address"]')))

    def return_to_login_section(self):
        button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="success-sent-return"]')))
        button.click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Password"]')))

    def wait_main_page(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Clients"]')))





