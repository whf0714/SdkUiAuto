from nt import device_encoding
from re import S
from time import sleep
from tracemalloc import Snapshot
# from selenium.common.exceptions import NoSuchWindowException
from utils.driver_manager import get_driver_manager
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from appium.webdriver.common.mobileby import MobileBy
from datetime import datetime
import os
import time
import pyautogui as pg
from config.config import SCREENSHOTS_DIR, NAVIGATION_PATHS, UI_READ_DATA_PATH, UI_SAVE_DATA_PATH


class MenuPage:
    # 设备状态按钮相关常量
    DEVICE_STATUS_BUTTON_X = 113
    DEVICE_STATUS_BUTTON_Y = 1384
    DEVICE_STATUS_COLOR_HOLD = (176, 28, 58)  # 暂停状态颜色 (红色)
    DEVICE_STATUS_COLOR_RUN = (77, 133, 72)   # 运行状态颜色 (绿色)

    def __init__(self):
        # 使用驱动管理器获取驱动实例
        # self.driver = get_driver_manager().get_driver()
        # self._initialize_device_status()
        pass

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # 使用驱动管理器获取驱动实例
            cls._instance.driver = get_driver_manager().get_driver()
            # 保存当前窗口句柄（可能是显示窗口）
            cls._instance.main_window_handle = cls._instance.driver.current_window_handle
            # print(f"已保存初始窗口句柄: {cls._instance.main_window_handle}")
            # 初始化操作界面窗口句柄为None，需要在使用时动态获取
            cls._instance.operation_window_handle = None
            cls._instance._initialize_device_status()  # 单例初始化时自动检查设备状态
            # 初始化时尝试识别操作界面窗口
            cls._instance._ensure_operation_window()
        return cls._instance

    def _get_device_current_status(self):
        """
        获取设备当前的运行状态
        :return: 'run' 表示运行状态, 'hold' 表示暂停状态
        """
        device_status_button_color = pg.pixel(self.DEVICE_STATUS_BUTTON_X, self.DEVICE_STATUS_BUTTON_Y)

        if device_status_button_color == self.DEVICE_STATUS_COLOR_RUN:
            return 'run'
        elif device_status_button_color == self.DEVICE_STATUS_COLOR_HOLD:
            return 'hold'
        else:
            self.take_screenshot("UnexpectedColor")
            raise RuntimeError(
                f"Unexpected color detected {device_status_button_color} at ({self.DEVICE_STATUS_BUTTON_X}, {self.DEVICE_STATUS_BUTTON_Y})"
            )
    
    def get_device_status(self):
        """
        获取设备当前的运行状态（公开方法）
        :return: 'run' 表示运行状态, 'hold' 表示暂停状态
        """
        return self._get_device_current_status()

    def _initialize_device_status(self):
        """单例初始化时自动检查设备状态 - MenuPage需要确保设备处于暂停状态"""
        time.sleep(1)      
        # 通过_get_device_current_status获取设备当前状态
        current_status = self._get_device_current_status()      
        # 确保设备处于暂停状态
        if current_status == 'run':
            pg.click(self.DEVICE_STATUS_BUTTON_X, self.DEVICE_STATUS_BUTTON_Y)

    def open_sdk(self, server, desired_caps):
        self.driver = webdriver.Remote(command_executor=server, desired_capabilities=desired_caps)

    def _wait_until_clickable(self, locator, timeout=10):
        """Helper method to wait until an element is clickable."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.take_screenshot("element_not_clickable")
            raise
          
    def _ensure_operation_window(self):
        """确保当前窗口是操作界面窗口，而不是显示窗口
        问题核心：main_window_handle可能只是显示窗口，而我们需要操作界面窗口来执行菜单操作
        
        Returns:
            bool: 是否成功切换到操作界面窗口
        """
        try:
            # 检查当前窗口是否已经是操作界面窗口，避免不必要的切换
            if self.driver.current_window_handle == self.operation_window_handle:
                # 如果已经在操作界面窗口，则不执行任何操作
                return True
                
            # 如果已经知道操作界面窗口句柄且它仍然存在，则直接切换
            if self.operation_window_handle and self.operation_window_handle in self.driver.window_handles:
                self.driver.switch_to.window(self.operation_window_handle)
                # print(f"已切换到操作界面窗口: {self.operation_window_handle}")
                return True
                
            # 尝试查找包含菜单的操作界面窗口
            original_handle = self.driver.current_window_handle
            for handle in self.driver.window_handles:
                if handle != original_handle:
                    try:
                        self.driver.switch_to.window(handle)
                        # 检查是否是操作界面（例如检查是否存在"文件"菜单）
                        file_menu = self.driver.find_elements(By.NAME, "文件")
                        if len(file_menu) > 0:
                            self.operation_window_handle = handle
                            # print(f"找到并切换到操作界面窗口: {handle}")
                            return True
                    except Exception as e:
                        print(f"检查窗口{handle}时出错: {str(e)}")
                        continue
                        
            # 如果没有找到专门的操作界面窗口，至少确保我们回到主窗口
            self.driver.switch_to.window(self.main_window_handle)
            # 设置主窗口为操作界面窗口，避免后续重复查找
            self.operation_window_handle = self.main_window_handle
            # if self.debug:
            #     print(f"未找到专门的操作界面窗口，已切换回主窗口: {self.main_window_handle}")
            return True
            
        except Exception as e:
            print(f"确保操作界面窗口时发生错误: {str(e)}")
            # 出错时至少回到主窗口
            if self.main_window_handle in self.driver.window_handles:
                self.driver.switch_to.window(self.main_window_handle)
                self.operation_window_handle = self.main_window_handle
            return False
            
    def _switch_to_new_window(self, original_window, timeout=30):
        """等待新窗口出现并切换到该窗口
        
        Args:
            original_window: 原始窗口句柄
            timeout: 超时时间(秒)
            
        Returns:
            bool: 是否成功切换到新窗口
        """
        try:
            # 等待新窗口出现
            WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.window_handles) > 1
            )
            
            # 切换到新窗口
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    # print(f"已切换到新窗口: {window_handle}")
                    return True
            
            return False
        except Exception as e:
            print(f"切换到新窗口时发生错误: {str(e)}")
            return False
            
    def _switch_to_original_window(self, original_window):
        """切换回原始窗口
        
        Args:
            original_window: 原始窗口句柄
        """
        try:
            if original_window and original_window in self.driver.window_handles:
                self.driver.switch_to.window(original_window)
                print(f"已切换回原始窗口: {original_window}")
                return True
            else:
                # 如果原始窗口不存在，则切换到操作界面窗口
                print("原始窗口不存在，切换到操作界面窗口")
                return self._ensure_operation_window()
        except Exception as e:
            print(f"切换回原始窗口时发生错误: {str(e)}")
            return self._ensure_operation_window()

    def click(self, locator, timeout=10, ignore_timeout=False):
        try:
            element = self._wait_until_clickable(locator, timeout)
            element.click()
        except TimeoutException:
            if not ignore_timeout:
                raise
            print(f"Timeout while waiting for {locator} to be clickable.")

    def force_click(self, locator, wait_timeout=5):
        try:
            element = WebDriverWait(self.driver, wait_timeout).until(
                EC.presence_of_element_located(locator)
            )
            ActionChains(self.driver).move_to_element(element).click().perform()
            # print(f"✅ 强制点击成功: {locator}")
        except Exception as e:
            # self.take_screenshot(f"force_click_failed_{str(locator).replace('/', '_')}")
            print(f"❌强制点击失败: {e}")
            raise


    def double_click(self, locator, timeout=10, ignore_timeout=False):
        try:
            element = self._wait_until_clickable(locator, timeout)
            ActionChains(self.driver).double_click(element).perform()
        except TimeoutException:
            if not ignore_timeout:
                raise
            print(f"Timeout while waiting for {locator} to be clickable.")

    def scroll_down(self):
        scroll_locator = (MobileBy.ACCESSIBILITY_ID, "NonClientVerticalScrollBar")
        self.click(scroll_locator)
        pg.scroll(-1)

    def wait_for_standby(self, timeout=10):
        standby_locator = (By.XPATH, "//StatusBar[@AutomationId='DeviceInfoSts']//Text[normalize-space(@Name)='StandBy']")
        standby_text = None
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(standby_locator)
            )
            element = self.driver.find_element(*standby_locator)
            standby_text = element.text
            # print(f"获取的当前设备状态为: {standby_text}")
            return standby_text
        except TimeoutException:
            print("❌ The current device status is not 'StandBy' ")
            return None

    def wait_for_text_prompt(self, expected_text, timeout=10):
        """等待包含指定文本的提示元素出现

        Args:
            expected_text: 期望包含的文本内容
            timeout: 等待超时时间（秒）

        Returns:
            dict: 包含text和control_type的字典，如果超时则返回None
        """
        locator = (By.XPATH, f"//*[contains(@Name, '{expected_text}')]")

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element = self.driver.find_element(*locator)
            prompt_text = element.get_attribute('Name')
            # print(f"✅ 检测到提示: '{prompt_text}'")
            return {
                'text': prompt_text,
            }
        except TimeoutException:
            print(f"❌ 未检测到包含'{expected_text}'的提示")
            self.take_screenshot(f"{expected_text.replace(' ', '_')}PromptNotFound")
            return None

    def take_screenshot(self, name):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        file_path = os.path.join(SCREENSHOTS_DIR, file_name)
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved as {file_path}")

    def get_checkbox_status(self, locator):
        checkbox = self.driver.find_element(*locator)
        return checkbox.is_selected()

    def navigate_to_data_directory(self):
        """导航到数据目录的辅助方法"""
        try:
            self.click((By.NAME, NAVIGATION_PATHS['d_drive']))
            self.double_click((By.NAME, NAVIGATION_PATHS['program']))
            self.double_click((By.NAME, NAVIGATION_PATHS['python']))
            self.double_click((By.NAME, NAVIGATION_PATHS['sdkui']))
            self.double_click((By.NAME, NAVIGATION_PATHS['data']))
            return True
        except Exception as e:
            print(f"导航到数据目录时出错: {str(e)}")
            self.take_screenshot("navigate_directory_error")
            return False
    
    def navigate_to_read_directory(self):
        """导航到读取目录的辅助方法"""
        try:
            if not self.navigate_to_data_directory():
                return False
            self.double_click((By.NAME, NAVIGATION_PATHS['read']))
            return True
        except Exception as e:
            print(f"导航到读取目录时出错: {str(e)}")
            self.take_screenshot("navigate_read_directory_error")
            return False
    
    def navigate_to_save_directory(self):
        """导航到保存目录的辅助方法"""
        try:
            if not self.navigate_to_data_directory():
                return False
            self.double_click((By.NAME, NAVIGATION_PATHS['save']))
            return True
        except Exception as e:
            print(f"导航到保存目录时出错: {str(e)}")
            self.take_screenshot("navigate_save_directory_error")
            return False

    def trigger_camera(self):
        trigger_locator = (By.NAME, "发送软件触发")
        self.click(trigger_locator)
           
    def load_data(self, data_name):
        # print(f"Trying to open data: {data_name}")
        self.click((By.NAME, "文件"))
        self.click((By.NAME, "导入数据"))
        if not self.navigate_to_read_directory():
            return False
        self.click((By.NAME, data_name), timeout=10)
        self.click((By.NAME, "打开(O)"))
        # print(f"Successfully opened data: {data_name}")
        return True

    def close_popup(self):
        self.click((By.NAME, "确定"))

    def close_multi_windows(self):
        # self.click((By.NAME, "关闭"))
        close_multi_windows_locator = (MobileBy.ACCESSIBILITY_ID, "Close")
        self.click(close_multi_windows_locator)


    def load_settings(self,file_name):
        # print(f"Trying to open settings: {file_name}")
        self.click((By.NAME, "文件"))
        load_setting_locator = (By.NAME, "导入设备设置")
        self.force_click(load_setting_locator)
        if not self.navigate_to_read_directory():
            return False
        self.click((By.NAME, file_name), timeout=10)
        self.click((By.NAME, "打开(O)"))
        # print(f"Successfully opened settings: {file_name}")
        return True

    def _input_file_name(self, file_name, timeout=10, screenshot_name="input_error"):
        """
        定位windows文件名输入框并输入内容的通用方法
        
        Args:
            file_name: 要输入的文件名
            timeout: 等待超时时间
            screenshot_name: 发生错误时的截图名称前缀
            
        Returns:
            bool: 操作是否成功
        """
        try:
            # 使用更可靠的类名定位文件名输入框
            input_locator = (By.CLASS_NAME, "Edit")
            # 等待输入框可见
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(input_locator)
            )
            # 获取输入框元素
            input_box = self.driver.find_element(*input_locator)
            # 点击输入框以激活
            input_box.click()
            # 全选现有文本(Ctrl+A)并删除
            pg.hotkey('ctrl', 'a')
            pg.press('backspace')
            # 输入新文件名
            pg.write(file_name)
            return True
        except Exception as e:
            print(f"定位或操作文件名输入框时出错: {str(e)}")
            self.take_screenshot(screenshot_name)
            return False

    def save_data(self, file_name, timeout=10):
        # print(f"Trying to save data: {file_name}")
        self.click((By.NAME, "文件"))
        save_data_locator = (By.NAME, "保存数据")
        self.force_click(save_data_locator)
        if not self.navigate_to_save_directory():
            return False

        if not self._input_file_name(file_name, timeout, "save_data_input_error"):
            return False

        self.click((By.NAME, "保存(S)"))
        # print(f"Successfully saved data : {file_name}")
        return True

    def save_settings(self, file_name, timeout=10):
        # print(f"Trying to save settings: {file_name}")
        self.click((By.NAME, "文件"))
        save_settings_locator = (By.NAME, "保存设备设置")
        self.force_click(save_settings_locator)
        if not self.navigate_to_save_directory():
            return False

        if not self._input_file_name(file_name, timeout, "save_settings_input_error"):
            return False

        self.click((By.NAME, "保存(S)"))
        # print(f"Successfully saved settings : {file_name}")
        return True

    def save_point_cloud_format(self, file_name, timeout=10):
        # print(f"Trying to save point cloud format: {file_name}")
        self.click((By.NAME, "文件"))
        save_point_cloud_locator = (By.NAME, "保存点云格式")
        self.force_click(save_point_cloud_locator)
        if not self.navigate_to_save_directory():
            return False

        if not self._input_file_name(file_name, timeout, "point_cloud_format_input_error"):
            return False

        self.click((By.NAME, "保存(S)"))
        # print(f"Successfully saved point cloud format : {file_name}")
        return True

    def save_2d_snapshot(self, file_name, timeout=10):
        # print(f"Trying to save 2D snapshot: {file_name}")
        self.click((By.NAME, "文件"))
        save_2d_locator = (By.NAME, "保存二维截图")
        self.force_click(save_2d_locator)
        if not self.navigate_to_save_directory():
            return False

        if not self._input_file_name(file_name, timeout, "save_2d_snapshot_input_error"):
            return False

        self.click((By.NAME, "保存(S)"))
        # print(f"Successfully saved 2D snapshot: {file_name}")
        return True

    def save_gif(self, file_name, timeout=10):
        # print(f"Trying to save gif: {file_name}")
        self.click((By.NAME, "文件"))
        save_gif_locator = (By.NAME, "保存动图")
        self.force_click(save_gif_locator)
        if not self.navigate_to_save_directory():
            return False

        if not self._input_file_name(file_name, timeout, "save_gif_input_error"):
            return False

        self.click((By.NAME, "保存(S)"))
        # print(f"Successfully saved animation: {file_name}")
        return True

    def save_all_file(self, file_name, timeout=30):

        # print(f"Trying to save all file，超时时间设置为: {timeout}秒") 
        # 获取当前窗口句柄
        original_window = self.driver.current_window_handle
        # print(f"原始窗口句柄: {original_window}")
        # print(f"主窗口句柄: {self.main_window_handle}")
        self.click((By.NAME, "文件"))
        save_all_locator = (By.NAME, "保存所有文件")
        self.force_click(save_all_locator)
        
        try:
            # 等待新窗口出现并切换到该窗口
            if not self._switch_to_new_window(original_window, timeout):
                print("未能切换到新窗口")
                return False
            
            # 等待"保存所有文件设置"窗口出现
            window_title = "保存所有文件设置"
            # print(f"等待{window_title}窗口加载完成...")
            
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.NAME, window_title))
            )
            
            # print(f"{window_title}窗口已加载，开始执行保存操作...")
            # print("打印窗口HTML内容:\n" + self.driver.page_source)
            
            # 内部函数：设置文件名
            def set_file_name(locator, file_name):
                self.double_click(locator)
                # 清除现有内容
                pg.keyDown('ctrl')
                pg.press('a')
                pg.keyUp('ctrl')
                pg.press('backspace')
                # 输入新文件名
                pg.write(file_name)
                
            # 勾选所有保存选项
            checkboxes = [
                (MobileBy.ACCESSIBILITY_ID, "SaveDataCkb"),
                (MobileBy.ACCESSIBILITY_ID, "SaveDeviceSettingCkb"),
                (MobileBy.ACCESSIBILITY_ID, "Save2DSnapshotCkb"),
                (MobileBy.ACCESSIBILITY_ID, "SaveTextPointCloudCkb")
            ]
            
            for checkbox in checkboxes:
                self.click(checkbox)
            
            # 设置所有文件名
            file_name_locators = [
                (MobileBy.ACCESSIBILITY_ID, "MpdatFileNameTb"),
                (MobileBy.ACCESSIBILITY_ID, "DeviceSettingFileNameTb"),
                (MobileBy.ACCESSIBILITY_ID, "SnapshotFileNameTb"),
                (MobileBy.ACCESSIBILITY_ID, "TextPointCloudFileNameTb")
            ]
            
            for locator in file_name_locators:
                set_file_name(locator, file_name)
            
            # 点击保存按钮
            save_button_locator = (MobileBy.ACCESSIBILITY_ID, "SaveBtn")
            self.click(save_button_locator)
            if not self.navigate_to_save_directory():
                return False

            self.click((By.NAME, "保存(S)"))
            
            # 操作成功时，确保返回操作界面窗口
            # 注意：这里不立即切换回原窗口，让调用者决定窗口切换的时机
            # 以便调用者可以先检测保存成功的提示信息
            return True
        
        except Exception as e:
            print(f"保存所有文件时发生错误: {str(e)}")
            # 保存截图以供调试
            self.take_screenshot("save_all_timeout_Failed")
            # 出错时确保切换回操作界面窗口
            self._ensure_operation_window()
            return False

        # return False

    def enable_expert_setting(self):
        self.click((By.NAME, "文件"))
        enable_expert_locator = (By.NAME, "启用专业设置")
        self.force_click(enable_expert_locator)


    def get_working_mode_status(self, mode_name):
        """
        获取指定工作模式的选中状态
        :param mode_name: 工作模式名称（fast, standard, precise, super_precise, white, grid, black, exposure_prediction）
        :return: 布尔值，表示该工作模式是否被选中
        """
        mode_locators = {
            'fast': (MobileBy.ACCESSIBILITY_ID, "WorkingModeFastRbt"),
            'standard': (MobileBy.ACCESSIBILITY_ID, "WorkingModeStandardRbt"),
            'precise': (MobileBy.ACCESSIBILITY_ID, "WorkingModePreciseRbt"),
            'super_precise': (MobileBy.ACCESSIBILITY_ID, "WorkingModeSuperPreciseRbt"),
            'white': (MobileBy.ACCESSIBILITY_ID, "WorkingModeWhiteRbt"),
            'grid': (MobileBy.ACCESSIBILITY_ID, "WorkingModeGridRbt"),
            'black': (MobileBy.ACCESSIBILITY_ID, "WorkingModeBlackRbt"),
            'exposure_prediction': (MobileBy.ACCESSIBILITY_ID, "WorkingModeExposurePredictionRbt")
        }

        return self.get_checkbox_status(mode_locators[mode_name])

    def get_binning_status(self):
        binning_locator = (MobileBy.ACCESSIBILITY_ID, "BinningStateCkb")
        return self.get_checkbox_status(binning_locator)

    def get_exposure_mode_status(self,mode_name):
        if mode_name == 'auto_phdr':
            locators =  (MobileBy.ACCESSIBILITY_ID, "ExposureModeAutoPHDRRbt")
        return self.get_checkbox_status(locators)

    def click_preset_mode(self, preset_name):
        self.click((By.NAME, "预设"))
        preset_locator = (By.NAME, preset_name)
        self.force_click(preset_locator)

    def preset_fast_binning(self):
        self.click_preset_mode("快速 - 合并像素开启")

    def preset_finest_binning(self):
        self.click_preset_mode("超准 - 合并像素开启")

    def preset_fastest_standard(self):
        self.click_preset_mode("快速 - 合并像素关闭")

    def preset_finest_standard(self):
        self.click_preset_mode("超准 - 合并像素关闭")

    def preset_fastest_binning_autohdr(self):
        self.click_preset_mode("快速 - 合并像素开启且自动曝光开启")

    def preset_finest_binning_autohdr(self):
        self.click_preset_mode("超准 - 合并像素开启且自动曝光开启")

    def preset_fastest_standard_autohdr(self):
        self.click_preset_mode("快速 - 合并像素关闭且自动曝光开启")

    def preset_finest_standard_autohdr(self):
        self.click_preset_mode("超准 - 合并像素关闭且自动曝光开启")      

    def preset_shortcut(self, key, modifiers=None):
        """
        模拟按键操作，支持单键和组合键
        Args:
            key: 主按键，如 'f1', 'f2', 'f5' 等
            modifiers: 可选的修饰键列表，如 ['shift'], ['ctrl', 'shift'] 等
        """
        if modifiers:
            with pg.hold(modifiers):
                pg.press(key)
        else:
            pg.press(key)
        time.sleep(1)

    def toggle_run_status(self):
        device_status = self.get_device_status()
        if device_status == 'run':
            pg.click(self.DEVICE_STATUS_BUTTON_X, self.DEVICE_STATUS_BUTTON_Y)
        self.click((By.NAME, "预设"))
        run_pause_locator = (By.NAME, "运行 / 暂停")
        self.force_click(run_pause_locator)

    def toggle_hold_status(self):
        device_status = self.get_device_status()
        if device_status == 'hold':
            pg.click(self.DEVICE_STATUS_BUTTON_X, self.DEVICE_STATUS_BUTTON_Y)
        self.click((By.NAME, "预设"))
        run_pause_locator = (By.NAME, "运行 / 暂停")
        self.force_click(run_pause_locator)

    def click_display(self, display_name):
        self.click((By.NAME, "显示"))
        display_locator = (By.NAME, display_name)
        self.force_click(display_locator)

    def click_language(self, language_name):
        try:
            self.click((By.XPATH, "//MenuBar[@AutomationId='menuStrip1']//MenuItem[@Name='语言']"))
        except:
            try:
                self.click((By.XPATH, "//MenuBar[@AutomationId='menuStrip1']//MenuItem[@Name='Language']"))
            except:
                self.take_screenshot("language_menu_not_found")
                raise Exception("无法找到语言菜单，尝试了'Language'和'语言'两种名称")
        language_locator = (By.NAME, language_name)
        self.force_click(language_locator)

    def get_element_name(self,automation_id, timeout=10):
        locator = (MobileBy.ACCESSIBILITY_ID, automation_id)
        try:
            element =WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element.get_attribute('Name')
        except Exception as e:
            raise Exception((f"获取元素 name 失败，automation_id: {automation_id}，错误信息: {str(e)}"))

    def _trigger_and_switch_to_post_process(self, timeout=30):
        # 获取当前窗口句柄
        original_window = self.driver.current_window_handle

        # 点击菜单触发保存操作
        self.click((By.NAME, "文件"))
        post_process_locator = (By.NAME, "实时后处理")
        self.force_click(post_process_locator)

        # 等待新窗口出现并切换到该窗口
        if not self._switch_to_new_window(original_window, timeout):
            print("未能切换到新窗口")
            return False

        # 等待"实时后处理设置"窗口完全加载
        window_title = "实时后处理设置"
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.NAME, window_title))
            )
            return True
        except TimeoutException:
            print(f"等待窗口 '{window_title}' 加载超时")
            return False

    def switch_post_process(self, timeout=30):
        # 在流程最开始获取并保存原始窗口句柄
        original_window = self.driver.current_window_handle
        # print(f"切换实时后处理设置窗口，原始窗口句柄: {original_window}")

        try:
            if not self._trigger_and_switch_to_post_process(timeout):
                return False
            # print("打印窗口HTML内容:\n" + self.driver.page_source)
            return True

        except Exception as e:
            print(f"切换实时后处理设置窗口发生错误: {str(e)}")
            self.take_screenshot("post_process_timeout_Failed")
            # 出错时确保切换回操作界面窗口
            self._ensure_operation_window()
            return False

    def set_post_process_enable(self):
        post_process_enable_locator = (MobileBy.ACCESSIBILITY_ID, "isEnablePostProcessCb")
        is_checked = self.get_checkbox_status(post_process_enable_locator)
        if not is_checked:
            self.click(post_process_enable_locator)

    def set_post_process_disable(self):
        post_process_disable_locator = (MobileBy.ACCESSIBILITY_ID, "isEnablePostProcessCb")
        is_checked = self.get_checkbox_status(post_process_disable_locator)
        if is_checked:
            self.click(post_process_disable_locator)

    def set_gpu_computation_enable(self):
        gpu_computation_enable_locator = (MobileBy.ACCESSIBILITY_ID, "isEnableGPUCb")
        is_checked = self.get_checkbox_status(gpu_computation_enable_locator)
        if not is_checked:
            self.click(gpu_computation_enable_locator)

    def set_gpu_computation_disable(self):
        gpu_computation_disable_locator = (MobileBy.ACCESSIBILITY_ID, "isEnableGPUCb")
        is_checked = self.get_checkbox_status(gpu_computation_disable_locator)
        if is_checked:
            self.click(gpu_computation_disable_locator)

    def set_global_buffer_enable(self):
        global_buffer_enable_locator = (MobileBy.ACCESSIBILITY_ID, "UseGlobalBufferCb")
        is_checked = self.get_checkbox_status(global_buffer_enable_locator)
        if not is_checked:
            self.click(global_buffer_enable_locator)

    def set_global_buffer_disable(self):
        global_buffer_disable_locator = (MobileBy.ACCESSIBILITY_ID, "UseGlobalBufferCb")
        is_checked = self.get_checkbox_status(global_buffer_disable_locator)
        if is_checked:
            self.click(global_buffer_disable_locator)

    # 范围检查相关方法
    def add_range_check(self):
        range_check_button = (MobileBy.ACCESSIBILITY_ID, "AddRangeCheckBtn")
        self.click(range_check_button)

    def set_range_check_center_x(self, input_value):
        center_x_locator = (By.XPATH, "//Edit[@AutomationId='CircleCenterXTb']")
        self.double_click(center_x_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_center_y(self, input_value):
        center_y_locator = (By.XPATH, "//Edit[@AutomationId='CircleCenterYTb']")
        self.double_click(center_y_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_inner_radius(self, input_value):
        inner_radius_locator = (By.XPATH, "//Edit[@AutomationId='InnerCircleRadiusTb']")
        self.double_click(inner_radius_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_outer_radius(self, input_value):
        outer_radius_locator = (By.XPATH, "//Edit[@AutomationId='OuterCircleRadiusTb']")
        self.double_click(outer_radius_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_x_min(self, input_value):
        x_min_locator = (By.XPATH, "//Edit[@AutomationId='XMinTb']")    
        self.double_click(x_min_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_x_max(self, input_value):
        x_max_locator = (By.XPATH, "//Edit[@AutomationId='XMaxTb']")
        self.double_click(x_max_locator)    
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_y_min(self, input_value):
        y_min_locator = (By.XPATH, "//Edit[@AutomationId='YMinTb']")    
        self.double_click(y_min_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_y_max(self, input_value):
        y_max_locator = (By.XPATH, "//Edit[@AutomationId='YMaxTb']")
        self.double_click(y_max_locator)            
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_z_min(self, input_value):
        z_min_locator = (By.XPATH, "//Edit[@AutomationId='ZMinTb']")
        self.double_click(z_min_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_z_max(self, input_value):
        z_max_locator = (By.XPATH, "//Edit[@AutomationId='ZMaxTb']")
        self.double_click(z_max_locator)
        pg.press("backspace")
        pg.write(input_value)

    # 去飞点相关方法
    def add_remove_burrs(self):
        remove_burrs_button = (MobileBy.ACCESSIBILITY_ID, "AddRemoveBurrsBtn")
        self.click(remove_burrs_button)

    def set_remove_burrs_win_size(self, input_value):#窗口尺寸
        win_size_locator = (By.XPATH, "//Pane[@AutomationId='WinSizeSettingItem']//Edit")
        self.double_click(win_size_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_remove_burrs_win_size2(self, input_value):#次窗口
        win_size2_locator = (By.XPATH, "//Pane[@AutomationId='WinSize2SettingItem']//Edit")
        self.double_click(win_size2_locator)
        pg.press("backspace")
        pg.write(input_value)
    
    def set_remove_burrs_slope_level(self, input_value):#斜率
        slope_level_locator = (By.XPATH, "//Pane[@AutomationId='SlopeLevelSettingItem']//Edit")
        self.double_click(slope_level_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_remove_burrs_neighbor_close_level(self, input_value):#邻近阈值
        neighbor_close_level_locator = (By.XPATH, "//Pane[@AutomationId='NeighborCloseLevelSettingItem']//Edit")
        self.double_click(neighbor_close_level_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_remove_burrs_neighbor_num_level(self, input_value):#邻近数量
        neighbor_num_level_locator = (By.XPATH, "//Pane[@AutomationId='NeighborNumLevelSettingItem']//Edit")
        self.double_click(neighbor_num_level_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_remove_burrs_edge_suppress_level(self, input_value):#抑制窄边
        edge_suppress_level_locator = (By.XPATH, "//Pane[@AutomationId='EdgeSuppressLevelSettingItem']//Edit")
        self.double_click(edge_suppress_level_locator)
        pg.press("backspace")
        pg.write(input_value)
        
    # 填补相关方法
    def add_mend(self):
        """勾选后处理_填补"""
        mend_button = (By.XPATH, "//Button[@AutomationId='AddMendBtn']")
        self.click(mend_button)
        
    def set_mend_win_size(self, input_value):#窗口尺寸
        win_size_locator = (By.XPATH, "//Pane[@AutomationId='WinSizeSettingItem2']//Edit")
        self.double_click(win_size_locator)
        pg.press("backspace")
        pg.write(input_value)
        
    def set_mend_win_size2(self, input_value):#次窗口尺寸
        win_size2_locator = (By.XPATH, "//Pane[@AutomationId='WinSize2SettingItem2']//Edit")
        self.double_click(win_size2_locator)
        pg.press("backspace")
        pg.write(input_value)
        
    def set_mend_method(self, input_value):#填补方法
        method_locator = (By.XPATH, "//Pane[@AutomationId='methodTb']//Edit")
        self.double_click(method_locator)
        pg.press("backspace")
        pg.write(input_value)

    # 平滑相关方法
    def add_filtrate(self):
        """勾选后处理_平滑"""
        filtrate_button = (By.XPATH, "//Button[@AutomationId='AddFiltrateBtn']")
        self.click(filtrate_button)

    def set_filtrate_win_size(self, input_value):#窗口尺寸
        win_size_locator = (By.XPATH, "//Pane[@AutomationId='WinSizeSettingItem3']//Edit")
        self.double_click(win_size_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_filtrate_neighbor_close_level(self, input_value):#邻近阈值
        neighbor_close_level_locator = (By.XPATH, "//Pane[@AutomationId='NeighborCloseLevelSettingItem2']//Edit")
        self.double_click(neighbor_close_level_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_filtrate_neighbor_num_level(self, input_value):#邻近数量
        neighbor_num_level_locator = (By.XPATH, "//Pane[@AutomationId='NeighborNumLevelSettingItem2']//Edit")
        self.double_click(neighbor_num_level_locator)
        pg.press("backspace")
        pg.write(input_value)
        
    def post_process_list(self):#后处理列表第一项
        first_item_locator = (By.XPATH, "//ListItem[1]")
        self.click(first_item_locator)
        
    def post_process_move_up(self):
        move_up_button = (By.XPATH, "//Button[@AutomationId='MoveUpBtn']")
        self.click(move_up_button)
        
    def post_process_move_down(self):
        move_down_button = (By.XPATH, "//Button[@AutomationId='MoveDownBtn']")
        self.click(move_down_button)
        
    def post_process_load_setting(self, setting_name):
        load_setting_button = (By.XPATH, "//Button[@AutomationId='LoadRealtimeSettingBtn']")
        self.click(load_setting_button)
        if not self.navigate_to_read_directory():
            return False
        self.click((By.NAME, setting_name), timeout=10)
        self.click((By.NAME, "打开(O)"))
        return True

    def post_process_save_setting(self, setting_name, timeout=10):
        save_setting_button = (By.XPATH, "//Button[@AutomationId='SaveRealtimeSettingBtn']")
        self.click(save_setting_button)
        if not self.navigate_to_save_directory():
            return False

        if not self._input_file_name(setting_name, timeout, "save_setting_input_error"):
            return False

        self.click((By.NAME, "保存(S)"))
        return True

    def post_process_delete(self):
        delete_button = (By.XPATH, "//Button[@AutomationId='DeleteBtn']")
        self.click(delete_button)
      
    def post_process_clear(self):
        clear_button = (By.XPATH, "//Button[@AutomationId='ClearBtn']")
        self.click(clear_button)

    def post_process_confirm(self):
        confirm_button = (By.XPATH, "//Button[@AutomationId='ConfirmBtn']")
        self.click(confirm_button)

    def quit(self):
        if self.driver:
            get_driver_manager().quit_driver()
            self.driver = None
            MenuPage._instance = None

