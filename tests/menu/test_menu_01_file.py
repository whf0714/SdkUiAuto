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
        """验证保存点云格式数据并弹窗提示"""
        file_name = "UI_PointCloudExport_" + now + ".ply"
        file_action = lambda: self.menu_page.save_point_cloud_format(file_name)
        self.verify_text_prompt(file_action, "点云导出成功", "point_cloud_format_export")

    def test_file_05_save_settings(self):
        """验证保存设备设置并弹窗提示"""
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

    def test_file_09_expert_setting_enable(self):
        """验证启用专业设置并弹窗提示"""
        self.verify_text_prompt(lambda: self.menu_page.enable_expert_setting(), "专业设置可能会影响设备正常工作, 需要谨慎使用!", "enable_expert_setting")

    def test_file_10_expert_setting_disable(self):
        """验证启用专业设置并弹窗提示"""
        self.menu_page.enable_expert_setting()


class TestMenuFileException(TestPublicMenu):
    """测试文件操作在设备运行状态下的异常场景"""

    def test_file_exception_01_load_data(self):
        """验证在设备运行状态下导入数据的异常提示"""
        self.menu_page.toggle_run_status() #测试前置条件：将设备切换到运行状态
        self.verify_text_prompt(lambda: self.menu_page.load_data_exception(), "需先暂停设备以进行任何文件操作", "load_data_exception")

    def test_file_exception_02_save_data(self):
        """验证在设备运行状态下保存数据的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_data_exception(),"需先暂停设备以进行任何文件操作", "save_data_exception")
      
    def test_file_exception_03_save_point_cloud_format(self):
        """验证在设备运行状态下保存点云格式文件的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_point_cloud_format_exception(), "需先暂停设备以进行任何文件操作", "save_point_cloud_exception")
    
    def test_file_exception_04_save_2d_snapshot(self):
        """验证在设备运行状态下保存二维解图的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_2d_snapshot_exception(), "需先暂停设备以进行任何文件操作", "save_2d_snapshot_exception")
    
    def test_file_exception_05_save_gif(self):
        """验证在设备运行状态下保存动图的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_gif_exception(), "需先暂停设备以进行任何文件操作", "save_gif_exception")
        self.menu_page.toggle_hold_status() #测试后置条件：将设备切换回暂停状态
