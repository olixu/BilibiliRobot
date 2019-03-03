# B 站直播弹幕姬 Python 版

Python 抓取 B 站直播弹幕。另外我还写了 [Go 版的直播弹幕](https://github.com/lyyyuna/gobilibili)。

## 简单说明

B 站弹幕协议是会变的，目前至少改过一次。故不能保证向后兼容性。

### 依赖

* Python 3.5
* pip3 install aiohttp

### 快速开始

在 config.py 中配置是否显示礼物、欢迎信息。

在命令行中，

    python3 main.py
    
根据提示输入房间号即可。

### 思路简单介绍

[B站弹幕协议简析](http://www.lyyyuna.com/2016/03/14/bilibili-danmu01/)

## 以此为基础做的弹幕收集系统

[Top 100 UP主的24小时弹幕收集器](https://github.com/lyyyuna/bilibili_danmu_colloector)
