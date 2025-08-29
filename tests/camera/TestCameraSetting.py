# import unittest
# import pyautogui as pg
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from pages.camera_setting_page import CameraSettingPage
# import time
#
# class TestCameraSetting(unittest.TestCase):
#     camera_setting_page = None
#
#     @classmethod
#     def setUpClass(cls):
#         cls.camera_setting_page = CameraSettingPage()
#         cls.check_and_click_device_status()
#
#     @classmethod
#     def check_and_click_device_status(cls):
#         """检查当前设备状态并切换进入待机状态"""
#         time.sleep(1)
#         button_x = 116
#         button_y = 1349
#         button_color = pg.pixel(button_x, button_y)
#         hold_button_color = (77, 133, 72)
#         run_button_color = (176, 28, 58)
#         if button_color == run_button_color:
#             pg.click(button_x, button_y)  # 点击运行
#         elif button_color == hold_button_color:
#             pass
#         else:
#             # 如果出现意外颜色，则截图
#             cls.camera_setting_page.take_screenshot("UnexpectedColor")
#             print(f"错误: 检测到意外颜色 {button_color}，请检查【】/【点击运行】按钮坐标是否正确。")

        #     def test_trigger_camera(self):
        # """验证相机触发拍摄功能"""
        # self.camera_setting_page.trigger_camera()

    # def test_Setting_Basic_fast(self):
    #     """验证切换工作模式（快速）并触发拍摄"""
    #     fast_button_x = 2188
    #     fast_button_y = 363
    #     pg.click(fast_button_x, fast_button_y)
    #     self.camera_setting_page.trigger_camera()
    #     standby_text = self.camera_setting_page.wait_for_standby()
    #     try:
    #         self.assertEqual(standby_text.strip(),  'StandBy', "验证切换工作模式（快速）并触发拍摄功能测试失败")
    #     except AssertionError:
    #         self.camera_setting_page.take_screenshot("TestFastModeFail")
    #         raise  # 重新抛出异常以确保测试失败

    # def test_Setting_Basic_fast(self):
    #     """验证切换工作模式（快速）并触发拍摄"""
    #     # fast_button_x = 2188
    #     # fast_button_y = 363
    #     # pg.click(fast_button_x, fast_button_y)
    #     self.camera_setting_page.WorkingMode_Fast()
    #     time.sleep(1)
    #     self.camera_setting_page.trigger_camera()
    #     standby_text = self.camera_setting_page.wait_for_standby()
    #     if standby_text is None or standby_text.strip() != 'StandBy':
    #         # 发生异常时截图并抛出自定义异常信息
    #         self.camera_setting_page.take_screenshot("TestFastModeFail")
    #         self.fail("验证切换工作模式（快速）并触发拍摄功能测试失败: standby_text 为 None 或不等于 'StandBy'")
    #
    # def test_Setting_Basic_Standard(self):
    #     """验证切换工作模式（标准）并触发拍摄"""
    #     self.camera_setting_page.WorkingMode_Standard()
    #     time.sleep(1)
    #     self.camera_setting_page.trigger_camera()
    #     standby_text = self.camera_setting_page.wait_for_standby()
    #     if standby_text is None or standby_text.strip() != 'StandBy':
    #         # 发生异常时截图并抛出自定义异常信息
    #         self.camera_setting_page.take_screenshot("TestFastModeFail")
    #         self.fail("验证切换工作模式（快速）并触发拍摄功能测试失败: standby_text 为 None 或不等于 'StandBy'")

    # def _test_working_mode(self, mode_method, mode_name):
    #     print(f"开始测试 {mode_name} 模式...")
    #     mode_method()  # 切换到指定模式
    #     # time.sleep(1)
    #     self.camera_setting_page.trigger_camera()
    #     standby_text = self.camera_setting_page.wait_for_standby()
    #     if standby_text is None or standby_text.strip() != 'StandBy':
    #         self.camera_setting_page.take_screenshot(f"Test{mode_name}ModeFail")
    #         self.fail(f"验证切换工作模式（{mode_name}）并触发拍摄功能测试失败: standby_text 为 None 或不等于 'StandBy'")
    #     print("pass")
    #
    # def test_Setting_Basic_fast(self):
    #     """验证切换工作模式（快速）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_Fast, "Fast")
    #
    # def test_Setting_Basic_Standard(self):
    #     """验证切换工作模式（标准）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_Standard, "Standard")
    #
    # def test_Setting_Basic_Precise(self):
    #     """验证切换工作模式（精准）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_Precise, "Precise")
    #
    # def test_Setting_Basic_SuperPrecise(self):
    #     """验证切换工作模式（超准）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_SuperPrecise, "SuperPrecise")
    #
    # def test_Setting_Basic_White(self):
    #     """验证切换工作模式（白照明）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_White, "White")
    #
    # def test_Setting_Basic_Black(self):
    #     """验证切换工作模式（无照明）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_Black, "Black")
    #
    # def test_Setting_Basic_Grid(self):
    #     """验证切换工作模式（网格）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_Grid, "Grid")
    #
    # def test_Setting_Basic_ExposurePrediction(self):
    #     """验证切换工作模式（曝光强度预测）并触发拍摄"""
    #     self._test_working_mode(self.camera_setting_page.WorkingMode_ExposurePrediction, "ExposurePrediction")



