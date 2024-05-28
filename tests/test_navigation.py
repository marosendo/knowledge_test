# tests/test_navigation.py

import unittest
from config.config import get_driver
from main import navigate_menus
from main import readParagraph

class Test_Navigation(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_navigation(self):
        #browse the web and go to "Home"
        navigate_menus(self.driver,"//a[normalize-space()='Home'][1]")
        #extract paragraphs from "Home"
        readParagraph(self.driver)

if __name__ == "__main__":
    unittest.main()
