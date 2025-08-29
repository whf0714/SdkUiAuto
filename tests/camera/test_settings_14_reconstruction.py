import unittest
from tests.camera.test_camera_public import TestCameraPublic
import random

class TestCameraOverExposureFilter(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        self.camera_setting_page.expand_reconstruction()# 展开【重构】


    def test_over_exposure_filter_01_manual(self):
        """验证设置过曝滤除为手动模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_over_exposure_filter_manual, "OverExposureFilter_Manual")

    def test_over_exposure_filter_02_th_max(self):
        """验证设置过曝滤除阈值为最大值（16）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_over_exposure_filter_th, "16","OverExposureFilter_th_max")

    def test_over_exposure_filter_03_th_random(self):
        """验证设置过曝滤除阈值为为0-16之间的随机整数并触发拍摄"""
        th_random_value = str(random.randint(0, 16))
        self.verify_setting_change_by_input(self.camera_setting_page.set_over_exposure_filter_th, th_random_value,"OverExposureFilter_th_random")

    def test_over_exposure_filter_04_th_min(self):
        """验证设置过曝滤除阈值为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_over_exposure_filter_th, "0","OverExposureFilter_th_min")

    def test_over_exposure_filter_05_auto(self):
        """验证设置过曝滤除为手动模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_over_exposure_filter_auto, "OverExposureFilter_auto")

class TestCameraValidPointJudgement(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        self.camera_setting_page.expand_reconstruction()# 展开【重构】


    def test_valid_point_judgement_0_th0_max(self):
        """验证设置有效点判断阈值0为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th0, "100","ValidPointJudgement_th0_max")

    def test_valid_point_judgement_1_th0_min(self):
        """验证设置有效点判断阈值0为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th0, "0","ValidPointJudgement_th0_min")

    def test_valid_point_judgement_2_th0_random(self):
        """验证设置有效点判断阈值0为为0-100之间的随机整数并触发拍摄"""
        th_random_value = str(random.randint(0, 100))
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th0, th_random_value,"ValidPointJudgement_th0_random")

    def test_valid_point_judgement_3_th1_max(self):
        """验证设置有效点判断阈值1为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th1, "100","ValidPointJudgement_th1_max")

    def test_valid_point_judgement_4_th1_min(self):
        """验证设置有效点判断阈值1为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th1, "0","ValidPointJudgement_th1_min")

    def test_valid_point_judgement_5_th1_random(self):
        """验证设置有效点判断阈值1为为0-100之间的随机整数并触发拍摄"""
        th_random_value = str(random.randint(0, 100))
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th1, th_random_value,"ValidPointJudgement_th1_Random")

    def test_valid_point_judgement_6_weak(self):
        """验证设置有效点判断为weak设置（1,1）并触发拍摄"""
        self.camera_setting_page.set_valid_point_judgement_th0("1")
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th1, "1","ValidPointJudgement_Weak")

    def test_valid_point_judgement_7_normal(self):
        """验证设置有效点判断为normal设置（3,3）并触发拍摄"""
        self.camera_setting_page.set_valid_point_judgement_th0("3")
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th1, "3","ValidPointJudgement_Normal")

    def test_valid_point_judgement_8_strong(self):
        """验证设置有效点判断为strong设置（6,6）并触发拍摄"""
        self.camera_setting_page.set_valid_point_judgement_th0("6")
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th1, "6","ValidPointJudgement_Strong")

    def test_valid_point_judgement_9_default(self):
        """验证设置有效点判断为默认设置（3,3）并触发拍摄"""
        self.camera_setting_page.set_valid_point_judgement_th0("3")
        self.verify_setting_change_by_input(self.camera_setting_page.set_valid_point_judgement_th1, "3","ValidPointJudgement_Default")


