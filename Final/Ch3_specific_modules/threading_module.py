import threading


def hello_world():
    print("Hello world")


t1 = threading.Thread(target=hello_world)
t1.start()


def f1():
    [print(f"F1: {x}") for x in range(10000)]


def f2():
    [print(f"F2: {x}") for x in range(10000)]


t2 = threading.Thread(target=f1)
t3 = threading.Thread(target=f2)

t2.start()
t3.start()

