
from tests.camera.test_camera_public import TestCameraPublic
import random

"""当前定点数转换及范围检查设置均为M051040参数，需要先确认设备型号"""

class TestCamera01WorkingMode(TestCameraPublic):

    def test_working_mode_0_fast(self):
        """验证切换工作模式（快速）并触发拍摄"""
        self.camera_setting_page.set_soft_trigger() #确保设备触发模式为软件触发
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "Fast")

    def test_working_mode_1_standard(self):
        """验证切换工作模式（标准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_standard, "Standard")

    def test_working_mode_2_precise(self):
        """验证切换工作模式（精准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_precise, "Precise")

    def test_working_mode_3_superPrecise(self):
        """验证切换工作模式（超准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_super_precise, "SuperPrecise")

    def test_working_mode_5_white(self):
        """验证切换工作模式（白照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_white, "White")

    def test_working_mode_6_black(self):
        """验证切换工作模式（无照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_black, "Black")

    def test_working_mode_7_grid(self):
        """验证切换工作模式（网格）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_grid, "Grid")

    def test_working_mode_9_fast(self):
        """验证工作模式恢复为（快速）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "Fast")

class TestCamera02Binning(TestCameraPublic):

    def test_binning_0_enable(self):
        """验证切换启用Binning模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_binning_enable, "EnableBinning")

    def test_binning_1_standard(self):
        """验证切换工作模式（Binning_标准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_standard, "BinningStandard")

    def test_binning_2_precise(self):
        """验证切换工作模式（Binning_精准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_precise, "BinningPrecise")

    def test_binning_3_superPrecise(self):
        """验证切换工作模式（Binning_超准）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_super_precise, "BinningSuperPrecise")

    def test_binning_4_white(self):
        """验证切换工作模式（Binning_白照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_white, "BinningWhite")

    def test_binning_5_black(self):
        """验证切换工作模式（Binning_无照明）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_black, "BinningBlack")

    def test_binning_6_grid(self):
        """验证切换工作模式（Binning_网格）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_grid, "BinningGrid")

    def test_binning_8_fast(self):
        """验证切换工作模式（Binning_快速）并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fast, "BinningFast")

    def test_binning_9_disable(self):
        """验证切换关闭Binning模式并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_binning_disable, "DisableBinning")

class TestCamera03Roi(TestCameraPublic):

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

class TestCamera04Exposure(TestCameraPublic):

    def test_exposure_number_01_double(self):
        """验证切换2次曝光并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_num_double, "DoubleExposure")

    def test_exposure_number_02_single(self):
        """验证切换1次曝光并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_num_single, "SingleExposure")

    def test_gain_01_random(self):
        """验证修改增益起始值为为0-5之间的随机整数并触发拍摄"""
        gain_01_value = str(random.randint(0, 5))
        self.verify_setting_change_by_input(self.camera_setting_page.set_gain, gain_01_value, "Gain_Random")

    def test_gain_02_max(self):
        """验证修改增益为最大值（5）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_gain, "5", "Gain_max")

    def test_gain_03_min(self):
        """验证修改增益为最小值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_gain, "0", "Gain_min")

    def test_intensity_3d_01_1st_random(self):
        """验证修改3D_1次曝光强度为0.1-100之间保留一位小数的随机小数并触发拍摄"""
        self.camera_setting_page.set_exposure_num_single()# 切换2次曝光
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

    #恢复默认设置
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

class TestCamera05OverExposureFilter(TestCameraPublic):

    def test_over_exposure_filter_01_manual(self):
        """验证设置过曝滤除为手动模式并触发拍摄"""
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_exposure()  # 折叠【曝光】
        self.camera_setting_page.expand_reconstruction()  # 展开【重构】
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

class TestCamera06ValidPointJudgement(TestCameraPublic):

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

class TestCamera07BurrRemovalFilter(TestCameraPublic):

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

class TestCamera08PreProcess(TestCameraPublic):

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

