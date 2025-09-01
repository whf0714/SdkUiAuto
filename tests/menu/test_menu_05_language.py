import unittest
import time
from pages.menu_page import MenuPage
from tests.menu.test_menu_public import TestPublicMenu
from datetime import datetime



class TestMenuLanguage(TestPublicMenu):


    def test_language_01_en(self):
        """验证切换语言_English"""
        automation_id="WorkingModeFastRbt"
        language_action = lambda: self.menu_page.click_language("English")
        self.verify_language_element_name(language_action, "Fast","click_language_en",automation_id)

    def test_language_02_zh(self):
        """验证切换语言_中文"""
        automation_id = "WorkingModeFastRbt"
        language_action = lambda: self.menu_page.click_language("中文")
        self.verify_language_element_name(language_action, "快速", "click_language_zh", automation_id)

