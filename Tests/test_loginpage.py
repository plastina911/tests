import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.loginpage import Login
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test_Login(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://jgtest.immigrationforms.net/"
        self.driver.maximize_window()


    def test_login_staff(self):
        driver = self.driver
        driver.get(self.base_url)
        login = Login(driver)
        login.enter_email_login("owner9km.test@gmail.com")
        login.enter_password_login("Test123$")
        login.enter_button_login()
        login.wait_main_page()
        self.assertIn("ZONTLAW", driver.title)

    def test_login_wrong_1(self):
        driver = self.driver
        driver.get(self.base_url)
        login = Login(driver)
        login.enter_email_login("tut@gmail.com")
        login.enter_button_login()
        login.message_wrong_login()
        assert ("Email or Password is invalid") in driver.page_source

    def test_login_wrong_2(self):
        driver = self.driver
        driver.get(self.base_url)
        login = Login(driver)
        login.enter_password_login(123)
        login.enter_button_login()
        login.message_wrong_login()
        assert ("Email or Password is invalid") in driver.page_source

    def test_forgot_password(self):
        driver = self.driver
        driver.get(self.base_url)
        login = Login(driver)
        login.forgot_password()
        login.recovery_link("owner9km.test@gmail.com")
        login.send_recovery_link()
        login.return_to_login_section()
        assert ("Sign in") in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
