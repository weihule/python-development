from time import sleep
import threading


NUM = 0


def task1():
    global NUM
    NUM = 10
    print(f"in task1 NUM = {NUM}")


def task2():
    print(f"in task2 NUM = {NUM}")


def main1():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    sleep(2)
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
