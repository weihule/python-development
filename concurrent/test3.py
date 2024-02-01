from time import sleep
import os
from multiprocessing import Pool, Manager

def reader(q):
    print(f"reader start {os.getpid()} parent pid = {os.getppid()}")
    for _ in range(q.qsize()):
        print(f"The reader obtains a message from the queue {q.get()}")


def writer(q):
    print(f"writer start {os.getpid()} parent pid = {os.getppid()}")
    for i in "itcast":
        q.put(i)


if __name__ == "__main__":
    print(f"{os.getpid()} Start")
    q = Manager().Queue()       # 使用Manger中的Queue
    po = Pool()
    po.apply_async(writer, args=(q, ))

    # 先让上面的任务向Queue中存入数据
    sleep(1)

    po.apply_async(reader, args=(q, ))
    po.close()
    po.join()
    print(f"{os.getpid()} End")

