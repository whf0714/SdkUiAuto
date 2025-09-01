import unittest
import pyautogui
from pages.menu_page import MenuPage
import os
import time
import unittest

class TestPublicMenu(unittest.TestCase):

    menu_page = MenuPage()  # 直接使用单例

    @classmethod
    def setUpClass(cls):
        # 确保设备状态已初始化
        # MenuPage单例会在创建时自动调用_initialize_device_status方法
        # 等待初始化完成
        # time.sleep(2)
        print("设备状态已初始化，确保处于暂停状态")

    @classmethod
    def tearDownClass(cls):
        # 仅在非全局套件运行时关闭实例
        if not os.getenv('GLOBAL_SUITE_RUNNING'):
            cls.menu_page.quit()

    def verify_text_prompt(self, menu_method, expected_text, menu_name, timeout=None):
        """验证操作后是否出现包含指定文本的提示
        
        Args:
            menu_method: 要执行的操作方法
            expected_text: 期望包含的文本内容
            menu_name: 操作名称，用于日志输出
            timeout: 等待超时时间（秒），默认使用wait_for_text_prompt的默认值
        """
        print(f"Starting test for {menu_name} ...")
        try:
            # 执行操作
            menu_method()
            # 等待提示出现
            if timeout is not None:
                prompt_info = self.menu_page.wait_for_text_prompt(expected_text, timeout=timeout)
            else:
                prompt_info = self.menu_page.wait_for_text_prompt(expected_text)
            # 验证提示内容
            if prompt_info:
                self.assertTrue(expected_text in prompt_info['text'], 
                               f"{menu_name}后提示文本不正确: {prompt_info['text']}")
                # print(f"✅ {menu_name}后验证成功: 出现包含'{expected_text}'的提示")
                # 验证成功后尝试关闭提示窗口
                try:
                    self.menu_page.close_popup()
                    # print("✅ 成功关闭提示窗口")
                    # 关闭提示窗口后确保切换回操作界面窗口
                    # self.menu_page._ensure_operation_window() ##########444
                except Exception as e:
                    # print(f"❌ 关闭提示窗口失败: {str(e)}")
                    pass
            else:
                self.fail(f"❌ {menu_name}后未出现包含'{expected_text}'的提示")
        except Exception as e:
            self.menu_page.take_screenshot(f"{menu_name}VerificationFailed")
            # print(f"❌ {menu_name}验证失败: {str(e)}")
            raise e

    def verify_save_all_prompt(self, menu_method, expected_text, menu_name, timeout=None):
        """专门用于验证保存所有文件操作后的提示，确保关闭所有窗口并返回主界面
        
        Args:
            menu_method: 要执行的操作方法
            expected_text: 期望包含的文本内容
            menu_name: 操作名称，用于日志输出
            timeout: 等待超时时间（秒）
        """
        print(f"Starting test for {menu_name} (save_all_specific)...")
        try:
            # 执行操作
            menu_method()
            # 等待提示出现
            if timeout is not None:
                prompt_info = self.menu_page.wait_for_text_prompt(expected_text, timeout=timeout)
            else:
                prompt_info = self.menu_page.wait_for_text_prompt(expected_text)
            # 验证提示内容
            if prompt_info:
                self.assertTrue(expected_text in prompt_info['text'], 
                               f"{menu_name}后提示文本不正确: {prompt_info['text']}")
                # 验证成功后尝试关闭提示窗口
                try:
                    self.menu_page.close_popup()
                except Exception as e:
                    print(f"关闭提示窗口失败: {str(e)}")
                    pass
                
                # 关闭所有可能打开的窗口
                try:
                    self.menu_page.close_multi_windows()
                except Exception as e:
                    print(f"关闭多窗口失败: {str(e)}")
                    pass
                
                # 通过 MenuPage 内部的窗口管理机制确保回到正确的操作界面窗口
                self.menu_page._ensure_operation_window()
                # 等待主窗口加载完成
                time.sleep(2)
            else:
                self.fail(f"❌ {menu_name}后未出现包含'{expected_text}'的提示")
        except Exception as e:
            self.menu_page.take_screenshot(f"{menu_name}VerificationFailed")
            print(f"❌ {menu_name}验证失败: {str(e)}")
            raise e

    def verify_preset_mode_combination(self, menu_method, preset_name,expected_states):
        """
        验证预设模式及其相关状态（如合并像素、自动曝光等）是否正确设置
        :param preset_name: 预设模式名称
        :param expected_states: 字典，包含其他需要验证的状态，如 {'binning': True, 'exposure_mode': 'auto_nhdr', 'working_mode': 'fast'}
        """
        print(f"Starting test for preset mode {preset_name} ...")
        try:

            menu_method()
            #验证共工作模式选中状态
            if 'working_mode' in expected_states:
                working_mode = expected_states['working_mode']
                actual_status =self.menu_page.get_working_mode_status(working_mode)
                self.assertTrue(actual_status, f"工作模式 '{working_mode}' 未被选中")
            
            # 处理合并像素验证
            if 'binning' in expected_states:
                expected_binning_status = expected_states['binning']
                actual_binning_status = self.menu_page.get_binning_status()
                self.assertEqual(actual_binning_status, expected_binning_status, 
                                f"合并像素状态不匹配: 预期={expected_binning_status}, 实际={actual_binning_status}")
            # 处理曝光模式验证
            if 'exposure_mode' in expected_states:
                exposure_mode = expected_states['exposure_mode']
                actual_exposure_status =self.menu_page.get_exposure_mode_status(exposure_mode)
                self.assertTrue(actual_exposure_status, f"曝光模式 '{exposure_mode}' 未被选中")

        except AssertionError as ae:
            self.menu_page.take_screenshot(f"{preset_name}_combination_failed")
            print(f"❌ 验证预设模式组合 '{preset_name}' 失败")
            raise


    def verify_run_hold_toggle(self, menu_method,setting_name, expected_final_state=None):
        """
        验证运行/暂停功能的状态切换
            expected_final_state: 预期的最终状态('hold' 或 'run')
        """
        print(f"Starting test for preset mode_{setting_name}")
        try:
            # 执行运行/暂停切换
            menu_method()
            time.sleep(2)  # 等待状态切换完成   
            # 检查最终状态
            final_status = self.menu_page.get_device_status()
            if expected_final_state:
                self.assertEqual(final_status, expected_final_state, 
                                f"最终状态不匹配: 预期={expected_final_state}, 实际={final_status}")
                # print(f"✅ 最终状态验证成功: {final_status}")
        except AssertionError as ae:
            self.menu_page.take_screenshot("run_hold_verification_failed")
            print(f"❌ 验证运行/暂停功能失败")
            raise

    def verify_language_element_name(self,menu_method,expected_name,setting_name,automation_id):
        """
        验证切换语言后指定元素的名称是否为中/英文
        Args:
            menu_method: 要执行的语言切换方法
            expected_name: 期望的元素名称
            setting_name: 操作名称，用于日志输出
            automation_id: 元素的AutomationId
        """
        print(f"Starting test for language_{setting_name}")
        try:
            menu_method()
            actual_name = self.menu_page.get_element_name(automation_id)
            self.assertEqual(actual_name, expected_name,f"{setting_name}后元素名称不匹配:,automation_id='{automation_id}' 预期='{expected_name}', 实际='{actual_name}'")
        except AssertionError as ae:
            self.menu_page.take_screenshot("language_verification_failed")
            print(f"❌ 验证{setting_name}功能失败")
            raise



    # if __name__ == '__main__':
#     unittest.main()