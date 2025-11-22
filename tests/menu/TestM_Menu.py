import unittest
import time
from pages.menu_page import MenuPage
from tests.menu.test_menu_public import TestPublicMenu
from datetime import datetime

now = datetime.now().strftime("%Y%m%d%H%M%S")

"""设置文件为M051040D """
class TestMenu01File(TestPublicMenu):
    def test_file_01_load_data(self):
        """验证导入数据并弹窗提示"""
        data_name = "3dMpdat_M.mpdat"
        load_action = lambda: self.menu_page.load_data(data_name)
        self.verify_text_prompt(load_action, "数据导入成功", "load_data")

    def test_file_02_load_settings(self):
        """验证导入设置并弹窗提示"""
        file_name = "M051040D_Settings.mpset"
        load_action = lambda: self.menu_page.load_settings(file_name)
        self.verify_text_prompt(load_action, "载入设置文件成功", "load_setting")

    def test_file_03_save_data(self):
        """验证保存数据并弹窗提示"""
        file_name = "M_DataExport_" + now + ".mpdat"
        file_action = lambda: self.menu_page.save_data(file_name)
        self.verify_text_prompt(file_action, "数据导出成功", "save_data")

    def test_file_04_point_cloud_format_export(self):
        """验证保存点云格式数据并弹窗提示"""
        file_name = "M_PointCloudExport_" + now + ".ply"
        file_action = lambda: self.menu_page.save_point_cloud_format(file_name)
        self.verify_text_prompt(file_action, "点云导出成功", "point_cloud_format_export")

    def test_file_05_save_settings(self):
        """验证保存设备设置并弹窗提示"""
        file_name = "M_Settings_" + now + ".mpset"
        file_action = lambda: self.menu_page.save_settings(file_name)
        self.verify_text_prompt(file_action, "设置文件保存成功", "save_settings")

    def test_file_06_save_2d_snapshot(self):
        """验证保存二维截图并弹窗提示"""
        file_name = "M_Snapshot_" + now + ".bmp"
        file_action = lambda: self.menu_page.save_2d_snapshot(file_name)
        self.verify_text_prompt(file_action, "保存截图成功", "save_2d_snapshot")

    def test_file_07_save_gif(self):
        """验证保存动图并弹窗提示"""
        file_name = "M_GifExport_" + now + ".gif"
        file_action = lambda: self.menu_page.save_gif(file_name)
        self.verify_text_prompt(file_action, "动图已生成", "save_gif", timeout=100)

    def test_file_08_save_all(self):
        """验证保存所有文件并弹窗提示"""
        file_name = "M_SaveFile_" + now
        file_action = lambda: self.menu_page.save_all_file(file_name)
        self.verify_save_all_prompt(file_action, "保存成功", "save_all", timeout=100)

    def test_file_09_expert_setting_enable(self):
        """验证启用专业设置并弹窗提示"""
        self.verify_text_prompt(lambda: self.menu_page.enable_expert_setting(),
                                "专业设置可能会影响设备正常工作, 需要谨慎使用!", "enable_expert_setting")

    def test_file_10_expert_setting_disable(self):
        """验证启用专业设置并弹窗提示"""
        self.menu_page.enable_expert_setting()

