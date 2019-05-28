import socket
from multiprocessing import Process, Lock, Queue
import os
import time
from multiprocessing import JoinableQueue

import json


def jsontest(request):
    data = {
        "result": "success",
        "data": [
            {'time': '00:11:12', 'hero': '幻影刺客', 'action': '击杀', 'target': '斧王', 'desc': '幻影刺客击杀了斧王。'},
            {'time': '00:13:22', 'hero': '幻影刺客', 'action': '购买了', 'target': '隐刀', 'desc': '幻影刺客购买了隐刀。'},
            {'time': '00:19:36', 'hero': '斧王', 'action': '购买了', 'target': '黑皇杖', 'desc': '斧王购买了黑皇杖。'},
            {'time': '00:21:43', 'hero': '力丸', 'action': '购买了', 'target': '隐刀', 'desc': '力丸购买了隐刀。'}
        ],
        "message": "",
        "pager": {
            "page": 1,
            "recTotal": 1001,
            "recPerPage": 10,
        }
    }
    requestdata = json.dumps(data).encode("utf-8")
    print(requestdata)
    request.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
    request.sendall(requestdata)
    return True


class dingshi(Process):
    def __init__(self,queue,mutex):
        Process.__init__(self)
        self.queue = queue
        self.mutex = mutex

    def run(self):
        while True:
            try:
                cnn, addr = self.queue.get()
                request = cnn.recv(1024)
                print(request)
                #cnn.sendall(b'HTTP/1.1 200 OK\r\n\r\n<html><body>hello</body></html>')
                jsontest(cnn)
                cnn.close()
                print('\x1B[40m%s 处理 %s %s\x1B[0m' % (os.getpid(), addr, os.getppid()))
            except Exception as e:
                print("\x1B[38m%s  %s\x1B[0m"%(os.getpid(),e))


def work(queue, mutex):
    while True:
        print('\x1B[41m%s ok\x1B[0m' % (os.getpid()))
        cnn,addr = queue.get()
        request = cnn.recv(1024)
        print(request)
        cnn.sendall(b'HTTP/1.1 200 OK\r\n\r\n<html><body>hello')
        cnn.sendall(b'hellodfasffafasfadsfasfasd</body></html>')
        cnn.close()
        print('\x1B[41m%s 处理 %s %s\x1B[0m'%(os.getpid(), addr, os.getppid()))

def socketAccept(queue,mutex):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 4444))
    s.listen(10000)
    while True:
        queue.put(s.accept())
if __name__ == '__main__':
    queue = Queue()
    mutex = Lock()
    p1 = Process(target=work, args=(queue, mutex), name='work')
    p2 = Process(target=work, args=(queue, mutex), name='work')
    p3 = Process(target=work, args=(queue, mutex), name='work')
    p4 = Process(target=socketAccept, args=(queue, mutex), name='socket')
    p5 = dingshi(queue, mutex)
    p5.daemon = True
    p5.start()


    p1.daemon = True
    p2.daemon = True
    p3.daemon = True
    p4.daemon = True
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p4.join()