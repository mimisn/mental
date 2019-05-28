from multiprocessing import Process,JoinableQueue
import os
import time
import random
#首先得有生产者和消费者
# 消费者吃包子
def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print('\033[41m%s吃了%s\033[0m' % (os.getpid(),res))
        q.task_done() #任务结束了（消费者告诉生产者，我已经吧东西取走了）
def product_baozi(q):
    for i in range(5):
        time.sleep(2)
        res = '包子%s' % i
        q.put(res)
        print('\033[44m%s制造了%s\033[0m' % (os.getpid(), res))
    q.join() #不用put(None) 了，在等q被取完。（如果数据没有被取完，生产者就不会结束掉）
def product_gutou(q):
    for i in range(5):
        time.sleep(2)
        res = '骨头%s' % i
        q.put(res)
        print('\033[44m%s制造了%s\033[0m' % (os.getpid(), res))
    q.join()
def product_doujiang(q):
    for i in range(5):
        time.sleep(2)
        res = '豆浆%s' % i
        q.put(res)
        print('\033[44m%s制造了%s\033[0m' % (os.getpid(), res))
    q.join()

if __name__ == '__main__':
    q = JoinableQueue()
    # 生产者们：厨师们
    p1 = Process(target=product_baozi,args=(q,))
    p2 = Process(target=product_doujiang,args=(q,))
    p3 = Process(target=product_gutou,args=(q,))

    #消费者们：吃货们
    p4 = Process(target=consumer,args=(q,))
    p5 = Process(target=consumer,args=(q,))
    p4.daemon = True
    p5.daemon = True
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    li = [p1,p2,p3,p4,p5]
    for i in li:
        i.start()
    p1.join()
    p2.join()
    p3.join()
    print('主')
