# SDKUI 自动化测试项目

## 项目简介

SDKUI 自动化测试项目是一个基于 Appium 和 Selenium 的 Windows 应用程序自动化测试框架，用于测试 SDK UI 界面的各项功能。

## 项目结构

```
SdkUiAuto/
├── config/             # 配置文件目录
│   └── config.py       # 项目配置
├── data/               # 测试数据目录
│   └── read/           # 读取数据目录
├── pages/              # 页面对象目录
│   ├── menu_page.py    # 菜单页面操作
│   └── camera_setting_page.py # 相机设置页面操作
├── reports/            # 测试报告目录
├── screenshots/        # 截图目录
├── tests/              # 测试用例目录
│   ├── camera/         # 相机设置测试
│   └── menu/           # 菜单操作测试
├── utils/              # 工具目录
│   ├── driver.py       # 驱动配置
│   └── driver_manager.py # 驱动管理
├── README.md           # 项目说明
├── requirements.txt    # 依赖包
└── runner.py           # 运行入口
```

## 安装步骤

### 1. 启动 WinAppDriver 服务

在运行自动化测试之前，需要启动 WinAppDriver 服务：

1. 下载并安装 WinAppDriver
2. 以管理员身份运行 WinAppDriver.exe
3. 确认服务启动成功（默认监听 127.0.0.1:4723）

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 SDK 路径

修改 `utils/driver.py` 文件中的 SDK 路径配置：

```python
# 修改为实际的 SDK 路径
app_path = "C:\\Path\\To\\Your\\SDK.exe"
```

### 4. 配置文件导航路径

修改 `config/config.py` 文件中的文件导航路径：

```python
# 文件保存对话框的导航路径
NAVIGATION_PATHS = {
    'd_drive': '新加卷 (D:)',
    'program': 'Program',
    'python': 'Python',
    'public': 'public',
    'sdkui': 'SdkUiAuto',
    'data': 'data',
    'read': 'read',
    'save': 'save'
}
```
### 5. 修改按钮坐标
修改 `config/config.py` 文件中的设备状态按钮坐标配置：

```python
# 设备状态按钮相关常量
DEVICE_STATUS_BUTTON_X = 113  # 修改为实际获取的 x 坐标
DEVICE_STATUS_BUTTON_Y = 1384  # 修改为实际获取的 y 坐标
DEVICE_STATUS_COLOR_HOLD = (176, 28, 58)  # 暂停状态颜色 (红色)
DEVICE_STATUS_COLOR_RUN = (77, 133, 72)   # 运行状态颜色 (绿色)
```
如果需要获取当前电脑上"点击运行"按钮的准确坐标，可以使用以下方法：

```python
import pyautogui
import time

print("将鼠标移动到'点击运行'按钮上，3秒后获取坐标...")
time.sleep(3)
x, y = pyautogui.position()
print(f"按钮坐标: x={x}, y={y}")

## 运行测试

### 1. 编辑运行配置

在 `runner.py` 文件中编辑需要运行的测试用例：

```python
CONFIG = {
    'test_dir': 'menu',  # 可选值: 'menu', 'camera'
    'test_pattern': 'test_*.py'  # 测试文件匹配模式
}
```

### 2. 执行测试

运行 `runner.py` 文件执行测试：


### 3. 查看测试报告

测试执行完成后，会在 `reports` 目录生成 HTML 格式的测试报告。




