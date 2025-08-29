from tests.camera.test_camera_public import TestCameraPublic
import random


class TestCameraMultiHeadExposureVariance(TestCameraPublic):

    # def setUp(self):
    #     super().setUp()  # 保留父类初始化
    #     # 所有测试用例的公共前置操作
    #     self.camera_setting_page.collapse_basic() # 折叠【基本】
    #     self.camera_setting_page.collapse_multi_head()# 折叠【多头】

    def test_multi_head_exposure_variance_01_priority_01(self):
        """验证修改多头曝光差异模式为01并触发拍摄"""
        self.camera_setting_page.collapse_basic()  # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()  # 折叠【多头】
        self.verify_setting_change_by_click(self.camera_setting_page.set_multi_head_exposure_variance_01, "MultiHeadExpoVar_Mode_01")

    def test_multi_head_exposure_variance_02_priority_23(self):
        """验证修改多头曝光差异模式为23并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_multi_head_exposure_variance_23, "MultiHeadExpoVar_Mode_23")

    def test_multi_head_exposure_variance_03_priority_02(self):
        """验证修改多头曝光差异模式为02并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_multi_head_exposure_variance_02, "MultiHeadExpoVar_Mode_02")

    def test_multi_head_exposure_variance_04_priority_13(self):
        """验证修改多头曝光差异模式为13并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_multi_head_exposure_variance_13, "MultiHeadExpoVar_Mode_13")

    def test_multi_head_exposure_variance_05_ratio_random(self):
        """验证修改多头曝光差异中差异比为0-15之间的随机正整数并触发拍摄"""
        priority_value = str(random.randint(0, 15))
        self.verify_setting_change_by_input(self.camera_setting_page.set_multi_head_exposure_variance_ratio, priority_value,"MultiHeadExpoVar_Ratio_Random")

    def test_multi_head_exposure_variance_06_ratio_max(self):
        """验证修改多头曝光中差异比为最大值（15）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_multi_head_exposure_variance_ratio, "15","MultiHeadExpoVar_Ratio_max")

    def test_multi_head_exposure_variance_07_ratio_min(self):
        """验证修改多头曝光中差异比为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_multi_head_exposure_variance_ratio, "0","MultiHeadExpoVar_Ratio_min")

    def test_multi_head_exposure_variance_08_priority_enable(self):
        """验证关闭多头曝光差异模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_multi_head_exposure_variance_enable, "MultiHeadExpoVar_Mode_Enable")