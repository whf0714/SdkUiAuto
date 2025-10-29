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
UI_DATA_PATH = '/\\data'
UI_READ_DATA_PATH = '/\\data\\read'
UI_SAVE_DATA_PATH = '/\\data\\save'
UI_SCREENSHOTS_PATH = '/\\screenshots'

# UI_DATA_PATH = 'D:\\Program\\Python\\SdkUiAuto\\data'
# UI_READ_DATA_PATH = 'D:\\Program\\Python\\SdkUiAuto\\data\\read'
# UI_SAVE_DATA_PATH = 'D:\\Program\\Python\\SdkUiAuto\\data\\save'
# UI_SCREENSHOTS_PATH = 'D:\\Program\\Python\\SdkUiAuto\\screenshots'

# 文件保存对话框的导航路径
NAVIGATION_PATHS = {
    'd_drive': '新加卷 (D:)',
    'program': 'Program',
    'python': 'Python',
    'sdkui': 'SdkUiAuto',
    'data': 'data',
    'read': 'read',
    'save': 'save'
}