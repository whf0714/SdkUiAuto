import unittest
import time
from pages.menu_page import MenuPage
from tests.menu.test_menu_public import TestPublicMenu
from datetime import datetime



class TestMenuLanguage(TestPublicMenu):

    def test_language_01_en(self):
        """验证切换语言_English"""
        automation_id="WorkingModeFastRbt"
        element_name = self.menu_page.get_element_name(automation_id)
        # 测试前置条件：确保设备处于中文语言环境下 如果元素名称是英文的"Fast"，说明当前是英文环境，需要切换到中文
        if element_name == "Fast":
            print("当前是英文环境，正在切换到中文...")
            # 从英文切换到中文
            self.menu_page.click_language("中文")
            # 等待语言切换完成
            time.sleep(1)
            print("已切换到中文环境")
        elif element_name == "快速":
            # print("当前已处于中文环境")
            pass
        language_action = lambda: self.menu_page.click_language("English")
        self.verify_language_element_name(language_action, "Fast","click_language_en",automation_id)

    def test_language_02_zh(self):
        """验证切换语言_中文"""
        automation_id = "WorkingModeFastRbt"
        language_action = lambda: self.menu_page.click_language("中文")
        self.verify_language_element_name(language_action, "快速", "click_language_zh", automation_id)

