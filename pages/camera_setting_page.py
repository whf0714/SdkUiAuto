from lib2to3.fixes.fix_imports import alternates
from time import sleep

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

# 导入配置文件中的路径
from config.config import SCREENSHOTS_DIR



class CameraSettingPage:
    def __init__(self):
        # 使用驱动管理器获取驱动实例
        pass


    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # 使用驱动管理器获取驱动实例
            cls._instance.driver = get_driver_manager().get_driver()
            cls._instance._initialize_device_status()  # 单例初始化时自动检查设备状态
        return cls._instance


    def _initialize_device_status(self):
        """单例初始化时自动检查设备状态 - CameraSettingPage需要确保设备处于运行状态"""
        time.sleep(1)
        device_status_button_x = 113
        device_status_button_y = 1384
        device_status_button_color = pg.pixel(device_status_button_x, device_status_button_y)
        device_status_button_color_hold = (176, 28, 58)   # 运行状态颜色 (绿色)
        device_status_button_color_run = (77, 133, 72)  # 暂停状态颜色 (红色)

        # Camera页面需要确保设备处于运行状态
        if device_status_button_color == device_status_button_color_hold:
            # 如果设备在暂停状态，则点击切换到运行状态
            pg.click(device_status_button_x, device_status_button_y)
        elif device_status_button_color == device_status_button_color_run:
            # 设备已经处于运行状态，不需要操作
            pass
        else:
            self.take_screenshot("UnexpectedColor")
            raise RuntimeError(
                f"Unexpected color detected {device_status_button_color} at ({device_status_button_x}, {device_status_button_y})"
            )
    # ======================================================================================================

    def open_sdk(self, server, desired_caps):
        self.driver = webdriver.Remote(command_executor=server, desired_capabilities=desired_caps)

    def _wait_until_clickable(self, locator, timeout=10):
        """Helper method to wait until an element is clickable."""
        # return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.take_screenshot("element_not_clickable")
            raise

    def click(self, locator, timeout=10, ignore_timeout=False):
        """Click on the specified element after waiting for it to be clickable."""
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
        """Double-click on the specified element after waiting for it to be clickable."""
        try:
            element = self._wait_until_clickable(locator, timeout)
            ActionChains(self.driver).double_click(element).perform()
        except TimeoutException:
            if not ignore_timeout:
                raise
            print(f"Timeout while waiting for {locator} to be clickable.")

    def trigger_camera(self):
        trigger_locator = (By.NAME, "发送软件触发")
        self.click(trigger_locator)

    def wait_for_standby(self, timeout=10):
        # standby_locator = (By.XPATH, "//StatusBar[@AutomationId='DeviceInfoSts']//Text[@Name='  StandBy  ']")
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
            print("The current device status is not 'StandBy' ")
            # print(self.driver.page_source)  # 打印当前页面的HTML以供排查
            return None

    def take_screenshot(self, name):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        file_path = os.path.join(SCREENSHOTS_DIR, file_name)
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved as {file_path}")
        # file_path = os.path.join(r"../../screenshots", file_name)
        # screenshot_file_path = os.path.abspath(file_path)
        # self.driver.save_screenshot(screenshot_file_path)
        # print(f"Screenshot saved as {screenshot_file_path}")

    def get_checkbox_status(self, locator):
        checkbox = self.driver.find_element(*locator)
        return checkbox.is_selected()

    def set_fast(self):
        fast_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeFastRbt")
        self.click(fast_locator)

    def set_standard(self):
        standard_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeStandardRbt")
        self.click(standard_locator)

    def set_precise(self):
        precise_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModePreciseRbt")
        self.click(precise_locator)

    def set_super_precise(self):
        super_precise_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeSuperPreciseRbt")
        self.click(super_precise_locator)

    def set_white(self):
        white_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeWhiteRbt")
        self.click(white_locator)

    def set_grid(self):
        grid_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeGridRbt")
        self.click(grid_locator)

    def set_black(self):
        black_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeBlackRbt")
        self.click(black_locator)

    def set_exposure_prediction(self):
        exposure_prediction_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeExposurePredictionRbt")
        self.click(exposure_prediction_locator)

    def set_binning_enable(self):
        binning_enable_locator = (MobileBy.ACCESSIBILITY_ID, "BinningStateCkb")
        is_checked = self.get_checkbox_status(binning_enable_locator)
        if not is_checked:
            self.click(binning_enable_locator)

    def set_binning_disable(self):
        binning_disable_locator = (MobileBy.ACCESSIBILITY_ID, "BinningStateCkb")
        is_checked = self.get_checkbox_status(binning_disable_locator)
        if is_checked:
            self.click(binning_disable_locator)

    def set_roi_x_star(self, input_value):
        roi_x_star_locator = (By.XPATH, "//Pane[@AutomationId='panel64']//Pane[@Name='X起始:']//Edit")
        self.double_click(roi_x_star_locator)
        pg.press("backspace")
        pg.write(input_value)
        
    def set_roi_y_star(self, input_value):
        roi_y_star_locator = (By.XPATH, "//Pane[@AutomationId='panel63']//Pane[@Name='Y起始:']//Edit")
        self.double_click(roi_y_star_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_roi_width(self, input_value):
        roi_width_locator= (By.XPATH, "//Pane[@AutomationId='panel62']//Pane[@Name='宽度:']//Edit")
        self.double_click(roi_width_locator)
        pg.press("backspace")
        pg.write(input_value)
        
    def set_roi_height(self, input_value):
        roi_height_locator = (By.XPATH, "//Pane[@AutomationId='panel61']//Pane[@Name='高度:']//Edit")
        self.double_click(roi_height_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_soft_trigger(self):
        soft_trigger_locator = (MobileBy.ACCESSIBILITY_ID, "TriggerSourceSWRbt")
        self.click(soft_trigger_locator)

    def set_auto_trigger(self):
        auto_trigger_locator = (MobileBy.ACCESSIBILITY_ID, "TriggerSourceATRbt")
        self.click(auto_trigger_locator)

    def set_hard_trigger_0(self):
        hard_trigger_0_locator = (MobileBy.ACCESSIBILITY_ID, "TriggerSourceI0Rbt")
        self.click(hard_trigger_0_locator)

    def set_hard_trigger_1(self):
        hard_trigger_1_locator = (MobileBy.ACCESSIBILITY_ID, "TriggerSourceI1Rbt")
        self.click(hard_trigger_1_locator)

#################测试投影模式（自定义组合）##############################
    def toggle_projector(self, projector_index, check_projector=True):
        """
        设置特定的投影模式（选择或取消选择）
        :param projector_index: 投影的索引（0-3）
        :param check_projector: 是否选择投影（True为选择，False为取消选择）
        """
        projector_locator = (MobileBy.ACCESSIBILITY_ID, f"Proj{projector_index}EnableCbx")
        if check_projector != self.get_checkbox_status(projector_locator):
            self.click(projector_locator)

    def set_all_projectors(self, select_all=False):
        """
        设置所有投影模式（全选或全不选）
        :param select_all: 是否全选（True为全选，False为全不选）
        """
        for i in range(4):
            self.toggle_projector(i, select_all)

    def set_single_projector(self, projector_index):
        """
        只选择单个投影，并取消其他所有投影的选择
        :param projector_index: 要选择的投影索引（0-3）
        """
        self.set_all_projectors(False)  # 先取消所有已选投影
        self.toggle_projector(projector_index, True)  # 选择特定的投影

    def set_multiple_projector(self, projector_indices):
        """
        选择多个投影，并取消其他所有投影的选择
        :param projector_indices: 要选择的投影索引列表（0-3）
        """
        self.set_all_projectors(False)  # 先取消所有已选投影
        for index in projector_indices:
            self.toggle_projector(index, True)  # 选择特定的投影

    def set_merge_parameters_th(self, input_value):
        merge_parameters_th_locator = (By.XPATH, "//Pane[@AutomationId='panel53']//Pane[@Name='阈值:']//Edit")
        self.double_click(merge_parameters_th_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_merge_parameters_num(self, input_value):
        merge_parameters_num_locator = (By.XPATH, "//Pane[@AutomationId='panel57']//Pane[@Name='数量:']//Edit")
        self.double_click(merge_parameters_num_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_exposure_mode_manual(self):
        manual_locator = (MobileBy.ACCESSIBILITY_ID, "ExposureModeManualRbt")
        self.click(manual_locator)

    def set_exposure_mode_manual_repeat(self):
        manual_repeat_locator = (MobileBy.ACCESSIBILITY_ID, "ExposureModeManualRepeatRbt")
        self.click(manual_repeat_locator)

    def set_exposure_mode_auto_nhdr(self):
        auto_nhdr_locator = (MobileBy.ACCESSIBILITY_ID, "ExposureModeAutoNHDRRbt")
        self.click(auto_nhdr_locator)

    def set_exposure_mode_auto_phdr(self):
        auto_phdr_locator = (MobileBy.ACCESSIBILITY_ID, "ExposureModeAutoPHDRRbt")
        self.click(auto_phdr_locator)


    def toggle_collapse(self, locator, collapse_text, timeout=10):
        try:
            # 等待直到元素可见
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            # 找到元素并获取其文本
            element = self.driver.find_element(*locator)
            element_text = element.text
            # 打印元素文本，用于调试
            # print(f"Element text is: {element_text}")
            # 如果元素文本去掉前后空格后与 collapse_text 一致，则点击元素
            if element_text.strip() == collapse_text:
                element.click()
                # 用于调试
                # print(f"Clicked on element with text: {collapse_text}")
            else:
                # 用于调试
                # print(f"Element text matches '{collapse_text}', skipping click.")
                pass
        except TimeoutException:
            print(f"Element with locator {locator} not visible within {timeout} seconds.")
        # except Exception as e:
        #     print(f"An error occurred: {e}")

    def collapse_basic(self):
        # 定义定位器和需要匹配的文本
        basic_locator = (MobileBy.ACCESSIBILITY_ID, "BasicLbl")
        collapse_text = '▼ 基本'
        # 调用 toggle_collapse 方法来折叠'▼ 基本'
        self.toggle_collapse(basic_locator, collapse_text)

    def collapse_multi_head(self):
        # 定义定位器和需要匹配的文本
        multi_head_locator = (MobileBy.ACCESSIBILITY_ID, "MultiHeadLbl")
        collapse_text = '▼ 多头'
        # 调用 toggle_collapse 方法来折叠'▼ 多头'
        self.toggle_collapse(multi_head_locator, collapse_text)

    def collapse_exposure(self):
        # 定义定位器和需要匹配的文本
        exposure_locator = (MobileBy.ACCESSIBILITY_ID, "ExposureLbl")
        collapse_text = "▼ 曝光"
        # 调用 toggle_collapse 方法来折叠'▼ 曝光'
        self.toggle_collapse(exposure_locator, collapse_text)

    def collapse_external_exposure(self):
        external_exposure_locator = (MobileBy.ACCESSIBILITY_ID, "ExternalExposureLbl")
        collapse_text = "▼ 外部曝光"
        # 调用 toggle_collapse 方法来折叠'▼ 外部曝光'
        self.toggle_collapse(external_exposure_locator, collapse_text)

    def collapse_reconstruction(self):
        reconstruction_locator = (MobileBy.ACCESSIBILITY_ID, "ReconstructionLbl")
        collapse_text = '▼ 重构'
        self.toggle_collapse(reconstruction_locator, collapse_text)

    def collapse_post_process(self):
        post_process_locator = (MobileBy.ACCESSIBILITY_ID, "PostProcessLbl")
        collapse_text = '▼ 后处理'
        self.toggle_collapse(post_process_locator, collapse_text)

    def expand_basic(self):
        basic_locator = (MobileBy.ACCESSIBILITY_ID, "BasicLbl")
        collapse_text = '► 基本'
        self.toggle_collapse(basic_locator, collapse_text)

    def expand_external_exposure(self):
        external_exposure_locator = (MobileBy.ACCESSIBILITY_ID, "ExternalExposureLbl")
        collapse_text = '► 外部曝光'
        self.toggle_collapse(external_exposure_locator, collapse_text)

    def expand_reconstruction(self):
        reconstruction_locator = (MobileBy.ACCESSIBILITY_ID, "ReconstructionLbl")
        collapse_text = '► 重构'
        self.toggle_collapse(reconstruction_locator, collapse_text)
        # print(self.driver.page_source)

    def expand_post_process(self):
        post_process_locator = (MobileBy.ACCESSIBILITY_ID, "PostProcessLbl")
        collapse_text = '► 后处理'
        self.toggle_collapse(post_process_locator, collapse_text)

    def scroll_down(self):
        scroll_locator = (MobileBy.ACCESSIBILITY_ID, "NonClientVerticalScrollBar")
        self.click(scroll_locator)
        pg.scroll(-100)


    def expand_io(self):
        io_locator = (MobileBy.ACCESSIBILITY_ID, "IOSettingPnl")
        collapse_text = '► I/O'
        self.toggle_collapse(io_locator, collapse_text)

    def set_exposure_num_single(self):
        exposure_num_single_locator = (MobileBy.ACCESSIBILITY_ID, "SingleExposureRbt")
        self.click(exposure_num_single_locator)

    def set_exposure_num_double(self):
        exposure_num_double_locator = (MobileBy.ACCESSIBILITY_ID, "DoubleExposureRbt")
        self.click(exposure_num_double_locator)

    def set_exposure_num_triple(self):
        exposure_num_triple_locator = (MobileBy.ACCESSIBILITY_ID, "TripleExposureRbt")
        self.click(exposure_num_triple_locator)

    def set_gain(self, input_value):
        gain_locator = (By.XPATH, "//Pane[@AutomationId='GainPnl']//Pane[@Name='用户增益']//Edit")
        self.double_click(gain_locator)
        pg.press("backspace")
        pg.write(input_value)


    def set_3d_exposure_i_1st(self, input_value):
        exposure_i_3d_1st_locator = (By.XPATH, "//Pane[@AutomationId='panel17']//Pane[@Name='第1次']//Edit")
        self.double_click(exposure_i_3d_1st_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_3d_exposure_i_2nd(self, input_value):
        exposure_i_3d_2nd_locator = (By.XPATH, "//Pane[@AutomationId='panel18']//Pane[@Name='第2次']//Edit")
        self.double_click(exposure_i_3d_2nd_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_3d_exposure_i_3rd(self, input_value):
        exposure_i_3d_3rd_locator = (By.XPATH, "//Pane[@AutomationId='panel19']//Pane[@Name='第3次']//Edit")
        self.double_click(exposure_i_3d_3rd_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_2d_exposure_i(self, input_value):
        exposure_i_2d_locator = (By.XPATH, "//Pane[@AutomationId='panel23']//Pane[@Name=' ● 2D曝光强度']//Edit")
        self.double_click(exposure_i_2d_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_auto_hdr_priority(self, input_value):
        auto_hdr_priority_locator = (By.XPATH, "//Pane[@AutomationId='panel2']//Pane[@Name='优先级']//Edit")
        self.double_click(auto_hdr_priority_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_auto_hdr_quality(self, input_value):
        auto_hdr_priority_locator = (By.XPATH, "//Pane[@AutomationId='AutoPHDRQualityMPInt']//Edit")
        self.double_click(auto_hdr_priority_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_multi_head_exposure_variance_enable(self):
        multi_head_exposure_variance_enable_locator = (MobileBy.ACCESSIBILITY_ID, "MultiHeadExpoVarEnable")
        self.click(multi_head_exposure_variance_enable_locator)

    def set_multi_head_exposure_variance_01(self):
        multi_head_exposure_variance_01_locator = (MobileBy.ACCESSIBILITY_ID, "MultiHeadExpoVarMode0")
        self.click(multi_head_exposure_variance_01_locator)

    def set_multi_head_exposure_variance_23(self):
        multi_head_exposure_variance_23_locator = (MobileBy.ACCESSIBILITY_ID, "MultiHeadExpoVarMode1")
        self.click(multi_head_exposure_variance_23_locator)

    def set_multi_head_exposure_variance_02(self):
        multi_head_exposure_variance_02_locator = (MobileBy.ACCESSIBILITY_ID, "MultiHeadExpoVarMode2")
        self.click(multi_head_exposure_variance_02_locator)

    def set_multi_head_exposure_variance_13(self):
        multi_head_exposure_variance_13_locator = (MobileBy.ACCESSIBILITY_ID, "MultiHeadExpoVarMode3")
        self.click(multi_head_exposure_variance_13_locator)

    def set_multi_head_exposure_variance_ratio(self, input_value):
        multi_head_exposure_variance_ratio_locator = (By.XPATH, "//Pane[@AutomationId='MultiHeadExpoVarRatioPnl']//Edit")
        self.double_click(multi_head_exposure_variance_ratio_locator)
        pg.press("backspace")
        pg.write(input_value)

    def toggle_exposure_enable(self, exposure_enable_type, enable):
        """
        切换白光或RGB使能的状态
        :param exposure_enable_type: 'white' 或 'rgb' 表示要切换的外部曝光使能
        :param enable: True 表示选择使能，False 表示取消使能
        """
        locators = {
            'white': (MobileBy.ACCESSIBILITY_ID, "AuxWhiteEnableCkb"),
            'rgb': (MobileBy.ACCESSIBILITY_ID, "AuxRGBEnableCkb")
        }
        locator = locators.get(exposure_enable_type)
        if locator:
            if enable != self.get_checkbox_status(locator):
                self.click(locator)

    def set_all_exposure_enable(self, enable_all):
        """
        设置所有灯光使能的状态（全选或全不选）
        :param enable_all: True 表示全选，False 表示全不选
        """
        for light_type  in ['white', 'rgb']:
            self.toggle_exposure_enable(light_type , enable_all)

    def set_single_exposure_enable(self, exposure_enable_type):
        """
        只选择单个外部曝光使能，并取消另一个外部曝光使能
        :param exposure_enable_type: 'white' 或 'rgb' 表示要切换的外部曝光使能
        """
        # self.set_all_exposure_enable(False)  # 先取消所有已选投影
        # self.toggle_exposure_enable(exposure_enable_type, True)  # 选择特定的投影
        for light_type  in ['white', 'rgb']:
            self.toggle_exposure_enable(light_type , light_type  == exposure_enable_type)

    def set_external_exposure_time_white(self, input_value):
        time_white_locator = (By.XPATH, "//Pane[@AutomationId='panel46']//Pane[@Name='白照明']//Edit")
        self.double_click(time_white_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_external_exposure_time_red(self, input_value):
        time_white_locator = (By.XPATH, "//Pane[@AutomationId='panel47']//Pane[@Name='红照明']//Edit")
        self.double_click(time_white_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_external_exposure_time_green(self, input_value):
        time_white_locator = (By.XPATH, "//Pane[@AutomationId='panel48']//Pane[@Name='绿照明']//Edit")
        self.double_click(time_white_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_external_exposure_time_blue(self, input_value):
        time_white_locator = (By.XPATH, "//Pane[@AutomationId='panel49']//Pane[@Name='蓝照明']//Edit")
        self.double_click(time_white_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_external_exposure_gain_white(self, input_value):
        gain_white_locator = (By.XPATH, "//Pane[@AutomationId='panel41']//Pane[@Name='白照明']//Edit")
        self.double_click(gain_white_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_external_exposure_gain_red(self, input_value):
        gain_white_locator = (By.XPATH, "//Pane[@AutomationId='panel42']//Pane[@Name='红照明']//Edit")
        self.double_click(gain_white_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_external_exposure_gain_green(self, input_value):
        gain_white_locator = (By.XPATH, "//Pane[@AutomationId='panel44']//Pane[@Name='绿照明']//Edit")
        self.double_click(gain_white_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_external_exposure_gain_blue(self, input_value):
        gain_white_locator = (By.XPATH, "//Pane[@AutomationId='panel45']//Pane[@Name='蓝照明']//Edit")
        self.double_click(gain_white_locator)
        pg.press("backspace")
        pg.write(input_value)


    def set_over_exposure_filter_manual(self):
        manual_locator = (MobileBy.ACCESSIBILITY_ID, "OverExposureFilterManualRbt")
        self.click(manual_locator)

    def set_over_exposure_filter_auto(self):
        auto_locator = (MobileBy.ACCESSIBILITY_ID, "OverExposureFilterAutoRbt")
        self.click(auto_locator)

    def set_over_exposure_filter_th(self, input_value):
        th_locator = (By.XPATH, "//Pane[@AutomationId='OverExposureFilterManualMPint']//Edit")
        self.double_click(th_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_valid_point_judgement_th0(self, input_value):
        th0_locator = (By.XPATH, "//Pane[@AutomationId='ValidPointTh0MPInt']//Edit")
        self.double_click(th0_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_valid_point_judgement_th1(self, input_value):
        th1_locator = (By.XPATH, "//Pane[@AutomationId='ValidPointTh1MPInt']//Edit")
        self.double_click(th1_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_burr_removal_filter_th0(self, input_value):
        th0_locator = (By.XPATH, "//Pane[@AutomationId='BurrRemovalTh0MPInt']//Edit")
        self.double_click(th0_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_burr_removal_filter_th1(self, input_value):
        th1_locator = (By.XPATH, "//Pane[@AutomationId='BurrRemovalTh1MPInt']//Edit")
        self.double_click(th1_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_pre_process_num(self, input_value):
        num_locator = (By.XPATH, "//Pane[@AutomationId='PreProcessLoopNumMPInt']//Edit")
        self.double_click(num_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_pre_process_th(self, input_value):
        th_locator = (By.XPATH, "//Pane[@AutomationId='PreProcessThMPInt']//Edit")
        self.double_click(th_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_float_point_cloud(self):
        float_locator = (MobileBy.ACCESSIBILITY_ID, "DataOutModeFloatRbt")
        self.click(float_locator)

    def set_fix_point_cloud(self):
        fix_locator = (MobileBy.ACCESSIBILITY_ID, "DataOutModeFixRbt")
        self.click(fix_locator)

    def set_fix_z_map(self):
        z_map_locator = (MobileBy.ACCESSIBILITY_ID, "DataOutModeZMapRbt")
        self.click(z_map_locator)

    def set_fix_z_map_simple(self):
        z_map_simple_locator = (MobileBy.ACCESSIBILITY_ID, "DataOutModeZMapSimpleRbt")
        self.click(z_map_simple_locator)

    def set_rt_matrix(self):
        rt_matrix_locator = (MobileBy.ACCESSIBILITY_ID, "panel11")
        self.click(rt_matrix_locator)


    def set_rt_matrix_enable(self):
        rt_enable_locator = (MobileBy.ACCESSIBILITY_ID, "RTMatrixEnableCkb")
        is_checked = self.get_checkbox_status(rt_enable_locator)
        if not is_checked:
            self.click(rt_enable_locator)

    def set_rt_matrix_disable(self):
        rt_disable_locator = (MobileBy.ACCESSIBILITY_ID, "RTMatrixEnableCkb")
        is_checked = self.get_checkbox_status(rt_disable_locator)
        if is_checked:
            self.click(rt_disable_locator)

    def set_theta_x(self, input_value):
        theta_x_locator = (By.XPATH, "//Pane[@AutomationId='panel13']//Edit")
        self.double_click(theta_x_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_theta_y(self, input_value):
        theta_y_locator = (By.XPATH, "//Pane[@AutomationId='panel14']//Edit")
        self.double_click(theta_y_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_theta_z(self, input_value):
        theta_z_locator = (By.XPATH, "//Pane[@AutomationId='panel15']//Edit")
        self.double_click(theta_z_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_kx(self, input_value):
        kx_locator = (By.XPATH, "//Pane[@AutomationId='panel16']//Edit")
        self.double_click(kx_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_ky(self, input_value):
        ky_locator = (By.XPATH, "//Pane[@AutomationId='panel20']//Edit")
        self.double_click(ky_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_kz(self, input_value):
        kz_locator = (By.XPATH, "//Pane[@AutomationId='panel22']//Edit")
        self.double_click(kz_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_bx(self, input_value):
        bx_locator = (By.XPATH, "//Pane[@AutomationId='panel24']//Edit")
        self.double_click(bx_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_by(self, input_value):
        by_locator = (By.XPATH, "//Pane[@AutomationId='panel27']//Edit")
        self.double_click(by_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_bz(self, input_value):
        bz_locator = (By.XPATH, "//Pane[@AutomationId='panel30']//Edit")
        self.double_click(bz_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)


    def set_x0_position(self, input_value):
        x0_position_locator = (By.XPATH, "//Pane[@AutomationId='DataScaleX0FVTbx']//Edit")
        self.double_click(x0_position_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_x_increment(self, input_value):
        x_increment_locator = (By.XPATH, "//Pane[@AutomationId='DataScaleXIncFVTbx']//Edit")
        self.double_click(x_increment_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_y0_position(self, input_value):
        y0_position_locator = (By.XPATH, "//Pane[@AutomationId='DataScaleY0FVTbx']//Edit")
        self.double_click(y0_position_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_y_increment(self, input_value):
        y_increment_locator = (By.XPATH, "//Pane[@AutomationId='DataScaleYIncFVTbx']//Edit")
        self.double_click(y_increment_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_z0_position(self, input_value):
        z0_position_locator = (By.XPATH, "//Pane[@AutomationId='DataScaleZ0FVTbx']//Edit")
        self.double_click(z0_position_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_z_increment(self, input_value):
        z_increment_locator = (By.XPATH, "//Pane[@AutomationId='DataScaleZIncFVTbx']//Edit")
        self.double_click(z_increment_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_enable(self):
        rc_enable_locator = (MobileBy.ACCESSIBILITY_ID, "RangeCheckEnableCkb")
        is_checked = self.get_checkbox_status(rc_enable_locator)
        if not is_checked:
            self.click(rc_enable_locator)

    def set_range_check_disable(self):
        rc_disable_locator = (MobileBy.ACCESSIBILITY_ID, "RangeCheckEnableCkb")
        is_checked = self.get_checkbox_status(rc_disable_locator)
        if is_checked:
            self.click(rc_disable_locator)

    def set_range_check_x_min(self, input_value):
        x_min_locator = (By.XPATH, "//Pane[@AutomationId='RangeCheckXMinFVTbx']//Edit")
        self.double_click(x_min_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_x_max(self, input_value):
        x_max_locator = (By.XPATH, "//Pane[@AutomationId='RangeCheckXMaxFVTbx']//Edit")
        self.double_click(x_max_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_y_min(self, input_value):
        y_min_locator = (By.XPATH, "//Pane[@AutomationId='RangeCheckYMinFVTbx']//Edit")
        self.double_click(y_min_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_y_max(self, input_value):
        y_max_locator = (By.XPATH, "//Pane[@AutomationId='RangeCheckYMaxFVTbx']//Edit")
        self.double_click(y_max_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_z_min(self, input_value):
        z_min_locator = (By.XPATH, "//Pane[@AutomationId='RangeCheckZMinFVTbx']//Edit")
        self.double_click(z_min_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)

    def set_range_check_z_max(self, input_value):
        z_max_locator = (By.XPATH, "//Pane[@AutomationId='RangeCheckZMaxFVTbx']//Edit")
        self.double_click(z_max_locator)
        pg.press("backspace")
        pg.press("backspace")
        pg.write(input_value)
        
        
    def set_auto_sleep_enable(self):
        as_enable_locator = (MobileBy.ACCESSIBILITY_ID, "AutoSleepEnableCkb")
        is_checked = self.get_checkbox_status(as_enable_locator)
        if not is_checked:
            self.click(as_enable_locator)

    def set_auto_sleep_disable(self):
        as_disable_locator = (MobileBy.ACCESSIBILITY_ID, "AutoSleepEnableCkb")
        is_checked = self.get_checkbox_status(as_disable_locator)
        if is_checked:
            self.click(as_disable_locator)

    def set_auto_sleep_setting(self, input_value):
        as_setting_locator = (By.XPATH, "//Pane[@AutomationId='AutoSleepDelayMPInt']//Edit")
        self.double_click(as_setting_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_correct_distortion_enable(self):
        cd_enable_locator = (MobileBy.ACCESSIBILITY_ID, "CorrectDistortionEnableCb")
        is_checked = self.get_checkbox_status(cd_enable_locator)
        if not is_checked:
            self.click(cd_enable_locator)

    def set_correct_distortion_disable(self):
        cd_enable_locator = (MobileBy.ACCESSIBILITY_ID, "CorrectDistortionEnableCb")
        is_checked = self.get_checkbox_status(cd_enable_locator)
        if is_checked:
            self.click(cd_enable_locator)


    def expert_setting_1enable(self):
        # self.click((By.NAME, "文件"))
        # self.click((By.NAME, "导入设备设置"))#######################问题1  找不到

        file_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "文件"))
        )
        file_button.click()

        # 模拟鼠标悬停在“文件”按钮上
        actions = ActionChains(self.driver)
        actions.move_to_element(file_button).perform()

        # 等待子菜单项的 visible 属性变为 True
        try:
            export_data_element = WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.NAME, "导出数据").get_attribute('visible') == 'True'
            )
            print("导出数据元素的HTML:")
            print(export_data_element.get_attribute('outerHTML'))
        except Exception as e:
            print("未能找到子菜单元素或子菜单元素不可见:", e)


    def expert_setting_enable(self):
        self.click((By.NAME, "文件"))
        time.sleep(2)
        enable_expert_locator = (By.NAME, "启用专业设置")
        self.force_click(enable_expert_locator)
        # pg.click(x=78, y=220) #点击'启用专业设置'
        # pg.click(x=74, y=248)  # 点击'实时后处理'
        # time.sleep(1)
        # pg.click(x=1136, y=757) #弹窗 启用专业设置
        # time.sleep(1)
        # pg.click(x=73, y=129) #切到专业设置tab

        apply_button = (By.XPATH, "//Button[@AutomationId='1']")
        self.click(apply_button)
        es_table = (By.XPATH, "//TabItem[@Name='专业设置']")
        self.click(es_table)

    def expert_setting_disable(self):
        self.click((By.NAME, "文件"))
        disable_expert_locator = (By.NAME, "启用专业设置")
        self.force_click(disable_expert_locator)
        # pg.click(x=78, y=220) #关闭'启用专业设置'

    def switch_setting_table(self):
        setting_button = (By.XPATH, "//TabItem[@Name='设置']")
        self.click(setting_button)

    def read_correct_distortion_parm(self):
        read_locator = (MobileBy.ACCESSIBILITY_ID, "ReadCorrectDistortionParamBtn")
        self.click(read_locator)

    def do_correct_distortion(self):
        do_locator = (MobileBy.ACCESSIBILITY_ID, "CorrectDistortionBtn")
        self.click(do_locator)
        apply_button = (By.XPATH, "//Button[@AutomationId='1']") ##################有问题，没有弹窗确认
        self.click(apply_button)

    def set_exp_roi_num(self,input_value):
        num_locator = (By.XPATH, "//Pane[@AutomationId='ExpROINumMPInt']//Edit")
        self.double_click(num_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_exp_roi_index(self,input_value):
        index_locator = (By.XPATH, "//Pane[@AutomationId='ExpROIIndexMPInt']//Edit")
        self.double_click(index_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_exp_roi_positive(self):
        positive_locator = (MobileBy.ACCESSIBILITY_ID, "PositiveRBtn")
        self.click(positive_locator)

    def set_exp_roi_negative(self):
        negative_locator = (MobileBy.ACCESSIBILITY_ID, "NegativeRBtn")
        self.click(negative_locator)

    def set_exp_roi_is_base_enable(self):
        is_base_enable_locator = (MobileBy.ACCESSIBILITY_ID, "ExpRoIIsBaseCkb")
        is_checked = self.get_checkbox_status(is_base_enable_locator)
        if not is_checked:
            self.click(is_base_enable_locator)

    def set_exp_roi_is_base_disable(self):
        is_base_disable_locator = (MobileBy.ACCESSIBILITY_ID, "ExpRoIIsBaseCkb")
        is_checked = self.get_checkbox_status(is_base_disable_locator)
        if is_checked:
            self.click(is_base_disable_locator)

    def  set_exp_roi_shape(self):
        shape_locator = (MobileBy.ACCESSIBILITY_ID, "ExpROIShapeCbx")
        self.click(shape_locator)
        # self.click(shape_locator)

        # 定位策略
        # shape_locator = (MobileBy.ACCESSIBILITY_ID, "ExpROIShapeCbx")
        # # 查找元素
        # shape_element = self.driver.find_element(*shape_locator)
        # # 获取元素的文本
        # selected_shape = shape_element.text
        # # 返回选中的形状
        # return selected_shape

    def set_exp_roi_x_center(self, input_value):
        x_center_locator = (By.XPATH, "//Pane[@AutomationId='XCenterMPInt']//Edit")
        self.double_click(x_center_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_exp_roi_y_center(self, input_value):
        y_center_locator = (By.XPATH, "//Pane[@AutomationId='YCenterMPInt']//Edit")
        self.double_click(y_center_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_exp_roi_width(self, input_value):
        width_center_locator = (By.XPATH, "//Pane[@AutomationId='WidthMPInt']//Edit")
        self.double_click(width_center_locator)
        pg.press("backspace")
        pg.write(input_value)

    def set_exp_roi_height(self, input_value):
        height_center_locator = (By.XPATH, "//Pane[@AutomationId='HeightMPInt']//Edit")
        self.double_click(height_center_locator)
        pg.press("backspace")
        pg.write(input_value)

 #################测试曝光抑制设置（自定义组合）##############################

    def toggle_suppress_exposure(self, suppress_index, check_suppress=True):
        """
        设置特定的曝光抑制（选择或取消选择）
        :param suppress_index: 抑制的索引（1-3）
        :param check_suppress: 是否选择抑制（True为选择，False为取消选择）
        """
        suppress_locator = (MobileBy.ACCESSIBILITY_ID, f"SuppressExpo{suppress_index}EnableCkb")
        if check_suppress != self.get_checkbox_status(suppress_locator):
            self.click(suppress_locator)

    def set_all_suppress_exposure(self, select_all=False):
        """
        设置所有曝光抑制（全选或全不选）
        :param select_all: 是否全选（True为全选，False为全不选）
        """
        for i in range(1, 4):
            self.toggle_suppress_exposure(i, select_all)

    def set_single_suppress_exposure(self, suppress_index):
        """
        只选择单个曝光抑制，并取消其他所有曝光抑制的选择
        :param suppress_index: 要选择的抑制索引（1-3）
        """
        self.set_all_suppress_exposure(False)  # 先取消所有已选抑制
        self.toggle_suppress_exposure(suppress_index, True)  # 选择特定的抑制

    def set_multiple_suppress_exposure(self, suppress_indices):
        """
        选择多个曝光抑制，并取消其他所有曝光抑制的选择
        :param suppress_indices: 要选择的抑制索引列表（1-3）
        """
        self.set_all_suppress_exposure(False)  # 先取消所有已选抑制
        for index in suppress_indices:
            self.toggle_suppress_exposure(index, True)  # 选择特定的抑制

    def set_flip_x(self):
        flip_x_locator = (MobileBy.ACCESSIBILITY_ID, "SetXFlipCb")
        self.click(flip_x_locator)
        apply_button = (By.XPATH, "//Button[@AutomationId='1']")
        self.click(apply_button)

    def set_flip_x_unselect(self):
        flip_x_locator = (MobileBy.ACCESSIBILITY_ID, "SetXFlipCb")
        self.click(flip_x_locator)

    def set_flip_y(self):
        flip_y_locator = (MobileBy.ACCESSIBILITY_ID, "SetYFlipCb")
        self.click(flip_y_locator)
        apply_button = (By.XPATH, "//Button[@AutomationId='1']")
        self.click(apply_button)

    def set_flip_y_unselect(self):
        flip_y_locator = (MobileBy.ACCESSIBILITY_ID, "SetYFlipCb")
        self.click(flip_y_locator)


    def quit(self):
        if self.driver:
            get_driver_manager().quit_driver()
            self.driver = None
            CameraSettingPage._instance = None