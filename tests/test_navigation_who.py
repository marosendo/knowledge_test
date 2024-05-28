# tests/test_navigationWho.py

import unittest
from config.config import get_driver
from main import navigate_menus
from main import readParagraph

class TestNavigationWho(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_navigation(self):
        #browse the web and go to "Who we are"
        navigate_menus(self.driver,"//a[normalize-space()='Who we are'][1]")
        #extract paragraphs from "Who we are"
        readParagraph(self.driver)

if __name__ == "__main__":
    unittest.main()
