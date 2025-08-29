import os
import unittest
from BeautifulReport import BeautifulReport
import time
from utils.driver_manager import get_driver_manager
import argparse



def run_all_tests(test_dir=None, test_pattern='test_*.py'):
    """运行测试用例

    Args:
        test_dir: 测试目录，如果为None则运行所有测试
        test_pattern: 测试文件匹配模式

    Returns:
        测试套件
    """
    # 设置默认测试目录
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests')

    if test_dir is None:
        # 运行所有测试
        test_suite = unittest.TestSuite()
        # 添加camera目录下的测试
        camera_dir = os.path.join(base_dir, 'camera')
        if os.path.exists(camera_dir):
            camera_suite = unittest.TestLoader().discover(start_dir=camera_dir, pattern=test_pattern)
            test_suite.addTest(camera_suite)
        # 添加menu目录下的测试
        menu_dir = os.path.join(base_dir, 'menu')
        if os.path.exists(menu_dir):
            menu_suite = unittest.TestLoader().discover(start_dir=menu_dir, pattern=test_pattern)
            test_suite.addTest(menu_suite)
        return test_suite
    else:
        # 运行指定目录下的测试
        full_test_dir = os.path.join(base_dir, test_dir)
        if not os.path.exists(full_test_dir):
            raise ValueError(f"测试目录不存在: {full_test_dir}")
        return unittest.TestLoader().discover(start_dir=full_test_dir, pattern=test_pattern)

# 通过修改 CONFIG 字典来控制测试执行：

# - 执行 camera 目录下的测试： 'test_dir': 'camera'
# - 执行 menu 目录下的测试： 'test_dir': 'menu'
# - 执行所有测试： 'test_dir': 'all'
# - 执行特定模式的测试文件：修改 'test_pattern' 的值，如 'test_menu_01_file.py'

# 配置区域 - 用户可以直接修改以下参数
CONFIG = {
    'test_dir': 'menu',  # 可选值: 'camera', 'menu', 'all'
    # 'test_pattern': 'test_settings_01_working_mode.py'
    'test_pattern': 'test_menu_03_display.py'  # 测试文件匹配模式 可选值test_*.py，'test_menu_01_file.py'

}


if __name__ == '__main__':
    os.environ['GLOBAL_SUITE_RUNNING'] = 'True'

    # 获取测试目录和模式 (从配置中读取)
    test_dir = CONFIG['test_dir'] if CONFIG['test_dir'] != 'all' else None
    test_pattern = CONFIG['test_pattern']

    # 运行测试套件
    test_suite = run_all_tests(test_dir=test_dir, test_pattern=test_pattern)

    # 生成报告
    report_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
    os.makedirs(report_dir, exist_ok=True)

    runner = BeautifulReport(test_suite)
    runner.report(
        description="SDK Tests Report",
        filename=f"Test_Report_{time.strftime('%Y_%m_%d_%H_%M_%S')}",
        report_dir=report_dir
    )

    # 关闭驱动
    get_driver_manager().quit_driver()
    del os.environ['GLOBAL_SUITE_RUNNING']