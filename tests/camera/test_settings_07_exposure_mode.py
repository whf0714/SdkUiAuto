
from tests.camera.test_camera_public import TestCameraPublic

class TestCameraExposureMode(TestCameraPublic):

    def test_exposure_mode_01_manual_repeat(self):
        """验证切换手动多次平均模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_mode_manual_repeat, "ManualRepeat")

    def test_exposure_mode_02_auto_nhdr(self):
        """验证切换指定次数自动曝光模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_mode_auto_nhdr, "AUTO_NHDR")

    def test_exposure_mode_03_auto_phdr(self):
        """验证切换指定质量自动曝光模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_mode_auto_phdr, "AUTO_PHDR")

    def test_exposure_mode_04_manual(self):
        """验证切换手动模式并拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_mode_manual, "Manual")