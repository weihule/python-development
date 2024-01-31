from time import sleep
from multiprocessing import Process
    

def test():
    while True:
        print("----test----")
        sleep(1)

if __name__ == "__main__":
    p = Process(target=test)
    p.start()

    # 主进程执行的代码
    while True:
        print("----main----")
        sleep(1)
