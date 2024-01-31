from time import sleep
import threading

# 创建一个互斥锁
mutex = threading.Lock()
NUM = 0


def task1(number):
    global NUM
    mutex.acquire()
    for i in range(number):
        NUM += 1
    mutex.release()
    print(f"in task1 NUM = {NUM}")


def task2(number):
    global NUM
    mutex.acquire()
    for i in range(number):
        NUM += 1
    mutex.release()
    print(f"in task2 NUM = {NUM}")


def main1():
    t1 = threading.Thread(target=task1, args=(1000000, ))
    t2 = threading.Thread(target=task2, args=(1000000, ))
    t1.start()
    t2.start()


class MY(threading.Thread):
    def run(self):
        while True:
            print(self.name)       # 查看当前线程的默认名字
            print("11111")
            sleep(1)


def main2():
    my = MY()
    my.daemon = True  # 设置为守护线程
    my.start()
    while True:
        print("main")
        sleep(1)
    

if __name__ == "__main__":
    main1()
