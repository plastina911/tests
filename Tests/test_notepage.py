import random
import unittest
from selenium import webdriver
from test_loginpage import Test_Login
from PageObjects.notepage import Note
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test_Note(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome
        Test_Login.setUp(self)
        Test_Login.test_login_staff(self)

    def test_create_note_top_menu(self):
        driver = self.driver
        note = Note(driver)
        note.create_note_top_menu()
        n = random.randint(100, 1000000)
        note.note_title("Test" + str(n))
        note.save_note()

    def test_create_note_top_menu_with_client(self):
        driver = self.driver
        note = Note(driver)
        note.create_note_top_menu()
        note.add_client("Lena")
        n = random.randint(1000, 1000000)
        note.note_title("Test" + str(n))
        note.note_text("Test" + str(n))
        note.save_note()

    def test_create_note_top_menu_with_check_list(self):
        driver = self.driver
        note = Note(driver)
        note.create_note_top_menu()
        note.note_title("Test")
        note.open_check_list()
        note.fill_in_check_list()
        note.open_check_list_item()
        note.fill_in_check_list_item()
        note.chek_item()
        note.open_check_list_item()
        note.fill_in_check_list_item()
        note.save_note()

    def test_create_note_left_menu_with_client(self):
        driver = self.driver
        note = Note(driver)
        note.create_note_left_menu()
        note.add_file()
        n = random.randint(100, 1000000)
        note.note_title("Test" + str(n))
        note.note_text("Test12")
        note.add_client("Dasha")
        note.save_note()
        assert "Test12" in driver.page_source

    def test_create_note_pinned(self):
        driver = self.driver
        note = Note(driver)
        note.create_note_left_menu()
        n = random.randint(100, 1000000)
        note.note_title("Test" + str(n))
        note.pinned_note()
        note.note_text("Test71")
        note.save_note()
        note.pinned_page()
        assert "Test71" in driver.page_source

    def test_crete_note_with_color(self):
        driver = self.driver
        note = Note(driver)
        note.create_note_top_menu()
        note.add_color()
        n = random.randint(100, 1000000)
        note.note_title("Test" + str(n))
        note.save_note()

    def test_create_note_with_phone(self):
        driver = self.driver
        note = Note(driver)
        note.create_note_top_menu()
        note.note_title("Test")
        note.add_phone()




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()




