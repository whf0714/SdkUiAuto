
from tests.camera.test_camera_public import TestCameraPublic
import random

class TestCameraGain(TestCameraPublic):

    # def setUp(self):
    #     super().setUp()  # 保留父类初始化
    #     # 所有测试用例的公共前置操作
    #     self.camera_setting_page.collapse_basic() # 折叠【基本】
    #     self.camera_setting_page.collapse_multi_head()# 折叠【多头】

    def test_gain_01_random(self):
        """验证修改增益起始值为为0-5之间的随机整数并触发拍摄"""
        self.camera_setting_page.collapse_basic()
        self.camera_setting_page.collapse_multi_head()
        gain_01_value = str(random.randint(0, 5))
        self.verify_setting_change_by_input(self.camera_setting_page.set_gain, gain_01_value, "Gain_Random")

    def test_gain_02_max(self):
        """验证修改增益为最大值（5）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_gain, "5", "Gain_max")

    def test_gain_03_min(self):
        """验证修改增益为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_gain, "0", "Gain_min")


