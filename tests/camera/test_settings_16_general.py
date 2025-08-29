from tests.camera.test_camera_public import TestCameraPublic
import random

class TestCameraGeneral(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        # self.camera_setting_page.collapse_basic() # 折叠【基本】
        # self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        # self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        # self.camera_setting_page.collapse_external_exposure()  # 折叠【外部曝光】
        # self.camera_setting_page.collapse_reconstruction()  # 折叠【重构】
        self.camera_setting_page.collapse_post_process()  # 折叠【后处理】

    def test_general_00_auto_sleep_enable(self):
        """验证启用自动休眠并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_auto_sleep_enable, "auto_sleep_enable")

    def test_general_01_auto_sleep_max(self):
        """验证自动休眠设置为最大值（65535）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,"65535", "auto_sleep_max")

    def test_general_02_auto_sleep_min(self):
        """验证自动休眠通过参数设置为最小值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,"100", "auto_sleep_min")

    def test_general_03_auto_sleep_random(self):
        """验证自动休眠设置为（100-65535）之间保留两位小数的随机小数并触发拍摄"""
        auto_sleep_value = str(random.randint(100, 65535))
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,auto_sleep_value, "auto_sleep_random")

    def test_general_04_auto_sleep_default(self):
        """验证自动休眠设置为默认值（5000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,"5000", "auto_sleep_default")

    def test_general_05_auto_sleep_disable(self):
        """验证关闭自动休眠并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_auto_sleep_disable, "auto_sleep_disable")

    def test_general_06_correct_distortion_enable(self):
        """验证启用矫正畸变并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_correct_distortion_enable, "correct_distortion_enable")

    def test_general_07_correct_distortion_disable(self):
        """验证关闭矫正畸变并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_correct_distortion_disable, "correct_distortion_disable")