class TestCamera093DDataFormat(TestCameraPublic):

    def test_3d_data_format_00_float_point_cloud(self):
        """验证切换浮点数点云并触发拍摄"""
        self.camera_setting_page.collapse_reconstruction()  # 折叠【重构】
        self.camera_setting_page.expand_post_process()
        self.verify_setting_change_by_click(self.camera_setting_page.set_float_point_cloud, "Float_Point_Cloud")

    def test_3d_data_format_01_fix_z_map(self):
        """验证切换深度图并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fix_z_map, "Fix_Z_Map")

    def test_3d_data_format_02_fix_z_map_simple(self):
        """验证切换简化深度图并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fix_z_map_simple, "Fix_Z_Map_Simple")

    def test_3d_data_format_03_fix_point_cloud(self):
        """验证切换定点数点云并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_fix_point_cloud, "Fix_Point_Cloud")

class TestCamera10RTMatrix(TestCameraPublic):

    def test_rt_matrix_00_enable(self):
        """验证启用矩阵变换并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_rt_matrix_enable, "rt_matrix_enable")

    def test_rt_matrix_01_theta_x_max(self):
        """验证矩阵变换通过参数设置θx为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x, "9.99", "theta_x_max")

    def test_rt_matrix_02_theta_x_min(self):
        """验证矩阵变换通过参数设置θx为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x, "-10", "theta_x_min")

    def test_rt_matrix_03_theta_x_random(self):
        """验证矩阵变换通过参数设置θx为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        theta_x_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x, theta_x_value, "theta_x_random")

    def test_rt_matrix_04_theta_x_default(self):
        """验证矩阵变换通过参数设置θx为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x, "0", "theta_x_default")

    def test_rt_matrix_05_theta_y_max(self):
        """验证矩阵变换通过参数设置θy为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y, "9.99", "theta_y_max")

    def test_rt_matrix_06_theta_y_min(self):
        """验证矩阵变换通过参数设置θy为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y, "-10", "theta_y_min")

    def test_rt_matrix_07_theta_y_random(self):
        """验证矩阵变换通过参数设置θy为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        theta_y_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y, theta_y_value, "theta_y_random")

    def test_rt_matrix_08_theta_y_default(self):
        """验证矩阵变换通过参数设置θy为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y, "0", "theta_y_default")

    def test_rt_matrix_09_theta_z_max(self):
        """验证矩阵变换通过参数设置θz为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z, "9.99", "theta_z_max")

    def test_rt_matrix_10_theta_z_min(self):
        """验证矩阵变换通过参数设置θz为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z, "-10", "theta_z_min")

    def test_rt_matrix_11_theta_z_random(self):
        """验证矩阵变换通过参数设置θz为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        theta_z_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z, theta_z_value, "theta_z_random")

    def test_rt_matrix_12_theta_z_default(self):
        """验证矩阵变换通过参数设置θz为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z, "0", "theta_z_default")

    def test_rt_matrix_13_kx_max(self):
        """验证矩阵变换通过参数设置kx为最大值（1.09）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_kx, "1.09", "kx_max")

    def test_rt_matrix_14_kx_min(self):
        """验证矩阵变换通过参数设置kx为最小值（0.9）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_kx, "0.9", "kx_min")

    def test_rt_matrix_15_kx_random(self):
        """验证矩阵变换通过参数设置kx为（0.9-1.09）之间保留两位小数的随机小数并触发拍摄"""
        kx_value = str(round(random.uniform(0.9, 1.09), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_kx, kx_value, "kx_random")

    def test_rt_matrix_16_kx_default(self):
        """验证矩阵变换通过参数设置kx为默认值（1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_kx, "1", "kx_default")

    def test_rt_matrix_17_ky_max(self):
        """验证矩阵变换通过参数设置ky为最大值（1.09）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_ky, "1.09", "ky_max")

    def test_rt_matrix_18_ky_min(self):
        """验证矩阵变换通过参数设置ky为最小值（0.9）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_ky, "0.9", "ky_min")

    def test_rt_matrix_19_ky_random(self):
        """验证矩阵变换通过参数设置ky为（0.9-1.09）之间保留两位小数的随机小数并触发拍摄"""
        ky_value = str(round(random.uniform(0.9, 1.09), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_ky, ky_value, "ky_random")

    def test_rt_matrix_20_ky_default(self):
        """验证矩阵变换通过参数设置ky为默认值（1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_ky, "1", "ky_default")

    def test_rt_matrix_21_kz_max(self):
        """验证矩阵变换通过参数设置kz为最大值（1.09）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_kz, "1.09", "kz_max")

    def test_rt_matrix_22_kz_min(self):
        """验证矩阵变换通过参数设置kz为最小值（0.9）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_kz, "0.9", "kz_min")

    def test_rt_matrix_23_kz_random(self):
        """验证矩阵变换通过参数设置kz为（0.9-1.09）之间保留两位小数的随机小数并触发拍摄"""
        kz_value = str(round(random.uniform(0.9, 1.09), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_kz, kz_value, "kz_random")

    def test_rt_matrix_24_kz_default(self):
        """验证矩阵变换通过参数设置kz为默认值（1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_kz, "1", "kz_default")

    def test_rt_matrix_25_bx_max(self):
        """验证矩阵变换通过参数设置bx为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx, "9.99", "bx_max")

    def test_rt_matrix_26_bx_min(self):
        """验证矩阵变换通过参数设置bx为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx, "-10", "bx_min")

    def test_rt_matrix_27_bx_random(self):
        """验证矩阵变换通过参数设置bx为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        bx_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx, bx_value, "bx_random")

    def test_rt_matrix_28_bx_default(self):
        """验证矩阵变换通过参数设置bx为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx, "0", "bx_default")

    def test_rt_matrix_29_by_max(self):
        """验证矩阵变换通过参数设置by为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_by, "9.99", "by_max")

    def test_rt_matrix_30_by_min(self):
        """验证矩阵变换通过参数设置by为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_by, "-10", "by_min")

    def test_rt_matrix_31_by_random(self):
        """验证矩阵变换通过参数设置by为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        by_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_by, by_value, "by_random")

    def test_rt_matrix_32_by_default(self):
        """验证矩阵变换通过参数设置by为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_by, "0", "by_default")

    def test_rt_matrix_33_bz_max(self):
        """验证矩阵变换通过参数设置bz为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz, "9.99", "bz_max")

    def test_rt_matrix_34_bz_min(self):
        """验证矩阵变换通过参数设置bz为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz, "-10", "bz_min")

    def test_rt_matrix_35_bz_random(self):
        """验证矩阵变换通过参数设置bz为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        bz_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz, bz_value, "bz_random")

    def test_rt_matrix_36_bz_default(self):
        """验证矩阵变换通过参数设置bz为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz, "0", "bz_default")

    def test_rt_matrix_37_disable(self):
        """验证启用矩阵变换并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_rt_matrix_disable, "rt_matrix_disable")

