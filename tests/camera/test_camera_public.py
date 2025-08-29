import unittest
import pyautogui as pg
from pages.camera_setting_page import CameraSettingPage
from pages.menu_page import MenuPage
import time
import os

# class TestCameraPublic(unittest.TestCase):
    # camera_setting_page = None

    # @classmethod
    # def setUpClass(cls):
    #     cls.camera_setting_page = CameraSettingPage()
    #     cls.check_and_click_device_status()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     if cls.camera_setting_page is not None:
    #         cls.camera_setting_page.quit()

    # =========================================================================================================

    # @classmethod
    # def setUpClass(cls):
    #     # 使用单例实例
    #     cls.camera_setting_page = CameraSettingPage()
    #     # 仅在首次初始化时执行设备状态检查
    #     if not hasattr(cls.camera_setting_page, '_is_initialized'):
    #         cls.check_and_click_device_status()
    #         cls.camera_setting_page._is_initialized = True  # 标记已初始化
    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # 如果未在全局套件中运行，则退出实例
    #     # if not os.getenv('GLOBAL_SUITE_RUNNING'):
    #     #     cls.camera_setting_page.quit()
    #     if not os.getenv('GLOBAL_SUITE_RUNNING'):
    #         if cls.camera_setting_page is not None:
    #             cls.camera_setting_page.quit()
    #             cls.camera_setting_page = None

# @classmethod
# def check_and_click_device_status(cls):
#     """检查当前设备状态并切换进入待机状态"""
# time.sleep(1)
# # if cls.camera_setting_page is None:
# #     raise ValueError("camera_setting_page is not initialized. Please check setUpClass.")
# device_status_button_x = 333#116
# device_status_button_y = 1349
# device_status_button_color = pg.pixel(device_status_button_x, device_status_button_y)
# device_status_button_color_hold = (77, 133, 72)
# device_status_button_color_run = (176, 28, 58)
# if device_status_button_color == device_status_button_color_run:
#     pg.click(device_status_button_x, device_status_button_y)  # 点击运行
# elif device_status_button_color == device_status_button_color_hold:
#     pass
# else:
#     # 如果出现意外颜色，则截图
#     cls.camera_setting_page.take_screenshot("UnexpectedColor")
#     # self.camera_setting_page.take_screenshot("UnexpectedColor")
#     print(
#         f"保存图片Error: Unexpected color detected {device_status_button_color} . Please check 【Click to Hold】/【Click to Run】 button.")
#     cls.fail()

    # =============================================================================================================

# =============================================================================================================
# class TestCameraPublic(unittest.TestCase):
#
#     camera_setting_page = CameraSettingPage()  # 直接使用单例
#
#
#     @classmethod
#     def setUpClass(cls):
#         # 无需额外初始化逻辑，单例已在类属性中创建
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         # 仅在非全局套件运行时关闭实例
#         if not os.getenv('GLOBAL_SUITE_RUNNING'):
#             cls.camera_setting_page.quit()
#
#     def verify_setting_change_by_click(self, setting_method, setting_name, check_standby= True):
#         print(f"Starting test for {setting_name} ...")
#         setting_method()  # Switch to the specified setting
#         # 判断当check_standby为false时不检查standby状态(针对自动连续触发功能）
#         if check_standby:
#             self.camera_setting_page.trigger_camera()
#             standby_text = self.camera_setting_page.wait_for_standby()
#             if standby_text is None or standby_text.strip() != 'StandBy':
#                 self.camera_setting_page.take_screenshot(f"Test{setting_name}ModeFail")
#                 self.fail(
#                     f"Test to switch（{setting_name}）and trigger capture failed: standby_text is None or not equal to 'StandBy'")
#         else:
#             time.sleep(0.1)
#
#         print("pass")
#
#     def verify_setting_change_by_input(self, setting_method, input_value, setting_name, check_standby=True):
#         print(f"Starting test for {setting_name} ...")
#         setting_method(input_value)  # Swit ch to the specified setting
#         # time.sleep(1)
#         self.camera_setting_page.trigger_camera()
#         # 判断当check_standby为false时不检查standby状态
#         if check_standby:
#             standby_text = self.camera_setting_page.wait_for_standby()
#             if standby_text is None or standby_text.strip() != 'StandBy':
#                 self.camera_setting_page.take_screenshot(f"Test{setting_name}ModeFail")
#                 self.fail(
#                     f"Test to switch（{setting_name}）with input value '{input_value}' failed: standby_text is None or not equal to 'StandBy'")
#
#         print("pass")

    # =============================================================================================================



class TestCameraPublic(unittest.TestCase):

    camera_setting_page = CameraSettingPage()  # 直接使用单例
    # menu_page = MenuPage()

    @classmethod
    def setUpClass(cls):
        # 无需额外初始化逻辑，单例已在类属性中创建
        pass

    @classmethod
    def tearDownClass(cls):
        # 仅在非全局套件运行时关闭实例
        if not os.getenv('GLOBAL_SUITE_RUNNING'):
            cls.camera_setting_page.quit()
            # cls.menu_page.quit()

    def verify_setting_change_by_click(self, setting_method, setting_name, check_standby= True):
        print(f"Starting test for {setting_name} ...")
        setting_method()  # Switch to the specified setting
        # 判断当check_standby为false时不检查standby状态(针对自动连续触发功能）
        if check_standby:
            self.camera_setting_page.trigger_camera()
            standby_text = self.camera_setting_page.wait_for_standby()
            if standby_text is None or standby_text.strip() != 'StandBy':
                self.camera_setting_page.take_screenshot(f"Test{setting_name}ModeFail")
                self.fail(
                    f"Test to switch（{setting_name}）and trigger capture failed: standby_text is None or not equal to 'StandBy'")
        else:
            time.sleep(0.1)

        print("pass")

    def verify_setting_change_by_input(self, setting_method, input_value, setting_name, check_standby=True):
        print(f"Starting test for {setting_name} ...")
        setting_method(input_value)  # Swit ch to the specified setting
        # time.sleep(1)
        self.camera_setting_page.trigger_camera()
        # 判断当check_standby为false时不检查standby状态
        if check_standby:
            standby_text = self.camera_setting_page.wait_for_standby()
            if standby_text is None or standby_text.strip() != 'StandBy':
                self.camera_setting_page.take_screenshot(f"Test{setting_name}ModeFail")
                self.fail(
                    f"Test to switch（{setting_name}）with input value '{input_value}' failed: standby_text is None or not equal to 'StandBy'")

        print("pass")

# if __name__ == '__main__':
#     unittest.main()
