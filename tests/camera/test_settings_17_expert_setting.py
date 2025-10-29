from tests.camera.test_camera_public import TestCameraPublic
import random


class TestCorrectDistortionSettings(TestCameraPublic):

    def test_correct_distortion_00_read_correct_param(self):
        """验证读取矫正畸变参数"""
        self.camera_setting_page.expert_setting_enable()  # 启用专业设置，并切换到专业设置tab
        self.verify_setting_change_by_click(self.camera_setting_page.read_correct_distortion_parm, "read_correct_distortion_parm")
        self.camera_setting_page.switch_setting_table()  # 切回设置table
        self.camera_setting_page.expert_setting_disable()  # 关闭专业设置

    # def test_correct_distortion_01_do_correct_distortion(self):############有问题 找不到点击矫正畸变后的弹窗
    #     """验证操作矫正畸变"""
    #     self.verify_setting_change_by_click(self.camera_setting_page.do_correct_distortion, "do_correct_distortion")


##################################2.754之后仅单头设备支持投影仪ROI裁切##################
# class TestExposureRoiSettings(TestCameraPublic):
#
#     def test_exposure_roi_setting_01_num_random(self):
#         """验证修改曝光区域数量为0-4之间的随机整数并触发拍摄"""
#         self.camera_setting_page.set_single_projector(0)  # 投影模式设置为单头
#         self.camera_setting_page.expert_setting_enable()  # 启用专业设置，并切换到专业设置tab
#         num_random_value = str(random.randint(0, 4))
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_num, num_random_value, "exposure_roi_setting_num_Random")
#
#     def test_exposure_roi_setting_02_num_max(self):
#         """验证修改曝光区域数量为最大值（4）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_num, "4","exposure_roi_setting_num_max")
#
#     def test_exposure_roi_setting_03_index_random(self):
#         """验证修改曝光区域序号为1-4之间的随机整数并触发拍摄"""
#         index_random_value = str(random.randint(1, 4))
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_index, index_random_value, "exposure_roi_setting_index_Random")
#
#     def test_exposure_roi_setting_04_index_max(self):
#         """验证修改曝光区域序号为最大值（4）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_index, "4","exposure_roi_setting_index_max")
#
#     def test_exposure_roi_setting_05_positive(self):
#         """验证修改曝光区域设置为正极性并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_exp_roi_positive,"exposure_roi_setting_positive")
#
#     def test_exposure_roi_setting_06_negative(self):
#         """验证修改曝光区域设置为负极性并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_exp_roi_negative,"exposure_roi_setting_index_negative")
#
#     def test_exposure_roi_setting_07_is_base_enable(self):
#         """验证修改曝光区域设置启用基准面并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_exp_roi_is_base_enable,"exposure_roi_setting_is_base_enable")
#
#     def test_exposure_roi_setting_08_is_base_disable(self):
#         """验证修改曝光区域设置不启用基准面并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_exp_roi_is_base_disable,"exposure_roi_setting_is_base_disable")
#
#     def test_exposure_roi_setting_09_shape(self):######有问题
#         """设置曝光区域形状并触发拍摄"""
#         self.verify_setting_change_by_click(self.camera_setting_page.set_exp_roi_shape,"set_exp_roi_shape")
#         # selected_shape = self.camera_setting_page.set_exp_roi_shape()
#         # print(selected_shape)
#
#     def test_exposure_roi_setting_10_x_center_random(self):
#         """验证修改曝光区域中心X为0-911之间的随机整数并触发拍摄"""
#         x_center_random_value = str(random.randint(0, 911))
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_x_center, x_center_random_value, "exposure_roi_setting_x_center_Random")
#
#     def test_exposure_roi_setting_11_x_center_max(self):
#         """验证修改曝光区域中心X为最大值（911）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_x_center, "911","exposure_roi_setting_x_center_max")
#
#     def test_exposure_roi_setting_12_x_center_min(self):
#         """验证修改曝光区域中心X为最小值（0）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_x_center, "0", "exposure_roi_setting_x_center_min")
#
#     def test_exposure_roi_setting_13_x_center_default(self):
#         """验证修改曝光区域中心X为默认值（450）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_x_center, "450", "exposure_roi_setting_x_center_default")
#
#     def test_exposure_roi_setting_14_y_center_random(self):
#         """验证修改曝光区域中心Y为0-569之间的随机整数并触发拍摄"""
#         y_center_random_value = str(random.randint(0, 569))
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_y_center, y_center_random_value, "exposure_roi_setting_y_center_Random")
#
#     def test_exposure_roi_setting_15_y_center_max(self):
#         """验证修改曝光区域中心Y为最大值（569）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_y_center, "569","exposure_roi_setting_y_center_max")
#
#     def test_exposure_roi_setting_16_y_center_min(self):
#         """验证修改曝光区域中心Y为最小值（0）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_y_center, "0", "exposure_roi_setting_y_center_min")
#
#     def test_exposure_roi_setting_17_y_center_default(self):
#         """验证修改曝光区域中心Y为默认值（290）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_y_center, "290", "exposure_roi_setting_y_center_default")
#
#     def test_exposure_roi_setting_18_width_random(self):
#         """验证修改曝光区域宽度为2-911之间的随机整数并触发拍摄"""
#         width_random_value = str(random.randint(2, 911))
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_width, width_random_value, "exposure_roi_setting_width_Random")
#
#     def test_exposure_roi_setting_19_width_max(self):
#         """验证修改曝光区域宽度为最大值（911）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_width, "911","exposure_roi_setting_width_max")
#
#     def test_exposure_roi_setting_20_width_min(self):
#         """验证修改曝光区域宽度为最小值（2）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_width, "2", "exposure_roi_setting_width_min")
#
#     def test_exposure_roi_setting_21_width_default(self):
#         """验证修改曝光区域宽度为默认值（300）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_width, "300", "exposure_roi_setting_width_default")
#
#     def test_exposure_roi_setting_22_height_random(self):
#         """验证修改曝光区域高度为0-569之间的随机整数并触发拍摄"""
#         height_random_value = str(random.randint(0, 569))
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_height, height_random_value, "exposure_roi_setting_height_Random")
#
#     def test_exposure_roi_setting_23_height_max(self):
#         """验证修改曝光区域高度为最大值（569）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_height, "569","exposure_roi_setting_height_max")
#
#     def test_exposure_roi_setting_24_height_min(self):
#         """验证修改曝光区域高度为最小值（0）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_height, "0", "exposure_roi_setting_height_min")
#
#     def test_exposure_roi_setting_25_height_default(self):
#         """验证修改曝光区域高度为默认值（150）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_height, "150", "exposure_roi_setting_height_default")
#
#     def test_exposure_roi_setting_26_index_min(self):
#         """验证修改曝光区域序号为最小值（1）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_index, "1", "exposure_roi_setting_index")
#
#     def test_exposure_roi_setting_27_num_min(self):
#         """验证修改曝光区域数量为最小值（0）并触发拍摄"""
#         self.verify_setting_change_by_input(self.camera_setting_page.set_exp_roi_num, "0", "exposure_roi_setting_num_min")
#         self.camera_setting_page.switch_setting_table()  # 切回设置table
#         self.camera_setting_page.set_all_projectors(True)  # 投影模式恢复四头
#         self.camera_setting_page.expert_setting_disable()  # 关闭专业设置