class TestCamera11FixPointDataScale(TestCameraPublic):

    def test_fix_point_data_scale_00_x0_position_default(self):
        """验证（设备：M051040）XO坐标值设置默认值（-25）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_x0_position, "-25", "x0_position_default")

    def test_fix_point_data_scale_01_x_increment_default(self):
        """验证（设备：M051040）X增量设置默认值（0.000762）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_x_increment, "0.000762", "x_increment_default")

    def test_fix_point_data_scale_02_y0_position_default(self):
        """验证（设备：M051040）YO坐标值设置默认值（-20.9）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_y0_position, "-20.9", "y0_position_default")

    def test_fix_point_data_scale_03_y_increment_default(self):
        """验证（设备：M051040）Y增量设置默认值（0.000636）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_y_increment, "0.000636", "y_increment_default")

    def test_fix_point_data_scale_04_z0_position_default(self):
        """验证（设备：M051040）YO坐标值设置默认值（-6）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_z0_position, "-6", "z0_position_default")

    def test_fix_point_data_scale_05_z_increment_default(self):
        """验证（设备：M051040）Y增量设置默认值（0.000184）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_z_increment, "0.000184", "z_increment_default")

class TestCamera12RangeCheck(TestCameraPublic):

    def test_range_check_00_enable(self):
        """验证启用范围检查并触发拍摄"""
        self.camera_setting_page.scroll_down()  # 滚动条下滑
        self.verify_setting_change_by_click(self.camera_setting_page.set_range_check_enable, "range_check_enable")

    def test_range_check_01_x_min_default(self):
        """验证（设备：M051040）范围检查X最小值设置默认值（-10000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_x_min, "-10000", "x_min_default")

    def test_range_check_02_x_max_default(self):
        """验证（设备：M051040）范围检查X最大值设置默认值（10000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_x_max, "10000", "x_max_default")

    def test_range_check_03_y_min_default(self):
        """验证（设备：M051040）范围检查Y最小值设置默认值（-10000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_y_min, "-10000", "y_min_default")

    def test_range_check_04_y_max_default(self):
        """验证（设备：M051040）范围检查Y最大值设置默认值（10000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_y_max, "10000", "y_max_default")

    def test_range_check_05_z_min_default(self):
        """验证（设备：M051040）范围检查Z最小值设置默认值（-10000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_z_min, "-10000", "z_min_default")

    def test_range_check_06_z_max_default(self):
        """验证（设备：M051040）范围检查Z最大值设置默认值（10000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_z_max, "10000", "z_max_default")

    def test_range_check_07_disable(self):
        """验证关闭范围检查并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_range_check_disable, "range_check_disable")

# class TestCamera11FixPointDataScale(TestCameraPublic):
#
#     def test_fix_point_data_scale_00_x0_position_default(self):
#         """验证（设备：M051280）XO坐标值设置默认值（-200.2）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_x0_position, "-200.2", "x0_position_default")
#
#     def test_fix_point_data_scale_01_x_increment_default(self):
#         """验证（设备：M051280）X增量设置默认值（0.006）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_x_increment, "0.006", "x_increment_default")
#
#     def test_fix_point_data_scale_02_y0_position_default(self):
#         """验证（设备：M051280）YO坐标值设置默认值（-167.1）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_y0_position, "-167.1", "y0_position_default")
#
#     def test_fix_point_data_scale_03_y_increment_default(self):
#         """验证（设备：M051280）Y增量设置默认值（0.0051）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_y_increment, "0.0051", "y_increment_default")
#
#     def test_fix_point_data_scale_04_z0_position_default(self):
#         """验证（设备：M051280）YO坐标值设置默认值（-120）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_z0_position, "-120", "z0_position_default")
#
#     def test_fix_point_data_scale_05_z_increment_default(self):
#         """验证（设备：M051280）Y增量设置默认值（0.00019）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_z_increment, "0.003663", "z_increment_default")

