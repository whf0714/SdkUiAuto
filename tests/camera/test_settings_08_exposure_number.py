from tests.camera.test_camera_public import TestCameraPublic

class TestCameraExposureNumber(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        self.camera_setting_page.collapse_basic() #折叠【基本】
        self.camera_setting_page.collapse_multi_head()#折叠【多头】

    def test_exposure_number_01_double(self):
        """验证切换2次曝光并触发拍摄"""
        # self.camera_setting_page.collapse_basic()
        # self.camera_setting_page.collapse_multi_head()
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_num_double, "DoubleExposure")

    def test_exposure_number_02_triple(self):
        """验证切换3次曝光并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_num_triple, "TripleExposure")

    def test_exposure_number_03_single(self):
        """验证切换1次曝光并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_exposure_num_single, "SingleExposure")