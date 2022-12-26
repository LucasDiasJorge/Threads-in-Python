import threading
import time


l = "false"


def thread1():
    x = 0
    print("thread running")

    while x < 10:
        x += 1
        if x == 7:
            l = "true"
            print(l)
            time.sleep(10)

    threading.Thread(target=function1).start()


def function1():
    print(l)
    print("function running")


threading.Thread(target=thread1).start()
