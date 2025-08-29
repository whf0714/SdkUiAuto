from appium import webdriver
from utils.driver import server_url, app_path, app_working_dir
import time

class DriverManager:
    _instance = None
    _driver = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_driver(self):
        if self._driver is None:
            # 创建新的驱动实例
            desired_caps = {
                'app': app_path,
                "deviceName": "WindowsPC",
                'platformName': 'Windows',
                'appWorkingDir': app_working_dir
            }
            self._driver = webdriver.Remote(server_url, desired_caps)
            time.sleep(1)  # 等待应用启动
        return self._driver

    def quit_driver(self):
        if self._driver is not None:
            self._driver.quit()
            self._driver = None

# 创建全局驱动管理器实例
_driver_manager = DriverManager()

def get_driver_manager():
    """获取全局驱动管理器实例"""
    return _driver_manager