import pyautogui as pg
import time

#
# #获取鼠标初始当前位置
# x, y = pg.position()
# # pg.moveTo(x=1000, y=300)
# while True:
#     #接收鼠标变动位置
#     x1, y1 = pg.position()
#     #如果初始位置和变动位置不一样
#     if x1 != x or y1 != y:
#         x, y = x1, y1
#         print(x1,y1)
"""
暂停  x=60, y=1346
显示 x=120, y=11
发送软件触发 x=243, y=1355
文件 x=29, y=10 
启用专业设置 x=78, y=220
弹窗 启用专业设置x=1136, y=757
切到专业设置tab x=73, y=129
读取矫正参数x=109, y=519
矫正畸变x=296, y=523
数据导入成功 x=1094, y=686 确定按钮x=1136, y=753
"""
"""
pg.moveTo(x=109, y=1151)


time.sleep(1)
#clicks是点击次数  interval间隔时间 button=右键"right"，中键"middle"duration鼠标移动时间
pg.click(x=109, y=1151, clicks=2, interval=1.0, button="middle", duration=1)
#鼠标移动 x正数向右，Y正数向下
pg.move(xOffset=-100, yOffset=-200)
#鼠标按住
pg.mouseDown(x=109, y=1151)
time.sleep(1)
#鼠标抬起
pg.mouseUp(x=109, y=1151)


"""
"""
#鼠标滑轮滚动 正数往上滑，负数往下滑 1000的值大概滑动8次
pg.click(x=2188, y=363)
time.sleep(1)
pg.scroll(-100)
"""
"""
#键盘输入 不支持中文 需要切换输入法
pg.click(x=2188, y=363)
time.sleep(1)
pg.write('123axc')
"""
"""
点击暂停（绿色）  x=99, y=1312   颜色: (77, 133, 72)
点击运行（红色）  x=99, y=1312   颜色: (176, 28, 58)
显示 x=120, y=11
发送软件触发 x=243, y=1355
文件 x=29, y=10 
启用专业设置 x=78, y=220
弹窗 启用专业设置x=1136, y=757
切到专业设置tab x=73, y=129
读取矫正参数x=109, y=519
矫正畸变x=296, y=523
数据导入成功 x=1094, y=686 确定按钮x=1136, y=753
"""
"""
快速 x=98, y=226   
标准 x=192, y=226   
精准 x=294, y=226  
超准 x=98, y=252
白照明 x=98, y=279   
无照明 x=194, y=279   
网格投影 x=294, y=279     
曝光强度预测  x=98, y=307    
实时后处理 x=74, y=248   
StandBy（绿色）  x=99, y=1387   颜色:(77, 133, 72)
UnderExposure/UnderTransfer（棕色）  x=99, y=1312   颜色:(194, 153, 108)
"""
"""
#截取屏幕图像
#安装第三方依赖库：pillow
import pyautogui as pg

#第一个参数传保存位置 绝对路径/相对路径，相对路径保存在项目下
#第二个参数 截图范围（起始X，起始y，终止X，终止y）
pg.screenshot(imageFilename='../screenshots/1.png', region=(1, 1, 1000, 100))

"""

# # 消息框 暂停的作用
# # 第一个参数传内容，第二个参数传标题，第三个参数传按钮
# pg.click(x=969, y=117)
# print('1')
# pg.alert('内容', '标题', '按钮')
# print('2')
# # # 输入框
# a1 = pg.prompt('内容', '标题', '默认输入值')
# print(a1)

# 初始化鼠标位置
x, y = pg.position()
while True:
    # 接收鼠标变动位置0
    x1, y1 = pg.position()
    # 如果初始位置和变动位置不一样
    if x1 != x or y1 != y:
        x, y = x1, y1
        # 获取当前鼠标位置的颜色
        pixel_color = pg.pixel(x, y)
        print(f"鼠标当前坐标: {x1}, {y1}, 颜色: {pixel_color}")
    time.sleep(0.1)  # 减少CPU占用，设置适当的刷新频率

# import itertools
#
#
# def generate_combinations():
#     numbers = [0, 1, 2, 3]
#     all_combinations = []
#
#     # 生成从长度 1 到长度 len(numbers) 的所有组合
#     for r in range(1, len(numbers) + 1):
#         combinations = list(itertools.combinations(numbers, r))
#         all_combinations.extend(combinations)
#
#     return all_combinations


# if __name__ == "__main__":
#     combinations = generate_combinations()
#     for combo in combinations:
#         print(combo)
import re

# 示例文本
# text = """
# 预处理
#  对齐1
#
# 特征
#  平面1
#  点1
# 测量
#  点到平面1
#  0.032126
#   mm
#  通过
# """

# # 使用正则表达式提取数值
# pattern = r'\d+\.\d+'  # 匹配浮点数
# matches = re.findall(pattern, text)
#
# # 输出提取的数值
# if matches:
#     print("提取的数值:", matches)  # 输出第一个匹配的数值
# else:
#     print("未找到数值")