class TestCameraBurrRemovalFilter(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        self.camera_setting_page.expand_reconstruction()# 展开【重构】

    def test_burr_removal_filter_0_th0_max(self):
        """验证设置飞点剔除阈值0为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th0, "100","BurrRemovalFilter_th0_max")

    def test_burr_removal_filter_1_th0_min(self):
        """验证设置飞点剔除阈值0为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th0, "0","BurrRemovalFilter_th0_min")

    def test_burr_removal_filter_2_th0_random(self):
        """验证设置飞点剔除阈值0为为0-100之间的随机整数并触发拍摄"""
        th0_random_value = str(random.randint(0, 100))
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th0, th0_random_value,"BurrRemovalFilter_th0_random")

    def test_burr_removal_filter_3_th1_max(self):
        """验证设置飞点剔除阈值1为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th1, "100","BurrRemovalFilter_th1_max")

    def test_burr_removal_filter_4_th1_min(self):
        """验证设置飞点剔除阈值1为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th1, "0","BurrRemovalFilter_th1_min")

    def test_burr_removal_filter_5_th1_random(self):
        """验证设置飞点剔除阈值1为为0-100之间的随机整数并触发拍摄"""
        th1_random_value = str(random.randint(0, 100))
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th1, th1_random_value,"BurrRemovalFilter_th1_random")

    def test_burr_removal_filter_6_weak(self):
        """验证设置飞点剔除为weak设置（6,6）并触发拍摄"""
        self.camera_setting_page.set_burr_removal_filter_th0("6")
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th1, "6","BurrRemovalFilter_Weak")

    def test_burr_removal_filter_7_normal(self):
        """验证设置飞点剔除为normal设置（13,13）并触发拍摄"""
        self.camera_setting_page.set_burr_removal_filter_th0("13")
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th1, "13","BurrRemovalFilter_Normal")

    def test_burr_removal_filter_8_strong(self):
        """验证设置飞点剔除为strong设置（26,26）并触发拍摄"""
        self.camera_setting_page.set_burr_removal_filter_th0("26")
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th1, "26","BurrRemovalFilter_Strong")

    def test_burr_removal_filter_9_default(self):
        """验证设置飞点剔除为默认设置（13,13）并触发拍摄"""
        self.camera_setting_page.set_burr_removal_filter_th0("13")
        self.verify_setting_change_by_input(self.camera_setting_page.set_burr_removal_filter_th1, "13","BurrRemovalFilter_Default")


class TestCameraPreProcess(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        self.camera_setting_page.expand_reconstruction()# 展开【重构】


    def test_pre_process_0_num_max(self):
        """验证设置预处理次数为最大值（5）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_num, "5","PreProcess_Num_max")

    def test_pre_process_1_num_min(self):
        """验证设置预处理次数为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_num, "0","PreProcess_Num_min")

    def test_pre_process_2_num_random(self):
        """验证设置预处理次数为为0-5之间的随机整数并触发拍摄"""
        num_random_value = str(random.randint(0, 5))
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_num, num_random_value,"PreProcess_Num_random")

    def test_pre_process_3_th_max(self):
        """验证设置预处理阈值为最大值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_th, "100","PreProcess_Th_max")

    def test_pre_process_4_th_min(self):
        """验证设置预处理阈值为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_th, "0","PreProcess_Th_min")

    def test_pre_process_5_th_random(self):
        """验证设置预处理阈值为为0-5之间的随机整数并触发拍摄"""
        th_random_value = str(random.randint(0, 5))
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_th, th_random_value,"PreProcess_Th_random")

    def test_pre_process_6_weak(self):
        """验证设置预处理为weak设置（1,10）并触发拍摄"""
        self.camera_setting_page.set_pre_process_num("1")
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_th, "10","PreProcess_Weak")

    def test_pre_process_7_normal(self):
        """验证设置预处理为normal设置（2,20）并触发拍摄"""
        self.camera_setting_page.set_pre_process_num("2")
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_th, "20","PreProcess_Normal")

    def test_pre_process_8_strong(self):
        """验证设置预处理为strong设置（4,40）并触发拍摄"""
        self.camera_setting_page.set_pre_process_num("4")
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_th, "40","PreProcess_Strong")

    def test_pre_process_9_default(self):
        """验证设置预处理为默认设置（5,20）并触发拍摄"""
        self.camera_setting_page.set_pre_process_num("5")
        self.verify_setting_change_by_input(self.camera_setting_page.set_pre_process_th, "20","PreProcess_Default")
