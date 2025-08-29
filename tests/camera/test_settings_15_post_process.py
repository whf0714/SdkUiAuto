from tests.camera.test_camera_public import TestCameraPublic
import random

class TestCamera3DDataFormat(TestCameraPublic):

    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        self.camera_setting_page.collapse_external_exposure()  # 折叠【外部曝光】
        self.camera_setting_page.collapse_reconstruction()  # 折叠【重构】
        self.camera_setting_page.expand_post_process()# 展开【后处理】

    def test_3d_data_format_00_float_point_cloud(self):
        """验证切换浮点数点云并触发拍摄"""
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

class TestCameraRTMatrix(TestCameraPublic):
    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        self.camera_setting_page.expand_post_process()# 展开【后处理】

    def test_rt_matrix_00_enable(self):
        """验证启用矩阵变换并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_rt_matrix_enable, "rt_matrix_enable")

    def test_rt_matrix_01_theta_x_max(self):
        """验证矩阵变换通过参数设置θx为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x,"9.99", "theta_x_max")

    def test_rt_matrix_02_theta_x_min(self):
        """验证矩阵变换通过参数设置θx为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x,"-10", "theta_x_min")

    def test_rt_matrix_03_theta_x_random(self):
        """验证矩阵变换通过参数设置θx为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        theta_x_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x,theta_x_value, "theta_x_random")

    def test_rt_matrix_04_theta_x_default(self):
        """验证矩阵变换通过参数设置θx为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_x,"0", "theta_x_default")

    def test_rt_matrix_05_theta_y_max(self):
        """验证矩阵变换通过参数设置θy为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y,"9.99", "theta_y_max")

    def test_rt_matrix_06_theta_y_min(self):
        """验证矩阵变换通过参数设置θy为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y,"-10", "theta_y_min")

    def test_rt_matrix_07_theta_y_random(self):
        """验证矩阵变换通过参数设置θy为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        theta_y_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y,theta_y_value, "theta_y_random")

    def test_rt_matrix_08_theta_y_default(self):
        """验证矩阵变换通过参数设置θy为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_y,"0", "theta_y_default")

    def test_rt_matrix_09_theta_z_max(self):
        """验证矩阵变换通过参数设置θz为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z,"9.99", "theta_z_max")

    def test_rt_matrix_10_theta_z_min(self):
        """验证矩阵变换通过参数设置θz为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z,"-10", "theta_z_min")

    def test_rt_matrix_11_theta_z_random(self):
        """验证矩阵变换通过参数设置θz为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        theta_z_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z,theta_z_value, "theta_z_random")

    def test_rt_matrix_12_theta_z_default(self):
        """验证矩阵变换通过参数设置θz为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_theta_z,"0", "theta_z_default")

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
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx,"9.99", "bx_max")

    def test_rt_matrix_26_bx_min(self):
        """验证矩阵变换通过参数设置bx为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx,"-10", "bx_min")

    def test_rt_matrix_27_bx_random(self):
        """验证矩阵变换通过参数设置bx为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        bx_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx,bx_value, "bx_random")

    def test_rt_matrix_28_bx_default(self):
        """验证矩阵变换通过参数设置bx为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bx,"0", "bx_default")

    def test_rt_matrix_29_by_max(self):
        """验证矩阵变换通过参数设置by为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_by,"9.99", "by_max")

    def test_rt_matrix_30_by_min(self):
        """验证矩阵变换通过参数设置by为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_by,"-10", "by_min")

    def test_rt_matrix_31_by_random(self):
        """验证矩阵变换通过参数设置by为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        by_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_by,by_value, "by_random")

    def test_rt_matrix_32_by_default(self):
        """验证矩阵变换通过参数设置by为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_by,"0", "by_default")

    def test_rt_matrix_33_bz_max(self):
        """验证矩阵变换通过参数设置bz为最大值（9.99）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz,"9.99", "bz_max")

    def test_rt_matrix_34_bz_min(self):
        """验证矩阵变换通过参数设置bz为最小值（-10）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz,"-10", "bz_min")

    def test_rt_matrix_35_bz_random(self):
        """验证矩阵变换通过参数设置bz为（-10-9.99）之间保留两位小数的随机小数并触发拍摄"""
        bz_value = str(round(random.uniform(-10, 9.99), 2))
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz,bz_value, "bz_random")

    def test_rt_matrix_36_bz_default(self):
        """验证矩阵变换通过参数设置bz为默认值（0）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_bz,"0", "bz_default")

    def test_rt_matrix_37_disable(self):
        """验证启用矩阵变换并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_rt_matrix_disable, "rt_matrix_disable")