import unittest
import pyautogui as pg
from pages.camera_setting_page import CameraSettingPage
import time
import random
class TestCameraSettingFalse(unittest.TestCase):  ####无效的
# class TestCameraSetting(unittest.TestCase):
    camera_setting_page = None

    @classmethod
    def setUpClass(cls):
        cls.camera_setting_page = CameraSettingPage()
        cls.check_and_click_device_status()

    @classmethod
    def check_and_click_device_status(cls):
        """检查当前设备状态并切换进入待机状态"""
        time.sleep(1)
        device_status_button_x = 333#116
        device_status_button_y = 1349
        device_status_button_color = pg.pixel(device_status_button_x, device_status_button_y)
        device_status_button_color_hold = (77, 133, 72)
        device_status_button_color_run = (176, 28, 58)
        if device_status_button_color == device_status_button_color_run:
            pg.click(device_status_button_x, device_status_button_y)  # 点击运行
        elif device_status_button_color == device_status_button_color_hold:
            pass
        else:
            # 如果出现意外颜色，则截图
            cls.camera_setting_page.take_screenshot("UnexpectedColor")
            print(f"Error: Unexpected color detected {device_status_button_color} . Please check 【Click to Hold】/【Click to Run】 button.")
            cls.fail()

    def verify_setting_change_by_click(self, setting_method, setting_name):
        print(f"Starting test for {setting_name} ...")
        setting_method()  # Switch to the specified setting
        self.camera_setting_page.trigger_camera()
        standby_text = self.camera_setting_page.wait_for_standby()
        if standby_text is None or standby_text.strip() != 'StandBy':
            self.camera_setting_page.take_screenshot(f"Test{setting_name}ModeFail")
            self.fail(f"Test to switch（{setting_name}）and trigger capture failed: standby_text is None or not equal to 'StandBy'")
        print("pass")

    def verify_setting_change_by_input(self, setting_method, input_value, setting_name):
        print(f"Starting test for {setting_name} ...")
        setting_method(input_value)  # Swit ch to the specified setting
        # time.sleep(1)
        self.camera_setting_page.trigger_camera()
        standby_text = self.camera_setting_page.wait_for_standby()
        if standby_text is None or standby_text.strip() != 'StandBy':
            self.camera_setting_page.take_screenshot(f"Test{setting_name}ModeFail")
            self.fail(f"Test to switch（{setting_name}）with input value '{input_value}' failed: standby_text is None or not equal to 'StandBy'")
        print("pass")

    def test_Setting_Basic_Fast(self):
        """验证切换工作模式（快速）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "Fast")

    def test_Setting_Basic_Standard(self):
        """验证切换工作模式（标准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_standard, "Standard")

    def test_Setting_Basic_Precise(self):
        """验证切换工作模式（精准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_precise, "Precise")

    def test_Setting_Basic_SuperPrecise(self):
        """验证切换工作模式（超准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_super_precise, "SuperPrecise")

    def test_Setting_Basic_White(self):
        """验证切换工作模式（白照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_white, "White")

    def test_Setting_Basic_Black(self):
        """验证切换工作模式（无照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_black, "Black")

    def test_Setting_Basic_Grid(self):
        """验证切换工作模式（网格）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_grid, "Grid")

    def test_Setting_Basic_ExposurePrediction(self):
        """验证切换工作模式（曝光强度预测）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_prediction, "ExposurePrediction")

    def test_Setting_Binning_Enable(self):
        """验证切换启用Binning模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_binning_enable, "EnableBinning")

    def test_Setting_Binning_Fast(self):
        """验证切换工作模式（Binning_快速）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "BinningFast")

    def test_Setting_Binning_Standard(self):
        """验证切换工作模式（Binning_标准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_standard, "BinningStandard")

    def test_Setting_Binning_Precise(self):
        """验证切换工作模式（Binning_精准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_precise, "BinningPrecise")

    def test_Setting_Binning_SuperPrecise(self):
        """验证切换工作模式（Binning_超准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_super_precise, "BinningSuperPrecise")

    def test_Setting_Binning_White(self):
        """验证切换工作模式（Binning_白照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_white, "BinningWhite")

    def test_Setting_Binning_Black(self):
        """验证切换工作模式（Binning_无照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_black, "BinningBlack")

    def test_Setting_Binning_Grid(self):
        """验证切换工作模式（Binning_网格）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_grid, "BinningGrid")

    def test_Setting_Binning_ExposurePrediction(self):
        """验证切换工作模式（Binning_曝光强度预测）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_prediction, "BinningExposurePrediction")

    def test_Setting_Binning_Disable(self):
        """验证切换关闭Binning模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_binning_disable, "DisableBinning")

    def test_Setting_Roi_XStar_100(self):
        """验证修改ROI_X起始值为100并触发拍摄"""
        #方式一：直接使用pg坐标点击修改
        # pg.click(142, 427, 2)
        # pg.press("backspace")
        # pg.write("30")
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_x_star, "100",  "RoiXStar_100")

    def test_Setting_Roi_XStar_255(self):
        """验证修改ROI_X起始值为255并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_x_star, "255", "RoiXStar_255")

    def test_Setting_Roi_XStar_0(self):
        """验证修改ROI_X起始值为0并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_x_star, "0", "RoiStar_0")
        
    def test_Setting_Roi_YStar_100(self):
        """验证修改ROI_Y起始值为100并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_y_star, "100", "RoiYStar_100")

    def test_Setting_Roi_YStar_255(self):
        """验证修改ROI_Y起始值为255并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_y_star, "255", "RoiYStar_255")

    def test_Setting_Roi_YStar_0(self):
        """验证修改ROI_Y起始值为0并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_y_star, "0", "RoiYStar_0")
        
    def test_Setting_Roi_Width_0(self):
        """验证修改ROI_Width值为0并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_width, "0", "RoiWidth_0")
        
    def test_Setting_Roi_Width_100(self):
        """验证修改ROI_Width值为100并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_width, "100", "RoiWidth_100")

    def test_Setting_Roi_Width_255(self):
        """验证修改ROI_Width值为255并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_width, "255", "RoiWidth_255")

    def test_Setting_ROI_Height_0(self):
        """验证修改ROI_Height值为0并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_height, "0", "RoiHeight_0")

    def test_Setting_ROI_Height_100(self):
        """验证修改ROI_Height值为100并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_height, "100", "RoiHeight_100")

    def test_Setting_ROI_Height_random(self):
        """验证修改ROI_Height值为0-255之间的随机整数并触发拍摄"""
        random_value = str(random.randint(0, 255))  # 生成0-255之间的随机整数并转换为字符串
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_height, random_value, "RoiHeight_random")

    def test_Setting_ROI_Height_255(self):
        """验证修改ROI_Height值为255并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_height, "255", "RoiHeight_255")

    @classmethod
    def tearDownClass(cls):
        if cls.camera_setting_page is not None:
            cls.camera_setting_page.quit()

if __name__ == '__main__':
    unittest.main()

