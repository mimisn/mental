import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mental.settings")

import django
django.setup()

from django.conf import settings
import socket
from multiprocessing import Process, Lock, Queue
import time
from multiprocessing import JoinableQueue




class SocketMonitorProcess(Process):
    def __init__(self, queue, mutex):
        Process.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.daemon = True

    def run(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind(('0.0.0.0', 4444))
        sk.listen(10000)
        while True:
            self.queue.put(sk.accept())

'''
# 处理文件上传任务
# 处理部署任务
# 处理发布任务
# 处理批量任务
{   
    "taskNumber":12313123123232,
    "target":"UploadClass",
    "result": "success",
    "data":{
            fileName:
            fileDestPath
            fileSize
            fileMd5
            fileSourcePath
    }
}


'''
class SocketHandleProcess(Process):
    def __init__(self, queue, mutex):
        Process.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.daemon = True
    def run(self):
        while True:
            try:
                cnn, addr = self.queue.get()
                request = cnn.recv(1024)
                cnn.sendall(b'HTTP/1.1 200 OK\r\n\r\n<html><body>hello</body></html>')
                cnn.close()
                print('\x1B[40m%s 处理 %s %s' % (os.getpid(), addr, os.getppid()))
            except Exception as e:
                print(e)
'''
# 处理定时任务
# 处理计划任务
# 处理备份任务
# 处理一切和时间有关的任务
'''
class TimerHandleProcess(Process):
    def __init__(self):
        pass

class RunMain():
    socketQueue = Queue()
    timeQueue = JoinableQueue()
    handleQueue = Queue()
    def __init__(self):
        pass