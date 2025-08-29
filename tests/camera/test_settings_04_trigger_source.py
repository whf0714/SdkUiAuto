import unittest
# from .test_camera_public import TestCameraPublic
from tests.camera.test_camera_public import TestCameraPublic


class TestCameraTriggerSource(TestCameraPublic):

    def test_trigger_source_01_at(self):
        """验证切换自动连续触发模式并拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_auto_trigger, "AutoTrigger", False)

    def test_trigger_source_02_i0(self):
        """验证切换硬件触发I(0)模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_hard_trigger_0, "HardTriggerI0")

    def test_trigger_source_03_i1(self):
        """验证切换硬件触发I(1)模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_hard_trigger_1, "HardTriggerI1")

    def test_trigger_source_04_sw(self):
        """验证切换软件触发模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_soft_trigger, "SoftTrigger")