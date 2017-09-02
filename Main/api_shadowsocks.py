# -*- coding: utf-8 -*-
# @Author   : Sdite
# @DateTime : 2017-07-18 21:13:00
import re
import subprocess
import json
import requests
import tkinter.messagebox
import webbrowser
import time

class ShadowSocks(object):
    """docstring for ShadowSocks
    
    初始化函数的两个参数:
        ssPath, ssConfigPath分别代表可执行程序shadowsocks.exe的路径, gui-config.json的路径

    函数:
        setShadowSocks(self, pattern=JapanA_pattern)  # 可用help查看使用
        getHtml(self)                                 # 获取页面内容
        printItem(self, pattern=JapanA_pattern)       # 获取服务器内容
    """

    def __init__(self, ssPath, ssConfigPath):
        '''
        文档注释
        
        Args: 
            ssPath: 代表可执行程序shadowsocks.exe的路径
            ssConfigPath: 代表gui-config.json的路径
      
        '''
        super(ShadowSocks, self).__init__()
        self.ssPath = ssPath
        self.ssConfigPath = ssConfigPath
        self.getHtml()

    # 获取页面内容
    def getHtml(self):
        '''
        文档注释
        
        Args: 
            None
        
        Returns: 
            None: 无返回值
            self.content 保存页面内容
            若访问页面失败, 程序直接退出.
        '''
        res = requests.get(url=url, headers=headers)

        if res.status_code:
            res.encoding = 'utf-8'
            self.content = res.text
        else:
            print("error!")
            exit(0)

    # 获取服务器内容
    def printItem(self, pattern):
        '''
        文档注释
        
        Args: 
            pattern:所要爬取的服务器的模式.

            可选值有:
            * JapanA_pattern     # 日本服务器A
            * JapanB_pattern     # 日本服务器B
            * JapanC_pattern     # 日本服务器C
            * SingaporeA_pattern # 新加坡服务器A
            * SingaporeB_pattern # 新加坡服务器B
            * SingaporeC_pattern # 新加坡服务器C
            * UsaA_pattern       # 美国服务器A
            * UsaB_pattern       # 建议不使用
            * UsaC_pattern       # 建议不使用

        Returns: 
            None, 无返回
            打印出服务器,加密方式,密码,端口
        '''
        item = re.findall(pattern, self.content)[0]
        print('服务器  :', item[0])
        print('端口    :', item[1])
        print('密码    :', item[2])
        print('加密方式:', item[3])
        print('===================================')


    # 设置服务器
    def setShadowSocks(self, pattern):
        '''
        文档注释
        
        Args: 
            pattern:所要爬取的服务器的模式.

            可选值有:
            * JapanA_pattern     # 日本服务器A
            * JapanB_pattern     # 日本服务器B
            * JapanC_pattern     # 日本服务器C
            * SingaporeA_pattern # 新加坡服务器A
            * SingaporeB_pattern # 新加坡服务器B
            * SingaporeC_pattern # 新加坡服务器C
            * UsaA_pattern       # 美国服务器A
            * UsaB_pattern       # 建议不使用
            * UsaC_pattern       # 建议不使用

        Returns: 
            None, 无返回
        '''

        item = re.findall(pattern, self.content)[0]
        server = item[0]
        server_port = item[1]
        password = item[2]
        method = item[3]

        data = None
        with open(self.ssConfigPath, "r+") as f:
            data = json.load(f)
        data['configs'][0]['server'] = server
        data['configs'][0]['server_port'] = server_port
        data['configs'][0]['password'] = password
        data['configs'][0]['method'] = method
        with open(self.ssConfigPath, "w") as f:
            json.dump(data, f, indent=4)

        subprocess.call('taskkill /f /im shadowsocks.exe', stdout=subprocess.PIPE)
        subprocess.Popen(self.ssPath)


##################################################
##    基本变量
##################################################
url = 'http://ss.ishadowx.com/'           # 所要爬取服务器密码的网站
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

# 匹配日本服务器的模式
JapanA_pattern = re.compile(
    r'<span id="ipjpa">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwjpa">(.+?)</span>.+<h4>Method:(.+?)</h4>.+jpa.png', re.S)
JapanB_pattern = re.compile(
    r'<span id="ipjpb">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwjpb">(.+?)</span>.+<h4>Method:(.+?)</h4>.+jpb.png', re.S)
JapanC_pattern = re.compile(
    r'<span id="ipjpc">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwjpc">(.+?)</span>.+<h4>Method:(.+?)</h4>.+jpc.png', re.S)

# 匹配新加坡服务器的模式
SingaporeA_pattern = re.compile(
    r'<span id="ipsga">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwsga">(.+?)</span>.+<h4>Method:(.+?)</h4>.+sga.png', re.S)
SingaporeB_pattern = re.compile(
    r'<span id="ipsgb">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwsgb">(.+?)</span>.+<h4>Method:(.+?)</h4>.+sgb.png', re.S)
SingaporeC_pattern = re.compile(
    r'<span id="ipsgc">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwsgc">(.+?)</span>.+<h4>Method:(.+?)</h4>.+sgc.png', re.S)

# 匹配美国服务器的模式
UsaA_pattern = re.compile(
    r'<span id="ipusa">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwusa">(.+?)</span>.+<h4>Method:(.+?)</h4>.+usa.png', re.S)
UsaB_pattern = re.compile(
    r'<span id="ipusb">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwusb">(.+?)</span>.+<h4>Method:(.+?)</h4>.+usb.png', re.S)
UsaC_pattern = re.compile(
    r'<span id="ipusc">(.+?)</span>.+<h4>Port：(.+?)</h4>.+<span id="pwusc">(.+?)</span>.+<h4>Method:(.+?)</h4>.+usc.png', re.S)

if __name__ == '__main__':
    # 更改为你的ss程序路径
    ssPath = "E:\Shadowsocks\Shadowsocks.exe"

    # 更换为你的ss配置文件路径
    ssConfigPath = "E:\Shadowsocks\gui-config.json"

    a = ShadowSocks(ssPath, ssConfigPath)
    a.printItem(pattern=JapanA_pattern)
    a.printItem(pattern=JapanB_pattern)
    a.printItem(pattern=JapanC_pattern)
    a.printItem(pattern=SingaporeA_pattern)
    a.printItem(pattern=SingaporeB_pattern)
    a.printItem(pattern=SingaporeC_pattern)
    a.printItem(pattern=UsaA_pattern)
    a.printItem(pattern=UsaB_pattern)
    a.printItem(pattern=UsaC_pattern)
