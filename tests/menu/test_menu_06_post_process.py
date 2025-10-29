import unittest
import time
from pages.menu_page import MenuPage
from tests.menu.test_menu_public import TestPublicMenu
from datetime import datetime
now = datetime.now().strftime("%Y%m%d%H%M%S")

class TestPostProcess(TestPublicMenu):

    # def setUp(self):
    #     """前置条件：导入数据并进入实时后处理设置窗口"""
    #     data_name = "3dMpdat3.mpdat"
    #     self.menu_page.load_data(data_name)
    #     self.menu_page.post_process()

    def test_post_process_01_enable(self):
        """验证勾选启用实时软后处理"""
        data_name = "3dMpdat3.mpdat"
        load_action = lambda: self.menu_page.load_data(data_name)
        self.verify_text_prompt(load_action, "数据导入成功", "load_data")
        self.menu_page.switch_post_process() #前置条件
        self.menu_page.set_post_process_enable()

    def test_post_process_02_disable(self):
        """验证取消勾选启用实时软后处理"""
        self.menu_page.set_post_process_disable()

    def test_post_process_03_gpu_computation_enable(self):
        """验证勾选启用GPU运算"""
        self.menu_page.set_gpu_computation_enable()

    def test_post_process_04_gpu_computation_disable(self):
        """验证取消勾选启用GPU运算"""
        self.menu_page.set_gpu_computation_disable()

    def test_post_process_05_global_buffer_enable(self):
        """验证勾选使用全局缓存"""
        self.menu_page.set_global_buffer_enable()

    def test_post_process_06_global_buffer_disable(self):
        """验证取消勾选使用全局缓存"""
        self.menu_page.set_global_buffer_disable()

    def test_post_process_07_range_check_center_x(self):
        """验证修改后处理_范围检查参数设置_中心X"""
        self.menu_page.set_range_check_center_x("100")

    def test_post_process_08_range_check_center_y(self):
        """验证修改后处理_范围检查参数设置_中心Y"""
        self.menu_page.set_range_check_center_y("100")

    def test_post_process_09_range_check_inner_radius(self):
        """验证修改后处理_范围检查参数设置_内半径"""
        self.menu_page.set_range_check_inner_radius("50")

    def test_post_process_10_range_check_outer_radius(self):
        """验证修改后处理_范围检查参数设置_外半径"""
        self.menu_page.set_range_check_outer_radius("100")

    def test_post_process_11_range_check_x_min(self):
        """验证修改后处理_范围检查参数设置_X最小"""
        self.menu_page.set_range_check_x_min("-100")

    def test_post_process_12_range_check_x_max(self):
        """验证修改后处理_范围检查参数设置_X最大"""
        self.menu_page.set_range_check_x_max("100")

    def test_post_process_13_range_check_y_min(self):
        """验证修改后处理_范围检查参数设置_Y最小"""
        self.menu_page.set_range_check_y_min("-50")

    def test_post_process_14_range_check_y_max(self):
        """验证修改后处理_范围检查参数设置_Y最大"""
        self.menu_page.set_range_check_y_max("50")

    def test_post_process_15_range_check_z_min(self):
        """验证修改后处理_范围检查参数设置_Z最小"""
        self.menu_page.set_range_check_z_min("10")

    def test_post_process_16_range_check_z_max(self):
        """验证修改后处理_范围检查参数设置_Z最大"""
        self.menu_page.set_range_check_z_max("10")

    def test_post_process_17_add_range_check(self):
        """验证勾选后处理_范围检查"""
        self.menu_page.add_range_check()
        
    def test_post_process_18_remove_burrs_win_size(self):
        """验证修改后处理_去飞点参数设置_窗口尺寸"""
        self.menu_page.set_remove_burrs_win_size("10")
        
    def test_post_process_19_remove_burrs_win_size2(self):
        """验证修改后处理_去飞点参数设置_次窗口"""
        self.menu_page.set_remove_burrs_win_size2("5")
        
    def test_post_process_20_remove_burrs_slope_level(self):
        """验证修改后处理_去飞点参数设置_斜率"""
        self.menu_page.set_remove_burrs_slope_level("60")
        
    def test_post_process_21_remove_burrs_neighbor_close_level(self):
        """验证修改后处理_去飞点参数设置_邻近阈值"""
        self.menu_page.set_remove_burrs_neighbor_close_level("60")
        
    def test_post_process_22_remove_burrs_neighbor_num_level(self):
        """验证修改后处理_去飞点参数设置_邻近数量"""
        self.menu_page.set_remove_burrs_neighbor_num_level("60")
        
    def test_post_process_23_remove_burrs_edge_suppress_level(self):
        """验证修改后处理_去飞点参数设置_抑制窄边"""
        self.menu_page.set_remove_burrs_edge_suppress_level("60")
        
    def test_post_process_24_add_remove_burrs(self):
        """验证勾选后处理_去飞点"""
        self.menu_page.add_remove_burrs()
        
    def test_post_process_25_mend_win_size(self):
        """验证修改后处理_填补参数设置_窗口尺寸"""
        self.menu_page.set_mend_win_size("30")
        
    def test_post_process_26_mend_win_size2(self):
        """验证修改后处理_填补参数设置_次窗口尺寸"""
        self.menu_page.set_mend_win_size2("10")
        
    def test_post_process_27_mend_method(self):
        """验证修改后处理_填补参数设置_填补_方法_膨胀法"""
        # 0: 膨胀法、1：插值法、膨胀的相关设置参数（主窗口尺寸、次窗口尺寸）
        self.menu_page.set_mend_method("0")
        
    def test_post_process_28_add_mend(self):
        """验证勾选后处理_填补"""
        self.menu_page.add_mend()

    def test_post_process_29_filtrate_win_size(self):
        """验证修改后处理_平滑参数设置_窗口尺寸"""
        self.menu_page.scroll_down()  # 滚动条下滑
        self.menu_page.set_filtrate_win_size("30")

    def test_post_process_30_filtrate_neighbor_close_level(self):
        """验证修改后处理_平滑参数设置_邻近阈值"""
        self.menu_page.set_filtrate_neighbor_close_level("1")

    def test_post_process_31_filtrate_neighbor_num_level(self):
        """验证修改后处理_平滑参数设置_邻近数量"""
        self.menu_page.set_filtrate_neighbor_num_level("1")
           
    def test_post_process_32_add_filtrate(self):
        """验证添加后处理_平滑"""
        self.menu_page.add_filtrate()
        
    def test_post_process_33_select_first_item(self):
        """验证选择后处理列表第一项"""
        self.menu_page.post_process_list()

    def test_post_process_34_move_down(self):
        """验证点击'下移' 按钮"""
        self.menu_page.post_process_move_down()

    def test_post_process_35_move_up(self):
        """验证点击'上移' 按钮"""
        self.menu_page.post_process_move_up()

    def test_post_process_36_delete(self):
        """验证点击'删除当前选中项’ 按钮"""
        self.menu_page.post_process_delete()

    def test_post_process_37_clear(self):
        """验证点击'清空' 按钮"""
        self.menu_page.post_process_clear()
        time.sleep(2)

    def test_post_process_38_load_setting(self):
        """验证点击'加载后处理设置'按钮"""
        setting_name = "MPPostProcessSettings.mppp"
        load_action = lambda: self.menu_page.post_process_load_setting(setting_name)
        self.verify_text_prompt(load_action, "实时后处理设置导入成功", "post_process_load_setting")

    def test_post_process_39_save_setting(self):
        """验证点击'保存后处理设置'按钮"""
        setting_name = "MPPostProcessSettings_"+now+".mppp"
        file_action = lambda: self.menu_page.post_process_save_setting(setting_name)
        self.verify_text_prompt(file_action, "实时后处理设置导出成功", "post_process_save_setting")

    def test_post_process_40_confirm(self):
        """验证启用实时后处理及GPU运算并点击'应用'按钮"""
        self.menu_page.set_post_process_enable()
        self.menu_page.set_gpu_computation_enable()
        self.menu_page.post_process_confirm()
        

        

