from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import start_driver
import time
import os

class BasePage:
    def __init__(self):
        self.driver = start_driver()

    def openSDK(server, desired_caps):  # 打开viewer
        driver = webdriver.Remote(command_executor=server, desired_capabilities=desired_caps)
        time.sleep(1)
        return driver

    def LoadData(self, data_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "文件"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "导入数据"))).click()
        print(f"Trying to open data: {data_name}")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "Data (D:)"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "mpdat"))).click()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "打开(O)"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "softwarePreprocess"))).click()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "打开(O)"))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, data_name))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "打开(O)"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "确定"))).click()


    def quit(self):
        self.driver.quit()
