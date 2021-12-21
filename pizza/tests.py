from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def test_there_is_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.page_source)

    def testDown(self):
        self.browser.quit()