class TestMenu02ileException(TestPublicMenu):
    """测试文件操作在设备运行状态下的异常场景"""

    def test_file_exception_01_load_data(self):
        """验证在设备运行状态下导入数据的异常提示"""
        self.menu_page.toggle_run_status()  # 测试前置条件：将设备切换到运行状态
        self.verify_text_prompt(lambda: self.menu_page.load_data_exception(), "需先暂停设备以进行任何文件操作",
                                "load_data_exception")

    def test_file_exception_02_save_data(self):
        """验证在设备运行状态下保存数据的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_data_exception(), "需先暂停设备以进行任何文件操作",
                                "save_data_exception")

    def test_file_exception_03_save_point_cloud_format(self):
        """验证在设备运行状态下保存点云格式文件的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_point_cloud_format_exception(),
                                "需先暂停设备以进行任何文件操作", "save_point_cloud_exception")

    def test_file_exception_04_save_2d_snapshot(self):
        """验证在设备运行状态下保存二维解图的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_2d_snapshot_exception(), "需先暂停设备以进行任何文件操作",
                                "save_2d_snapshot_exception")

    def test_file_exception_05_save_gif(self):
        """验证在设备运行状态下保存动图的异常提示"""
        self.verify_text_prompt(lambda: self.menu_page.save_gif_exception(), "需先暂停设备以进行任何文件操作",
                                "save_gif_exception")
        self.menu_page.toggle_hold_status()  # 测试后置条件：将设备切换回暂停状态

class TestMenu03PresetModes(TestPublicMenu):
    def test_preset_01_fast_with_binning_enabled(self):
        """验证预设模式_'快速 - 合并像素开启'"""
        expected_states = {
            'working_mode': 'fast',
            'binning': True,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_fast_binning, "fast_with_binning_enabled",
                                            expected_states)

    def test_preset_02_super_precise_with_binning_enabled(self):
        """验证预设模式_'超准 - 合并像素开启'"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': True,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_finest_binning, "super_precise_with_binning_enabled",
                                            expected_states)

    def test_preset_03_fast_with_binning_disable(self):
        """验证预设模式_'快速 - 合并像素关闭'"""
        expected_states = {
            'working_mode': 'fast',
            'binning': False,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_fastest_standard, "fast_with_binning_disable",
                                            expected_states)

    def test_preset_04_super_precise_with_binning_disable(self):
        """验证预设模式_'超准 - 合并像素关闭'"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': False,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_finest_standard, "super_precise_with_binning_disable",
                                            expected_states)

    def test_preset_05_hold_to_run(self):
        """验证预设模式_ 运行 / 暂停_ 从暂停状态切换到运行状态"""
        self.verify_run_hold_toggle(self.menu_page.toggle_run_status, "hold to run", expected_final_state='run')

    def test_preset_06_run_to_hold(self):
        """验证预设模式_ 运行 / 暂停_ 从运行状态切换到暂停状态"""
        self.verify_run_hold_toggle(self.menu_page.toggle_hold_status, "run to hold", expected_final_state='hold')

    def test_preset_07_shortcut_f1(self):
        """验证快捷键F1 - 快速·合并像素开启"""
        expected_states = {
            'working_mode': 'fast',
            'binning': True,
        }
        self.menu_page.preset_shortcut('F1')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F1", expected_states)

    def test_preset_08_shortcut_f2(self):
        """验证快捷键F2 - 超准-合并像素开启"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': True,
        }
        self.menu_page.preset_shortcut('F2')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F2", expected_states)

    def test_preset_09_shortcut_f3(self):
        """验证快捷键F3 - 快速·合并像素关闭"""
        expected_states = {
            'working_mode': 'fast',
            'binning': False,
        }
        self.menu_page.preset_shortcut('F3')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F3", expected_states)

    def test_preset_10_shortcut_f4(self):
        """验证快捷键F4 - 超准-合并像素关闭"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': False,
        }
        self.menu_page.preset_shortcut('F4')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F4", expected_states)

    def test_preset_11_shortcut_f5(self):
        """验证快捷键F5 - 运行/暂停"""
        # 获取当前状态
        current_status = self.menu_page.get_device_status()
        # 确定预期的最终状态
        expected_final_state = 'run' if current_status == 'hold' else 'hold'
        self.menu_page.preset_shortcut('F5')
        # 验证状态
        self.verify_run_hold_toggle(lambda: None, "shortcut_F5", expected_final_state=expected_final_state)

class TestMenu04Display(TestPublicMenu):

    def test_display_01_full_screen(self):
        """验证进入全屏/ 退出全屏"""
        # self.menu_page.toggle_run_status()  # 单独执行用例时设备切换为运行状态
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

class TestMenu05Language(TestPublicMenu):

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