class TestSuppressExposureSettings(TestCameraPublic):

    def test_suppress_exposure_01_all(self):
        """验证曝光抑制全选并触发拍摄"""
        self.camera_setting_page.expert_setting_enable()  # 启用专业设置，并切换到专业设置tab
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_all_suppress_exposure(True),"suppress_exposure_All")

    def test_suppress_exposure_02_single_1(self):
        """验证切换曝光抑制1并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_single_suppress_exposure(1),"suppress_exposure_SuppressExpo1")

    def test_suppress_exposure_03_single_2(self):
        """验证切换曝光抑制2并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_single_suppress_exposure(2),"suppress_exposure_SuppressExpo2")

    def test_suppress_exposure_04_single_3(self):
        """验证切换曝光抑制3并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_single_suppress_exposure(3),"suppress_exposure_SuppressExpo3")

    def test_suppress_exposure_05_multiple_12(self):
        """验证同时选择曝光抑制（1）和（2）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_suppress_exposure([1, 2]),"suppress_exposure_SuppressExpo12")

    def test_suppress_exposure_06_multiple_13(self):
        """验证同时选择曝光抑制（1）和（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_suppress_exposure([1, 3]),"suppress_exposure_SuppressExpo13")

    def test_suppress_exposure_07_multiple_23(self):
        """验证同时选择曝光抑制（2）和（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_suppress_exposure([2, 3]),"suppress_exposure_SuppressExpo23")

    def test_suppress_exposure_08_unselect(self):
        """验证曝光抑制全不选并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_all_suppress_exposure, "suppress_exposure_Unselect")
        self.camera_setting_page.switch_setting_table()  # 切回设置table
        self.camera_setting_page.expert_setting_disable()  # 关闭专业设置

class TestFlipSettings(TestCameraPublic):
    def test_flip_setting_01_x(self):
        """验证翻转设置X翻转并触发拍摄"""
        self.camera_setting_page.expand_basic() #展开基本设置
        self.camera_setting_page.set_white()#切换2d_白照明模式
        self.camera_setting_page.expert_setting_enable()  # 启用专业设置，并切换到专业设置tab
        # self.camera_setting_page.scroll_down()  # 滚动条下滑
        self.verify_setting_change_by_click(self.camera_setting_page.set_flip_x, "flip_x")
        self.camera_setting_page.set_flip_x_unselect()

    def test_flip_setting_02_y(self):
        """验证翻转设置Y翻转并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_flip_y, "flip_y")
        self.camera_setting_page.set_flip_y_unselect()

    def test_flip_setting_03_all(self):
        """验证翻转设置XY翻转全选并触发拍摄"""
        self.camera_setting_page.set_flip_x()
        self.verify_setting_change_by_click(self.camera_setting_page.set_flip_y, "flip_xy")

    def test_flip_setting_04_unselect(self):
        """验证翻转设置XY翻转全不选并触发拍摄"""
        self.camera_setting_page.set_flip_x_unselect()
        self.verify_setting_change_by_click(self.camera_setting_page.set_flip_y_unselect, "flip_xy_unselect")
        self.camera_setting_page.switch_setting_table()  # 切回设置table
        self.camera_setting_page.set_fast()  # 切回换3d_快速模式
        self.camera_setting_page.expert_setting_disable()  # 关闭专业设置