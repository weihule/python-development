from time import sleep
from multiprocessing import Process, Queue


def task1(q: Queue):
    for v in ["A", "B", "C"]:
        q.put(v)
        print(f"Put {v} to queue")
        sleep(1)
    # 放入特殊标志表示队列结束
    q.put("END_OF_QUEUE")


def task2(q: Queue):
    while True:
        v = q.get()
        if v == "END_OF_QUEUE":
            break  # 遇到特殊标志时退出循环
        print(f"Get {v} from queue")
        sleep(1)


if __name__ == "__main__":
    q = Queue()    # 初始化一个Queue对象
    p = Process(target=task1, args=(q, ))
    p2 = Process(target=task2, args=(q, ))

    p.start()
    p2.start()
