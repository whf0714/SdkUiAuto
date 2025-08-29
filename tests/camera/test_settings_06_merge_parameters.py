from tests.camera.test_camera_public import TestCameraPublic
import random

class TestCameraMergeParameters(TestCameraPublic):

    def test_merge_parameters_01_th_random(self):
        """验证修改合并参数阈值为0-7之间的随机整数并触发拍摄"""
        th_random_value = str(random.randint(0, 7))
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_th, th_random_value, "MergeParameters_th_Random")

    def test_merge_parameters_02_th_max(self):
        """验证修改合并参数阈值为最大值（7）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_th, "7", "MergeParameters_th_max")

    def test_merge_parameters_03_th_min(self):
        """验证修改合并参数阈值为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_th, "0", "MergeParameters_th_min")

    def test_merge_parameters_04_th_default(self):
        """验证修改合并参数阈值为默认设置值（5）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_th, "5", "MergeParameters_th_default")
        
    def test_merge_parameters_05_num_random(self):
        """验证修改合并参数数量为1-4之间的随机整数并触发拍摄"""
        num_random_value = str(random.randint(1, 4))
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_num, num_random_value, "MergeParameters_num_Random")

    def test_merge_parameters_06_num_max(self):
        """验证修改合并参数数量为最大值（4）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_num, "4", "MergeParameters_num_max")

    def test_merge_parameters_07_num_min(self):
        """验证修改合并参数数量为最小值（1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_num, "1", "MergeParameters_num_min")

    def test_merge_parameters_08_num_default(self):
        """验证修改合并参数数量为默认设置值（2）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_merge_parameters_num, "2", "MergeParameters_th_default")



