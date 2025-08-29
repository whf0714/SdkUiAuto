import unittest
import time
from pages.menu_page import MenuPage
from tests.menu.test_menu_public import TestPublicMenu
from datetime import datetime

class TestMenuPresetModes(TestPublicMenu):
    def test_preset_01_fast_with_binning_enabled(self):
        """验证预设模式_'快速 - 合并像素开启'"""
        expected_states = {
            'working_mode': 'fast',
            'binning': True,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_fast_binning,"fast_with_binning_enabled", expected_states)

    def test_preset_02_super_precise_with_binning_enabled(self):
        """验证预设模式_'超准 - 合并像素开启'"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': True,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_finest_binning,"super_precise_with_binning_enabled", expected_states)
    
    def test_preset_03_fast_with_binning_disable(self):
        """验证预设模式_'快速 - 合并像素关闭'"""
        expected_states = {
            'working_mode': 'fast',
            'binning': False,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_fastest_standard,"fast_with_binning_disable", expected_states)
    
    def test_preset_04_super_precise_with_binning_disable(self):
        """验证预设模式_'超准 - 合并像素关闭'"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': False,
        }
        self.verify_preset_mode_combination(self.menu_page.preset_finest_standard,"super_precise_with_binning_disable", expected_states)
        
    def test_preset_05_fast_with_binning_and_auto_phdr(self):
        """验证预设模式_'快速 - 合并像素开启且自动曝光开启'"""
        expected_states = {
            'working_mode': 'fast',
            'binning': True,
            'exposure_mode': 'auto_phdr'
        }
        self.verify_preset_mode_combination(self.menu_page.preset_fastest_binning_autohdr,"fast_with_binning_and_auto_phdr", expected_states)

    def test_preset_06_super_precise_with_binning_and_auto_phdr(self):
        """验证预设模式_'超准 - 合并像素开启且自动曝光开启'"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': True,
            'exposure_mode': 'auto_phdr'
        }
        self.verify_preset_mode_combination(self.menu_page.preset_finest_binning_autohdr,"super_precise_with_binning_and_auto_phdr", expected_states)

    def test_preset_07_fast_with_binning_disable_and_auto_phdr(self):
        """验证预设模式_'快速 - 合并像素关闭且自动曝光开启'"""
        expected_states = {
            'working_mode': 'fast',
            'binning': False,
            'exposure_mode': 'auto_phdr'
        }
        self.verify_preset_mode_combination(self.menu_page.preset_fastest_standard_autohdr,"fast_with_binning_disable_and_auto_phdr", expected_states)

    def test_preset_08_super_precise_with_binning_disable_and_auto_phdr(self):
        """验证预设模式_'超准 - 合并像素关闭且自动曝光开启'"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': False,
            'exposure_mode': 'auto_phdr'
        }
        self.verify_preset_mode_combination(self.menu_page.preset_finest_standard_autohdr,"super_precise_with_binning_disable_and_auto_phdr", expected_states)

    def test_preset_09_hold_to_run(self):
        """验证预设模式_ 运行 / 暂停_ 从暂停状态切换到运行状态"""
        self.verify_run_hold_toggle(self.menu_page.toggle_run_status,"hold to run",expected_final_state='run')
    
    def test_preset_10_run_to_hold(self):
        """验证预设模式_ 运行 / 暂停_ 从运行状态切换到暂停状态"""
        self.verify_run_hold_toggle(self.menu_page.toggle_hold_status, "run to hold",expected_final_state='hold')

    def test_preset_11_shortcut_f1(self):
        """验证快捷键F1 - 快速·合并像素开启"""
        expected_states = {
            'working_mode': 'fast',
            'binning': True,
        }
        self.menu_page.preset_shortcut('F1')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F1", expected_states)

    def test_preset_12_shortcut_f2(self):
        """验证快捷键F2 - 超准-合并像素开启"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': True,
        }
        self.menu_page.preset_shortcut('F2')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F2", expected_states)

    def test_preset_13_shortcut_f3(self):
        """验证快捷键F3 - 快速·合并像素关闭"""
        expected_states = {
            'working_mode': 'fast',
            'binning': False,
        }
        self.menu_page.preset_shortcut('F3')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F3", expected_states)

    def test_preset_14_shortcut_f4(self):
        """验证快捷键F4 - 超准-合并像素关闭"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': False,
        }
        self.menu_page.preset_shortcut('F4')
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_F4", expected_states)

    def test_preset_15_shortcut_shift_f1(self):
        """验证快捷键Shift+f1 - 快速·合并像素开启且自动曝光开启"""
        expected_states = {
            'working_mode': 'fast',
            'binning': True,
            'exposure_mode': 'auto_phdr'
        }
        self.menu_page.preset_shortcut('F1', ['Shift'])
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_Shift_F1", expected_states)

    def test_preset_16_shortcut_shift_f2(self):
        """验证快捷键Shift+F2 - 超准-合并像素开启且自动曝光开启"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': True,
            'exposure_mode': 'auto_phdr'
        }
        self.menu_page.preset_shortcut('F2', ['Shift'])
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_Shift_F2", expected_states)

    def test_preset_17_shortcut_shift_f3(self):
        """验证快捷键Shift+F3 - 快速-合并像素关闭且自动曝光开启"""
        expected_states = {
            'working_mode': 'fast',
            'binning': False,
            'exposure_mode': 'auto_phdr'
        }
        self.menu_page.preset_shortcut('F3', ['Shift'])
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_Shift_F3", expected_states)

    def test_preset_18_shortcut_shift_f4(self):
        """验证快捷键Shift+F4 - 超准·合并像素关闭且自动曝光开启"""
        expected_states = {
            'working_mode': 'super_precise',
            'binning': False,
            'exposure_mode': 'auto_phdr'
        }
        self.menu_page.preset_shortcut('F4', ['Shift'])
        # 验证状态
        self.verify_preset_mode_combination(lambda: None, "shortcut_Shift_F4", expected_states)

    def test_preset_19_shortcut_f5(self):
        """验证快捷键F5 - 运行/暂停"""
        # 获取当前状态
        current_status = self.menu_page.get_device_status()
        # 确定预期的最终状态
        expected_final_state = 'run' if current_status == 'hold' else 'hold'
        self.menu_page.preset_shortcut('F5')
        # 验证状态
        self.verify_run_hold_toggle(lambda: None, "shortcut_F5", expected_final_state=expected_final_state)


# if __name__ == '__main__':
#     unittest.main()