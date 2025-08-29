
from tests.camera.test_camera_public import TestCameraPublic
import random

class TestCameraExposureIntensity(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】

    def test_intensity_3d_01_1st_random(self):
        """验证修改3D_1次曝光强度为0.1-100之间保留一位小数的随机小数并触发拍摄"""
        # self.camera_setting_page.collapse_basic()         #折叠【基本】
        # self.camera_setting_page.collapse_multi_head()    #折叠【多头】
        self.camera_setting_page.set_exposure_num_triple()# 切换3次曝光

        i_3d_1st_value = str(round(random.uniform(0.1, 100), 1))
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_1st, i_3d_1st_value, "3d_1st_random")

    def test_intensity_3d_02_1st_max(self):
        """验证修改3D_1次曝光强度为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_1st, "100", "3d_1st_max")

    def test_intensity_3d_03_1st_min(self):
        """验证修改3D_1次曝光强度为最小值（0.1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_1st, "0.1", "3d_1st_min")

    def test_intensity_3d_04_2nd_random(self):
        """验证修改3D_2次曝光强度为0.1-100之间保留一位小数的随机小数并触发拍摄"""
        i_3d_2nd_value = str(round(random.uniform(0.1, 100), 1))
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_2nd, i_3d_2nd_value, "3d_2nd_random")

    def test_intensity_3d_05_2nd_max(self):
        """验证修改3D_2次曝光强度为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_2nd, "100", "3d_2nd_max")

    def test_intensity_3d_06_2nd_min(self):
        """验证修改3D_2次曝光强度为最小值（0.1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_2nd, "0.1", "3d_2nd_min")

    def test_intensity_3d_07_3rd_random(self):
        """验证修改3D_3次曝光强度为0.1-100之间保留一位小数的随机小数并触发拍摄"""
        i_3d_3rd_value = str(round(random.uniform(0.1, 100), 1))
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_3rd, i_3d_3rd_value, "3d_3rd_random")

    def test_intensity_3d_08_3rd_max(self):
        """验证修改3D_3次曝光强度为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_3rd, "100", "3d_3rd_max")

    def test_intensity_3d_09_3rd_min(self):
        """验证修改3D_3次曝光强度为最小值（0.1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_3rd, "0.1", "3d_3rd_min")

    #恢复默认设置
    def test_intensity_3d_10_3rd_default(self):
        """验证修改3D_3次曝光强度为默认值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_3rd, "100", "3d_3rd_default")

    def test_intensity_3d_11_2nd_default(self):
        """验证修改3D_2次曝光强度为默认值（50）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_2nd, "50", "3d_2nd_default")

    def test_intensity_3d_12_1st_default(self):
        """验证修改3D_1次曝光强度为默认值（20）并触发拍摄"""
        self.camera_setting_page.set_exposure_num_single()      # 切换1次曝光
        self.verify_setting_change_by_input(self.camera_setting_page.set_3d_exposure_i_1st, "20", "3d_1st_default")

    """测试2D曝光强度"""
    def test_intensity_2d_13_random(self):
        """验证修改2D曝光强度为0.1-100之间保留一位小数的随机小数并触发拍摄"""
        # self.camera_setting_page.collapse_basic()  # 折叠【基本】
        # self.camera_setting_page.collapse_multi_head()    #折叠【多头】
        i_2d_value = str(round(random.uniform(0.1, 100), 1))
        self.verify_setting_change_by_input(self.camera_setting_page.set_2d_exposure_i, i_2d_value, "2d_exposure_i_random")

    def test_intensity_2d_14_max(self):
        """验证修改2D曝光强度为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_2d_exposure_i, "100", "2d_exposure_i_max")

    def test_intensity_2d_15_min(self):
        """验证修改2D曝光强度为最小值（0.1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_2d_exposure_i, "0.1", "2d_exposure_i_min")

    #恢复默认设置
    def test_intensity_2d_16_default(self):
        """验证修改2D曝光强度为默认值（20）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_2d_exposure_i, "20", "2d_exposure_i_default")
