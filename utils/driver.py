from appium import webdriver

server_url = 'http://127.0.0.1:4723'
# app_path = r"D:/s2714/02_Binary/01_SizectorS_ControlCenter/MPSizectorS_ControlCenter.exe"
# app_path = r"D:\MPsdk\s2753\2753\02_Binary\01_SizectorS_ControlCenter\MPSizectorS_ControlCenter.exe"
app_path = r"D:\MegaPhase\SoftWare\SDK\sdk582\582\02_Binary\01_SizectorS_ControlCenter\MPSizectorS_ControlCenter.exe"

# app_working_dir = r"D:/s2714/02_Binary/01_SizectorS_ControlCenter"
# app_working_dir = r"D:\MPsdk\s2753\2753\02_Binary\01_SizectorS_ControlCenter"
app_working_dir = r"D:\MegaPhase\SoftWare\SDK\sdk582\582\02_Binary\01_SizectorS_ControlCenter"




def start_driver():
    desired_caps = {
        'app': app_path,
        "deviceName": "WindowsPC",
        'platformName': 'Windows',
        'appWorkingDir': app_working_dir
    }
    driver = webdriver.Remote(server_url, desired_caps)
    return driver
