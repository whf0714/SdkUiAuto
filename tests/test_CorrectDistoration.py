import pyautogui as pg
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

server = 'http://127.0.0.1:4723'

desired_caps = {
    "app": r"D://s2714//02_Binary//01_SizectorS_ControlCenter//MPSizectorS_ControlCenter.exe",
    "deviceName": "WindowsPC",
    "platformName": "Windows",
    "appWorkingDir": "D://s2714//02_Binary//01_SizectorS_ControlCenter"
}

def openSDK(server, desired_caps):  # 打开viewer
    driver = webdriver.Remote(command_executor=server, desired_capabilities=desired_caps)
    return driver

def test_trigger_camera(driver):
    send_trigger_button_locator = (By.NAME, "发送软件触发")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(send_trigger_button_locator)).click()
    print("Camera trigger sent.")
    time.sleep(10)

"""
显示 x=120, y=11
发送软件触发 x=243, y=1355
文件 x=29, y=10 
启用专业设置 x=78, y=220
弹窗 启用专业设置x=1136, y=757
切到专业设置tab x=73, y=129
读取矫正参数x=109, y=519
矫正畸变x=296, y=523
"""
def Enble_ExpertSetting(driver):
    pg.moveTo(x=29, y=10)
    time.sleep(1)
    # clicks是点击次数  interval间隔时间 button=右键"right"，中键"middle"duration鼠标移动时间
    # pg.click(x=29, y=10, clicks=2, interval=1.0, button="middle", duration=1)
    pg.click(x=29, y=10)
    time.sleep(1)
    pg.click(x=78, y=220)
    time.sleep(1)
    pg.click(x=1136, y=757)
    time.sleep(1)
    pg.click(x=73, y=129)


if __name__ == "__main__":
    data_name = "7.mpdat"
    driver = openSDK(server, desired_caps)
    # openLocalData(data_name, driver)
    trigger_camera(driver)
    Enble_ExpertSetting(driver)
    driver.quit()