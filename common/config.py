# coding: utf-8

import os
import sys
import json
import re


# 调用配置文件
def open_accordant_config():
    screen_size = _get_screen_size()
    config_file = "{path}/config/{screen_size}/config.json".format(
        path=sys.path[0],
        screen_size=screen_size
    )
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            print("Load config file from {}".format(config_file))
            return json.load(f)
    else:
        with open('{}/config/default.json'.format(sys.path[0]), 'r') as f:
            print("Load default config")
            return json.load(f)


# 获取手机屏幕大小
def _get_screen_size():
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
    else:  # 没获取到默认2K分辨率
        return "1920x1080"