class TestCameraFixPointDataScale(TestCameraPublic):
    def setUp(self):
        super().setUp()  # 保留父类初始化
        # 所有测试用例的公共前置操作
        self.camera_setting_page.collapse_basic() # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()# 折叠【多头】
        self.camera_setting_page.collapse_exposure()# 折叠【曝光】
        self.camera_setting_page.expand_post_process()# 展开【后处理】

    def test_fix_point_data_scale_00_x0_position_default(self):
        """验证（设备：SQ081043）XO坐标值设置默认值（-26.1）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_x0_position,"-26.1", "x0_position_default")

    def test_fix_point_data_scale_01_x_increment_default(self):
        """验证（设备：SQ081043）X增量设置默认值（0.0008）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_x_increment,"0.0008", "x_increment_default")

    def test_fix_point_data_scale_02_y0_position_default(self):
        """验证（设备：SQ081043）YO坐标值设置默认值（-26）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_y0_position,"-26", "y0_position_default")

    def test_fix_point_data_scale_03_y_increment_default(self):
        """验证（设备：SQ081043）Y增量设置默认值（0.0008）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_y_increment,"0.0008", "y_increment_default")

    def test_fix_point_data_scale_04_z0_position_default(self):
        """验证（设备：SQ081043）YO坐标值设置默认值（-6）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_z0_position,"-6", "z0_position_default")

    def test_fix_point_data_scale_05_z_increment_default(self):
        """验证（设备：SQ081043）Y增量设置默认值（0.00019）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_z_increment,"0.00019", "z_increment_default")

class TestCameraRangeCheck(TestCameraPublic):

    def test_range_check_00_enable(self):
        """验证启用范围检查并触发拍摄"""
        self.camera_setting_page.collapse_basic()  # 折叠【基本】
        self.camera_setting_page.collapse_multi_head()  # 折叠【多头】
        self.camera_setting_page.collapse_exposure()  # 折叠【曝光】
        self.camera_setting_page.expand_post_process()  # 展开【后处理】
        self.camera_setting_page.scroll_down()  # 滚动条下滑
        self.verify_setting_change_by_click(self.camera_setting_page.set_range_check_enable, "range_check_enable")

    def test_range_check_01_x_min_default(self):
        """验证（设备：SQ081043）范围检查X最小值设置默认值（-65.2）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_x_min,"-65.2", "x_min_default")

    def test_range_check_02_x_max_default(self):
        """验证（设备：SQ081043）范围检查X最大值设置默认值（65.2）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_x_max,"65.2", "x_max_default")

    def test_range_check_03_y_min_default(self):
        """验证（设备：SQ081043）范围检查Y最小值设置默认值（-65）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_y_min,"-65", "y_min_default")

    def test_range_check_04_y_max_default(self):
        """验证（设备：SQ081043）范围检查Y最大值设置默认值（65）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_y_max,"65", "y_max_default")

    def test_range_check_05_z_min_default(self):
        """验证（设备：SQ081043）范围检查Z最小值设置默认值（-32.6）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_z_min,"-32.6", "z_min_default")

    def test_range_check_06_z_max_default(self):
        """验证（设备：SQ081043）范围检查Z最大值设置默认值（32.6）并触发拍摄"""
        self.verify_setting_change_by_input(self.camera_setting_page.set_range_check_z_max,"32.6", "z_max_default")
        
    def test_range_check_07_disable(self):
        """验证关闭范围检查并触发拍摄"""
        self.verify_setting_change_by_click(self.camera_setting_page.set_range_check_disable, "range_check_disable")





