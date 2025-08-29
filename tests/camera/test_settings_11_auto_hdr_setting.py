from tests.camera.test_camera_public import TestCameraPublic
import random


class TestCameraAutoHDR(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】

    def test_auto_hdr_setting_01_priority_min(self):
        """验证修改自动曝光设置优先级为最小值（0）并触发拍摄"""
        # self.camera_setting_page.collapse_basic()  # 折叠【基本】
        # self.camera_setting_page.collapse_multi_head()  # 折叠【多头】
        self.camera_setting_page.set_exposure_mode_auto_nhdr()  # 切换指定次数自动曝光（NHDR)

        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_priority, "0", "Auto_Hdr_Priority_min")

    def test_auto_hdr_setting_02_priority_max(self):
        """验证修改自动曝光设置优先级为最大值（7）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_priority, "7", "Auto_Hdr_Priority_max")

    def test_auto_hdr_setting_03_priority_nhdr_3_random(self):
        """验证修改NHDR模式下，三次曝光，自动曝光设置优先级为0-7之间的随机正整数并触发拍摄"""
        self.camera_setting_page.set_exposure_num_triple() #切换三次曝光
        priority_value = str(random.randint(0, 7))
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_priority, priority_value,"Auto_Hdr_Priority_NHDR_3_Random")

    def test_auto_hdr_setting_04_priority_nhdr_2_random(self):
        """验证修改NHDR模式下，二次曝光，自动曝光设置优先级为0-7之间的随机正整数并触发拍摄"""
        self.camera_setting_page.set_exposure_num_double() #切换二次曝光
        priority_value = str(random.randint(0, 7))
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_priority, priority_value,"Auto_Hdr_Priority_NHDR_2_random")

    def test_auto_hdr_setting_05_priority_nhdr_1_random(self):
        """验证修改NHDR模式下，一次曝光，自动曝光设置优先级为0-7之间的随机正整数并触发拍摄"""
        self.camera_setting_page.set_exposure_num_single() #切换一次曝光
        priority_value = str(random.randint(0, 7))
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_priority, priority_value,"Auto_Hdr_Priority_NHDR_1_random")

    def test_auto_hdr_setting_06_priority_phdr_random(self):
        """验证修改PHDR模式下,自动曝光设置优先级为0-7之间的随机正整数并触发拍摄"""
        self.camera_setting_page.set_exposure_mode_auto_phdr()  # 切换指定质量自动曝光（PHDR)
        priority_value = str(random.randint(0, 7))
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_priority, priority_value,"Auto_Hdr_Priority_PHDR_Random")

    def test_auto_hdr_setting_07_priority_phdr_default(self):
        """验证修改PHDR模式下,自动曝光设置优先级为默认值（3）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_priority, "3","Auto_Hdr_Priority_PHDR_default")

    def test_auto_hdr_setting_08_quality_min(self):
        """验证修改自动曝光设置质量阈值为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_quality, "0", "Auto_Hdr_Quality_min")

    def test_auto_hdr_setting_09_quality_max(self):
        """验证修改自动曝光设置质量阈值为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_quality, "100", "Auto_Hdr_Quality_max")

    def test_auto_hdr_setting_10_quality_random(self):
        """验证修改自动曝光设置质量阈值为0-100之间的随机正整数并触发拍摄并触发拍摄"""
        quality_value = str(random.randint(0, 7))
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_quality, quality_value, "Auto_Hdr_Quality_random")

    def test_auto_hdr_setting_11_quality_default(self):
        """验证修改自动曝光设置质量阈值为默认值（90）并触发拍摄并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_hdr_quality, "90","Auto_Hdr_Quality_default")
        self.camera_setting_page.set_exposure_mode_manual() #恢复曝光设置为手动模式