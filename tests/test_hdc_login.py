import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# 配置信息
# server_url = 'http://127.0.0.1:4723'
# app_path = r"D:\MegaPhase\SoftWare\SDK\MPSizectorS_SDK_V2_758_Win_Blue\02_Binary\01_SizectorS_ControlCenter\MPSizectorS_ControlCenter.exe"
# app_working_dir = r"D:\MegaPhase\SoftWare\SDK\MPSizectorS_SDK_V2_758_Win_Blue\02_Binary\01_SizectorS_ControlCenter"

server_url = 'http://127.0.0.1:4723'
app_path = r"D:\MegaPhase\SoftWare\HDC_SDK\hdc242\MPHdc SDK V2.42\02_Binary\01_MPHdc_ControlCenter\MPHdc_ControlCenter.exe"
app_working_dir = r"D:\MegaPhase\SoftWare\HDC_SDK\hdc242\MPHdc SDK V2.42\02_Binary\01_MPHdc_ControlCenter"

def start_driver():
    desired_caps = {
        'app': app_path,
        "deviceName": "WindowsPC",
        'platformName': 'Windows',
        'appWorkingDir': app_working_dir
    }
    driver = webdriver.Remote(server_url, desired_caps)
    return driver



class TestWorkingMode():

    def click_element(self, driver, locator):

            """
            :param driver: WebDriver实例
            :param locator: 元素定位器
            """
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

    def force_click_element(self, driver, locator):
        """
        使用ActionChains强制点击元素，适用于Windows桌面应用
        :param driver: WebDriver实例
        :param locator: 元素定位器
        :return: 无
        """
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            ActionChains(driver).move_to_element(element).click().perform()
            print(f"已使用ActionChains强制点击元素: {locator}")
        except Exception as e:
            print(f"使用ActionChains强制点击元素时发生错误: {e}")
            raise

    def test_click_working_mode_mono2d(self):
        driver = start_driver()
        # page_source = driver.page_source
        # print(page_source)
        try:
            time.sleep(2)
            hold_locator = (By.NAME, "暂停")
            self.click_element(driver, hold_locator)
            Color2D_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeColor2DRbt")
            self.click_element(driver, Color2D_locator)
            trigger_locator = (By.NAME, "发送软件触发")
            self.click_element(driver, trigger_locator)
            time.sleep(2)
            Color2D_locator = (MobileBy.ACCESSIBILITY_ID, "WorkingModeDefRbt")
            self.click_element(driver, Color2D_locator)
            trigger_locator = (By.NAME, "发送软件触发")
            self.click_element(driver, trigger_locator)

            # file_locator = (By.NAME, "文件")
            # self.click_element(driver, file_locator)
            # time.sleep(2)
            #
            # load_data_locator = (By.NAME, "保存数据")
            # self.force_click_element(driver, load_data_locator)
            # time.sleep(2)

        finally:
            driver.quit()
