from tests.camera.test_camera_public import TestCameraPublic
from itertools import combinations

class TestCameraProjectionMode(TestCameraPublic):

    ###############################测试投影模式（自动生成所有投影组合）##############################

    # def verify_projector_selection(self, projector_indices, setting_name):
    #     """
    #     验证投影模式的组合选择
    #     :param projector_indices: 要选择的投影列表
    #     :param setting_name: 投影模式的描述
    #     """
    #     self.verify_setting_change_by_click(
    #         lambda: self.camera_setting_page.set_projectors_by_indices(projector_indices),
    #         setting_name
    #     )
    #
    # def test_projector_mode_all_unselect(self):
    #     """验证投影模式全不选并触发拍摄"""
    #     self.verify_projector_selection([], "ProjectorUnselect")
    #
    # def test_projector_mode_combinations(self):
    #     """自动生成所有投影组合并执行测试并触发拍摄"""
    #     for r in range(1, 5):  # 从单个投影到四个投影的所有组合
    #         for combination in combinations(range(4), r):
    #             setting_name = f"ProjectorMode{''.join(map(str, combination))}"
    #             self.verify_projector_selection(list(combination), setting_name)
    #
    # def test_projector_mode_all_select(self):
    #     """验证投影模式全选并触发拍摄"""
    #     self.verify_projector_selection(range(4), "ProjectorSelectAll")

###############################测试投影模式（自定义组合）##############################


    def test_projector_mode_01_unselect(self):
        """验证投影模式全不选并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_all_projectors, "ProjectorUnselect")

    def test_projector_mode_02_single_0(self):
        """验证切换投影模式（0）并触发拍摄"""
        # 传递一个匿名函数（lambda），用于在点击时切换到投影模式0
        self.verify_setting_change_by_click(lambda:self.camera_setting_page.set_single_projector(0), "ProjectorMode0")

    def test_projector_mode_03_single_1(self):
        """验证切换投影模式（1）并触发拍摄"""
        self.verify_setting_change_by_click(lambda:self.camera_setting_page.set_single_projector(1), "ProjectorMode1")

    def test_projector_mode_04_single_2(self):
        """验证切换投影模式（2）并触发拍摄"""
        self.verify_setting_change_by_click(lambda:self.camera_setting_page.set_single_projector(2), "ProjectorMode2")

    def test_projector_mode_05_single_3(self):
        """验证切换投影模式（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda:self.camera_setting_page.set_single_projector(3), "ProjectorMode3")

    def test_projector_mode_06_multiple_01(self):
        """验证同时选择投影模式（0）和（1）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([0, 1]),"ProjectorMode01")

    def test_projector_mode_07_multiple_02(self):
        """验证同时选择投影模式（0）和（2）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([0, 2]),"ProjectorMode02")

    def test_projector_mode_08_multiple_03(self):
        """验证同时选择投影模式（0）和（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([0, 3]),"ProjectorMode03")

    def test_projector_mode_09_multiple_12(self):
        """验证同时选择投影模式（1）和（2）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([1, 2]),"ProjectorMode12")

    def test_projector_mode_10_multiple_13(self):
        """验证同时选择投影模式（1）和（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([1, 3]),"ProjectorMode13")

    def test_projector_mode_11_multiple_23(self):
        """验证同时选择投影模式（2）和（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([2, 3]),"ProjectorMode23")

    def test_projector_mode_12_multiple_012(self):
        """验证同时选择投影模式（0）（1）（2）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([0, 1, 2]),"ProjectorMode012")

    def test_projector_mode_13_multiple_013(self):
        """验证同时选择投影模式（0）（1）（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([0, 1, 3]),"ProjectorMode013")

    def test_projector_mode_14_multiple_023(self):
        """验证同时选择投影模式（0）（2）（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([0, 2, 3]),"ProjectorMode023")

    def test_projector_mode_15_multiple_123(self):
        """验证同时选择投影模式（1）（2）（3）并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_multiple_projector([1, 2, 3]),"ProjectorMode123")

    def test_projector_mode_16_all(self):
        """验证投影模式全选并触发拍摄"""
        self.verify_setting_change_by_click(lambda: self.camera_setting_page.set_all_projectors(True),"ProjectorSelectAll")
