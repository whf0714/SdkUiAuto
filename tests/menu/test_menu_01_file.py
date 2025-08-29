import unittest
import time
from pages.menu_page import MenuPage
from tests.menu.test_menu_public import TestPublicMenu
from datetime import datetime
now = datetime.now().strftime("%Y%m%d%H%M%S")

class TestMenuFile(TestPublicMenu):
    def test_file_01_load_data(self):
        """验证导入数据并弹窗提示"""
        data_name = "testData.mpdat"
        load_action = lambda: self.menu_page.load_data(data_name)
        self.verify_text_prompt(load_action, "数据导入成功", "load_data")

    def test_file_02_load_settings(self):
        """验证导入设置并弹窗提示"""
        file_name = "SizectorS_Settings.mpset"
        load_action = lambda: self.menu_page.load_settings(file_name)
        self.verify_text_prompt(load_action, "载入设置文件成功", "load_setting")

    def test_file_03_save_data(self):
        """验证保存数据并弹窗提示"""
        file_name = "UI_DataExport_"+now+".mpdat"
        file_action = lambda: self.menu_page.save_data(file_name)
        self.verify_text_prompt(file_action, "数据导出成功", "save_data")

    def test_file_04_point_cloud_format_export(self):
        """验证保存设置并弹窗提示"""
        file_name = "UI_PointCloudExport_" + now + ".ply"
        file_action = lambda: self.menu_page.save_point_cloud_format(file_name)
        self.verify_text_prompt(file_action, "点云导出成功", "point_cloud_format_export")

    def test_file_05_save_settings(self):
        """验证保存设置并弹窗提示"""
        file_name = "UI_Settings_"+now+".mpset"
        file_action = lambda: self.menu_page.save_settings(file_name)
        self.verify_text_prompt(file_action, "设置文件保存成功", "save_settings")

    def test_file_06_save_2d_snapshot(self):
        """验证保存二维截图并弹窗提示"""
        file_name = "UI_Snapshot_"+now+".bmp"
        file_action = lambda: self.menu_page.save_2d_snapshot(file_name)
        self.verify_text_prompt(file_action, "保存截图成功", "save_2d_snapshot")

    def test_file_07_save_gif(self):
        """验证保存动图并弹窗提示"""
        file_name = "UI_GifExport_"+now+".gif"
        file_action = lambda: self.menu_page.save_gif(file_name)
        self.verify_text_prompt(file_action, "动图已生成", "save_gif", timeout=60)

    def test_file_08_save_all(self):
        """验证保存所有文件并弹窗提示"""
        file_name = "UI_SaveFile_"+now
        file_action = lambda: self.menu_page.save_all_file(file_name)
        self.verify_save_all_prompt(file_action, "保存成功", "save_all", timeout=60)
