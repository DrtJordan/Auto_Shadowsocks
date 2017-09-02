from api_shadowsocks import *

# 更改为你的ss程序路径
ssPath = "..\Shadowsocks\Shadowsocks.exe"  # 当前是相对路径

# 更换为你的ss配置文件路径
ssConfigPath = "..\Shadowsocks\gui-config.json" # 当前是相对路径

if __name__ == '__main__':
    shadowsocks = ShadowSocks(ssPath=ssPath, ssConfigPath=ssConfigPath)
    shadowsocks.setShadowSocks(pattern=JapanA_pattern)

    # setShadowSocks可选服务器
    # 
    # pattern:所要爬取的服务器的模式.
    # 可选值有(定义在api中):
    # * JapanA_pattern     # 日本服务器A
    # * JapanB_pattern     # 日本服务器B
    # * JapanC_pattern     # 日本服务器C
    # * SingaporeA_pattern # 新加坡服务器A
    # * SingaporeB_pattern # 新加坡服务器B
    # * SingaporeC_pattern # 新加坡服务器C
    # * UsaA_pattern       # 美国服务器A
    # * UsaB_pattern       # 建议不使用
    # * UsaC_pattern       # 建议不使用