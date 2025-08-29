import unittest
# from .test_camera_public import TestCameraPublic
from tests.camera.test_camera_public import TestCameraPublic
import random

class TestCameraRoi(TestCameraPublic):

    def test_roi_01_x_star_random(self):
        """验证修改ROI_X起始值为0-255之间的随机整数并触发拍摄"""
        x_random_value = str(random.randint(0, 255))
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_x_star, x_random_value, "RoiXStar_Random")

    def test_roi_02_x_star_max(self):
        """验证修改ROI_X起始值为最大值（255）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_x_star, "255", "RoiXStar_max")

    def test_roi_03_x_star_min(self):
        """验证修改ROI_X起始值为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_x_star, "0", "RoiXStar_min")

    def test_roi_04_y_star_random(self):
        """验证修改ROI_X起始值为0-255之间的随机整数并触发拍摄"""
        y_random_value = str(random.randint(0, 255))
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_y_star, y_random_value, "RoiYStar_Random")

    def test_roi_05_y_star_max(self):
        """验证修改ROI_Y起始值为最大值（255）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_y_star, "255", "RoiYStar_max")

    def test_roi_06_y_star_min(self):
        """验证修改ROI_Y起始值为最小值（0)并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_y_star, "0", "RoiYStar_min")

    def test_roi_07_width_min(self):
        """验证修改ROI_width值为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_width, "0", "RoiWidth_min")

    def test_roi_08_width_random(self):
        """验证修改ROI_width值为0-255之间的随机整数并触发拍摄"""
        width_random_value = str(random.randint(0, 255))
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_width, width_random_value, "RoiWidth_Random")

    def test_roi_09_width_max(self):
        """验证修改ROI_width值为最大值（255）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_width, "255", "RoiWidth_max")

    def test_roi_10_height_min(self):
        """验证修改ROI_height值为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_height, "0", "RoiHeight_min")

    def test_roi_11_height_random(self):
        """验证修改ROI_height值为0-255之间的随机整数并触发拍摄"""
        height_random_value = str(random.randint(0, 255))  # 生成0-255之间的随机整数并转换为字符串
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_height, height_random_value, "RoiHeight_Random")

    def test_roi_12_height_max(self):
        """验证修改ROI_height值为最大值（255）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_roi_height, "255", "RoiHeight_max")