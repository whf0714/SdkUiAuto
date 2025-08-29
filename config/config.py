import os

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据目录路径
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
READ_DATA_DIR = os.path.join(DATA_DIR, 'read')
SAVE_DATA_DIR = os.path.join(DATA_DIR, 'save')

# 截图目录路径
SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, 'screenshots')

# 文件保存对话框中使用的路径（用于UI操作）
UI_DATA_PATH = 'D:\\Program\\Python\\SdkUi - ai\\data'
UI_READ_DATA_PATH = 'D:\\Program\\Python\\SdkUi - ai\\data\\read'
UI_SAVE_DATA_PATH = 'D:\\Program\\Python\\SdkUi - ai\\data\\save'
UI_SCREENSHOTS_PATH = 'D:\\Program\\Python\\SdkUi - ai\\screenshots'

# 文件保存对话框的导航路径
NAVIGATION_PATHS = {
    'd_drive': '新加卷 (D:)',
    'program': 'Program',
    'python': 'Python',
    'sdkui': 'SdkUi - ai',
    'data': 'data',
    'read': 'read',
    'save': 'save'
}