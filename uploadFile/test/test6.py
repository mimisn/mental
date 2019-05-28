import platform
import signal
from multiprocessing.managers import BaseManager
import time

def setTimeout(num, message):
    def decorator(func):
        # if platform.system() == 'Linux':
        def handle_linux(signum, frame):
            raise Exception(message)
        def wrapper(*args, **kwargs):
            #signal.signal(signal.SIGALRM, handle_linux)
            signal.alarm(num)
            rs = func(*args, **kwargs)
            signal.alarm(0)
            return rs
        return wrapper
    return decorator



@setTimeout(10,"xxxxx")
def xxx():
    print("dfadfdfsfasd")

#6s后终止程序
#signal.alarm(6)
#遇到SIGINT ctrl+c时，忽略SIG_IGN
#signal.signal(signal.SIGINT,signal.SIG_IGN)
#signal.pause()

if __name__ == '__main__':
    xxx()