# class TestCamera12RangeCheck(TestCameraPublic):
#
#     def test_range_check_00_enable(self):
#         """验证启用范围检查并触发拍摄"""
#         self.camera_setting_page.scroll_down()  # 滚动条下滑
#         self.verify_setting_change_by_click(self.camera_setting_page.set_range_check_enable, "range_check_enable")
#
#     def test_range_check_01_x_min_default(self):
#         """验证（设备：M051280）范围检查X最小值设置默认值（-420）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_x_min, "-420", "x_min_default")
#
#     def test_range_check_02_x_max_default(self):
#         """验证（设备：M051280）范围检查X最大值设置默认值（420）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_x_max, "420", "x_max_default")
#
#     def test_range_check_03_y_min_default(self):
#         """验证（设备：M051280）范围检查Y最小值设置默认值（-350.8）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_y_min, "-350.8", "y_min_default")
#
#     def test_range_check_04_y_max_default(self):
#         """验证（设备：M051280）范围检查Y最大值设置默认值（350.8）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_y_max, "350.8", "y_max_default")
#
#     def test_range_check_05_z_min_default(self):
#         """验证（设备：M051280）范围检查Z最小值设置默认值（-32.6）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_z_min, "-210.0", "z_min_default")
#
#     def test_range_check_06_z_max_default(self):
#         """验证（设备：M051280）范围检查Z最大值设置默认值（32.6）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_z_max, "210.0", "z_max_default")
#
#     def test_range_check_07_disable(self):
#         """验证关闭范围检查并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_range_check_disable, "range_check_disable")

