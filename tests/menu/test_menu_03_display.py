import unittest
import time
from pages.menu_page import MenuPage
from tests.menu.test_menu_public import TestPublicMenu
from datetime import datetime

#####没有断言

class TestMenuDisplay(TestPublicMenu):


    def test_display_01_full_screen(self):
        """验证进入全屏/ 退出全屏"""
        self.menu_page.toggle_run_status()  # 设备切换为运行状态
        self.menu_page.trigger_camera()  # 触发一次拍摄
        self.menu_page.click_display("进入全屏 / 退出全屏")
        self.menu_page.click_display("进入全屏 / 退出全屏")
        self.menu_page.click_display("进入全屏 / 退出全屏")

    def test_display_02_rotation(self):
        """验证开启旋转 / 关闭旋转"""
        self.menu_page.click_display("开启旋转 / 关闭旋转")
        self.menu_page.click_display("开启旋转 / 关闭旋转")

    def test_display_03_auto_color_depth_range(self):
        """验证执行自动色谱范围"""
        self.menu_page.click_display("执行自动色谱范围")

    def test_display_04_tile_display(self):
        """验证开启 / 关闭平铺显示"""
        self.menu_page.click_display("开启 / 关闭平铺显示")
        self.menu_page.click_display("开启 / 关闭平铺显示")

    def test_display_05_shortcut_f6(self):
        """验证快捷键 F6 - 进入全屏/ 退出全屏"""
        self.menu_page.preset_shortcut('F6')
        self.menu_page.preset_shortcut('F6')
        self.menu_page.preset_shortcut('F6')

    def test_display_06_shortcut_f7(self):
        """验证快捷键 F7 - 开启旋转 / 关闭旋转"""
        self.menu_page.preset_shortcut('F7')
        self.menu_page.preset_shortcut('F7')

    def test_display_07_shortcut_f8(self):
        """验证快捷键 F8 - 执行自动色谱范围"""
        self.menu_page.preset_shortcut('F8')
