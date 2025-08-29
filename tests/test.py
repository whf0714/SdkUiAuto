
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

server = 'http://127.0.0.1:4723'

desired_caps = {
    "app": r"D://MPsdk//s2753//2753//02_Binary//01_SizectorS_ControlCenter//MPSizectorS_ControlCenter.exe",
    "deviceName": "WindowsPC",
    "platformName": "Windows",
    "appWorkingDir": "D://MPsdk//s2753//2753//02_Binary//01_SizectorS_ControlCenter"
}

def openSDK(server, desired_caps):
    driver = webdriver.Remote(command_executor=server, desired_capabilities=desired_caps)
    return driver

def openLocalData(dataName, driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "文件"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "导入数据"))).click()
    print(f"Trying to open data: {dataName}")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Data (D:)"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "mpdat"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "打开(O)"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "softwarePreprocess"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "打开(O)"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, dataName))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "打开(O)"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "确定"))).click()

def trigger_camera(driver):
    send_trigger_button_locator = (By.NAME, "发送软件触发")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(send_trigger_button_locator)).click()
    print("Camera trigger sent.")
    time.sleep(10)

if __name__ == "__main__":
    data_name = "7.mpdat"
    driver = openSDK(server, desired_caps)
    openLocalData(data_name, driver)
    # trigger_camera(driver)
    driver.quit()




