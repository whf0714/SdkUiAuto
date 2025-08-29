from tests.camera.test_camera_public import TestCameraPublic
import random
import time


class TestCameraExternalExposure(TestCameraPublic):

    # def setUp(self):
    #     super().setUp()  # 保留父类初始化
    #     # 所有测试用例的公共前置操作
    #     self.camera_setting_page.collapse_basic() # 折叠【基本】
    #     self.camera_setting_page.collapse_multi_head()# 折叠【多头】
    #     self.camera_setting_page.collapse_exposure()# 折叠【曝光】
    #     self.camera_setting_page.expand_external_exposure()# 展开【外部曝光】

    def test_external_exposure_01_enable_white(self):
        """验证仅开启白光使能并触发拍摄"""
        self.camera_setting_page.collapse_basic()  # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()  # 折叠【多头】
        self.camera_setting_page.collapse_exposure()  # 折叠【曝光】
        self.camera_setting_page.expand_external_exposure() # 展开【外部曝光】
        self.verify_setting_change_by_click(lambda:self.camera_setting_page.set_single_exposure_enable('white'),"External_Exposure_Enable_White")

    def test_external_exposure_02_enable_rgb(self):
        """验证仅开启RGB使能并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_single_exposure_enable('rgb'),"External_Exposure_Enable_RGB")

    def test_external_exposure_03_enable_all(self):
        """验证开启白光使能 & RGB使能并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_all_exposure_enable( True),"External_Exposure_Enable_All")

    def test_external_exposure_04_enable_unselect(self):
        """验证不开启白光使能 & RGB使能并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_all_exposure_enable(False),"External_Exposure_Enable_Unselect")

    def test_external_exposure_05_time_white_min(self):
        """验证外部曝光时间_白照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_white,"0", "External_Exposure_Time_White_0")

    def test_external_exposure_06_time_white_max(self):
        """验证外部曝光时间_白照明为最大值(10000)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_white, "10000","External_Exposure_Time_White_10000")

    def test_external_exposure_07_time_white_random(self):
        """验证外部曝光时间_白照明为0-10000之间的随机整数能并触发拍摄"""
        white_random_value = str(random.randint(0, 10000))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_white, white_random_value,"External_Exposure_Time_White_Random")

    def test_external_exposure_08_time_red_min(self):
        """验证外部曝光时间_红照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_red, "0","External_Exposure_Time_Red_0")

    def test_external_exposure_09_time_red_max(self):
        """验证外部曝光时间_红照明为最大值(10000)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_red, "10000","External_Exposure_Time_Red_10000")

    def test_external_exposure_10_time_red_random(self):
        """验证外部曝光时间_红照明为0-10000之间的随机整数能并触发拍摄"""
        red_random_value = str(random.randint(0, 10000))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_red,red_random_value, "External_Exposure_Time_Red_Random")

    def test_external_exposure_11_time_green_min(self):
        """验证外部曝光时间_绿照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_green, "0","External_Exposure_Time_Green_0")

    def test_external_exposure_12_time_green_max(self):
        """验证外部曝光时间_绿照明为最大值(10000)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_green, "10000","External_Exposure_Time_Green_10000")

    def test_external_exposure_13_time_green_random(self):
        """验证外部曝光时间_绿照明为0-10000之间的随机整数能并触发拍摄"""
        green_random_value = str(random.randint(0, 10000))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_green,green_random_value, "External_Exposure_Time_Green_Random")

    def test_external_exposure_14_time_blue_min(self):
        """验证外部曝光时间_蓝照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_blue, "0","External_Exposure_Time_Blue_0")

    def test_external_exposure_15_time_blue_max(self):
        """验证外部曝光时间_蓝照明为最大值(10000)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_blue, "10000","External_Exposure_Time_Blue_10000")

    def test_external_exposure_16_time_blue_random(self):
        """验证外部曝光时间_蓝照明为0-10000之间的随机整数能并触发拍摄"""
        blue_random_value = str(random.randint(0, 10000))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_blue, blue_random_value, "External_Exposure_Time_Blue_Random")

    def test_external_exposure_17_time_default(self):
        """验证外部曝光时间为默认设置(700,800,850,750)并触发拍摄"""
        self.camera_setting_page.set_external_exposure_time_white("700")
        self.camera_setting_page.set_external_exposure_time_red("800")
        self.camera_setting_page.set_external_exposure_time_green("850")
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_time_blue, "750","External_Exposure_Time_Default")

    def test_external_exposure_18_gain_white_min(self):
        """验证外部曝光增益_白照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_white,"0", "External_Exposure_Gain_White_0")

    def test_external_exposure_19_gain_white_max(self):
        """验证外部曝光增益_白照明为最大值(4)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_white, "4","External_Exposure_Gain_White_4")

    def test_external_exposure_20_gain_white_random(self):
        """验证外部曝光增益_白照明为0-4之间的随机整数能并触发拍摄"""
        white_random_value = str(random.randint(0, 4))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_white, white_random_value,"External_Exposure_Gain_White_Random")

    def test_external_exposure_21_gain_red_min(self):
        """验证外部曝光增益_红照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_red, "0","External_Exposure_Gain_Red_0")

    def test_external_exposure_22_gain_red_max(self):
        """验证外部曝光增益_红照明为最大值(4)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_red, "4","External_Exposure_Gain_Red_4")

    def test_external_exposure_23_gain_red_random(self):
        """验证外部曝光增益_红照明为0-4之间的随机整数能并触发拍摄"""
        red_random_value = str(random.randint(0, 4))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_red,red_random_value, "External_Exposure_Gain_Red_Random")

    def test_external_exposure_24_gain_green_min(self):
        """验证外部曝光增益_绿照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_green, "0","External_Exposure_Gain_Green_0")

    def test_external_exposure_25_gain_green_max(self):
        """验证外部曝光增益_绿照明为最大值(4)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_green, "4","External_Exposure_Gain_Green_4")

    def test_external_exposure_26_gain_green_random(self):
        """验证外部曝光增益_绿照明为0-4之间的随机整数能并触发拍摄"""
        green_random_value = str(random.randint(0, 4))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_green,green_random_value, "External_Exposure_Gain_Green_Random")

    def test_external_exposure_27_gain_blue_min(self):
        """验证外部曝光增益_蓝照明为最小值(0)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_blue, "0","External_Exposure_Gain_Blue_0")

    def test_external_exposure_28_gain_blue_max(self):
        """验证外部曝光增益_蓝照明为最大值(4)能并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_blue, "4","External_Exposure_Gain_Blue_4")

    def test_external_exposure_29_gain_blue_random(self):
        """验证外部曝光增益_蓝照明为0-4之间的随机整数能并触发拍摄"""
        blue_random_value = str(random.randint(0, 4))
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_blue, blue_random_value, "External_Exposure_Gain_Blue_Random")

    def test_external_exposure_30_gain_default(self):
        """验证外部曝光增益为默认设置(0,0,0,0)并触发拍摄"""
        self.camera_setting_page.set_external_exposure_gain_white("0")
        self.camera_setting_page.set_external_exposure_gain_red("0")
        self.camera_setting_page.set_external_exposure_gain_green("0")
        self.verify_setting_change_by_input(self.camera_setting_page.set_external_exposure_gain_blue, "0","External_Exposure_Gain_Default")