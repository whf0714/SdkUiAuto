import unittest
# from .test_camera_public import TestCameraPublic
from tests.camera.test_camera_public import TestCameraPublic

class TestCameraWorkingMode(TestCameraPublic):

    def test_working_mode_01_fast(self):
        """验证切换工作模式（快速）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "Fast")

    def test_working_mode_02_standard(self):
        """验证切换工作模式（标准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_standard, "Standard")

    def test_working_mode_03_precise(self):
        """验证切换工作模式（精准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_precise, "Precise")

    def test_working_mode_04_superPrecise(self):
        """验证切换工作模式（超准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_super_precise, "SuperPrecise")

    def test_working_mode_05_white(self):
        """验证切换工作模式（白照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_white, "White")

    def test_working_mode_06_black(self):
        """验证切换工作模式（无照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_black, "Black")

    def test_working_mode_07_grid(self):
        """验证切换工作模式（网格）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_grid, "Grid")

    def test_working_mode_08_exposurePrediction(self):
        """验证切换工作模式（曝光强度预测）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_prediction, "ExposurePrediction")

    def test_working_mode_09_fast(self):
        """验证工作模式为默认设置（快速）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "Fast")

