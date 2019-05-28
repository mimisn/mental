import threading
import time
import multiprocessing


def fun(args):
    for i in range(5):
        print('myname is : %s \n' %(args))
        time.sleep(1)

def aaa():
    for i in range(4):
        t = multiprocessing.Process(target=fun, args=("name %s" % (i),))
        t.start()
    return "wo pao le"


if __name__ == '__main__':

    print(aaa())
