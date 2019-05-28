import os
from multiprocessing import Semaphore, Process
# 创建信号量对象
sem = Semaphore(4)
def fun():
    print("进程%d等待信号量"%os.getpid())
    # 消耗一个信号量
    sem.acquire()
    print("进程%d消耗信号量"%os.getpid())
    # 添加一个信号量
    sem.release()
    print("进程%d添加信号量"%os.getpid())

if __name__ == '__main__':
    jobs = []
    for i in range(4):
        p = Process(target=fun)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
    print(sem.get_value())