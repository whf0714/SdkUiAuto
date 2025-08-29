import unittest
# from .test_camera_public import TestCameraPublic
from tests.camera.test_camera_public import TestCameraPublic

class TestCameraBinning(TestCameraPublic):
    
    def test_binning_01_enable(self):
        """验证启用Binning模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_binning_enable, "EnableBinning")

    def test_binning_02_standard(self):
        """验证切换工作模式（Binning_标准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_standard, "BinningStandard")

    def test_binning_03_precise(self):
        """验证切换工作模式（Binning_精准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_precise, "BinningPrecise")

    def test_binning_04_superPrecise(self):
        """验证切换工作模式（Binning_超准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_super_precise, "BinningSuperPrecise")

    def test_binning_05_white(self):
        """验证切换工作模式（Binning_白照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_white, "BinningWhite")

    def test_binning_06_black(self):
        """验证切换工作模式（Binning_无照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_black, "BinningBlack")

    def test_binning_07_grid(self):
        """验证切换工作模式（Binning_网格）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_grid, "BinningGrid")

    def test_binning_08_exposurePrediction(self):
        """验证切换工作模式（Binning_曝光强度预测）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_prediction, "BinningExposurePrediction")

    def test_binning_09_fast(self):
        """验证切换工作模式（Binning_快速）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "BinningFast")

    def test_binning_10_disable(self):
        """验证关闭Binning模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_binning_disable, "DisableBinning")


    
