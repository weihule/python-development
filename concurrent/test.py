from time import sleep
import threading


def task1():
    while True:
        print("sing ...")
        sleep(1)

def task2():
    while True:
        print("dancing ...")
        sleep(1.5)


if __name__ == "__main__":
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task1)
    t1.start()
    t2.start()
