from multiprocessing import Event,Process
from time import sleep

def wait_event1(e):
    print("1想操作临界区资源")
    e.wait()
    print("1开始操作临界区资源",e.is_set())
    with open("file") as f:
        print(f.read())
def wait_event2(e):
    print("2也想操作临界区资源")
    # 超时3秒检测
    e.wait(1)
    # 判断是否被设置
    if e.is_set():
        print("2开始操作临界区资源",e.is_set())
        with open("file") as f:
            print(f.read())
    else:
        print("2不能操作")




if __name__ == '__main__':
    # 创建事件对象
    e = Event()
    p1 = Process(target=wait_event1, args=(e,))
    p2 = Process(target=wait_event2, args=(e,))
    p1.start()
    p2.start()
    print("主进程操作")
    with open("file", 'w') as f:
        f.write("HELLO WORD")

    # 延迟4秒释放临界区
    sleep(4)
    # 释放临界区资源
    e.set()
    print("释放临界区")
    p1.join()
    p2.join()