class TestCamera13General(TestCameraPublic):

    def test_general_00_auto_sleep_enable(self):
        """验证启用自动休眠并触发拍摄"""
        self.camera_setting_page.collapse_post_process()  # 折叠【后处理】
        self.verify_setting_change_by_click(self.camera_setting_page.set_auto_sleep_enable, "auto_sleep_enable")

    def test_general_01_auto_sleep_max(self):
        """验证自动休眠设置为最大值（65535）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,"65535", "auto_sleep_max")

    def test_general_02_auto_sleep_min(self):
        """验证自动休眠通过参数设置为最小值（100）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,"100", "auto_sleep_min")

    def test_general_03_auto_sleep_random(self):
        """验证自动休眠设置为（100-65535）之间保留两位小数的随机小数并触发拍摄"""
        auto_sleep_value = str(random.randint(100, 65535))
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,auto_sleep_value, "auto_sleep_random")

    def test_general_04_auto_sleep_default(self):
        """验证自动休眠设置为默认值（5000）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_auto_sleep_setting,"5000", "auto_sleep_default")

    def test_general_05_auto_sleep_disable(self):
        """验证关闭自动休眠并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_auto_sleep_disable, "auto_sleep_disable")

    def test_general_06_correct_distortion_enable(self):
        """验证启用矫正畸变并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_correct_distortion_enable, "correct_distortion_enable")

    def test_general_07_correct_distortion_disable(self):
        """验证关闭矫正畸变并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_correct_distortion_disable, "correct_distortion_disable")

# class TestCamera14CorrectDistortionSettings(TestCameraPublic):
#
#     def test_correct_distortion_00_read_correct_param(self):
#         """验证读取矫正畸变参数"""
#         self.camera_setting_page.expand_basic()  # 展开基本设置
#         self.camera_setting_page.set_white()  # 切换2d_白照明模式
#         self.camera_setting_page.expert_setting_enable()  # 启用专业设置，并切换到专业设置tab
#         self.verify_setting_change_by_click(self.camera_setting_page.read_correct_distortion_parm, "read_correct_distortion_parm")
#
#     def test_flip_setting_01_x(self):
#         """验证翻转设置X翻转并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_flip_x, "flip_x")
#         self.camera_setting_page.set_flip_x_unselect()
#
#     def test_flip_setting_02_y(self):
#         """验证翻转设置Y翻转并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_flip_y, "flip_y")
#         self.camera_setting_page.set_flip_y_unselect()
#
#     def test_flip_setting_03_all(self):
#         """验证翻转设置XY翻转全选并触发拍摄"""
#         self.camera_setting_page.set_flip_x()
#         self.verify_setting_change_by_click(self.camera_setting_page.set_flip_y, "flip_xy")
#
#     def test_flip_setting_04_unselect(self):
#         """验证翻转设置XY翻转全不选并触发拍摄"""
#         self.camera_setting_page.set_flip_x_unselect()
#         self.verify_setting_change_by_click(self.camera_setting_page.set_flip_y_unselect, "flip_xy_unselect")
#         self.camera_setting_page.switch_setting_table()  # 切回设置table
#         self.camera_setting_page.set_fast()  # 切回换3d_快速模式
#         self.camera_setting_page.expert_setting_disable()  # 关闭专业设置