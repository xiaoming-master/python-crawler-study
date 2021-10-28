"""
@author:ming
@file:thread_test.py
@time:2021/10/28
"""
from threading import Thread

"""
多线程测试
创建多线程有两种方式：
    1、创建一个类继承Thread类，并重写run()方法
    2、创建一个方法，再创建一个Thread对象，将方法作为参数传给Thread的构造函数，最后执行start()方法
"""


# class MyThread(Thread):
#     def __init__(self, name):
#         super(MyThread, self).__init__()
#         self.name = name
#
#     def run(self):
#         for i in range(1000):
#             print("MyThread", self.name, i)
#
#
# if __name__ == '__main__':
#     t = MyThread("线程")
#     t.start()
#     for i in range(1000):
#         print("main", i)

def func(name):
    for i in range(1000):
        print("func", name, ":", i)


if __name__ == '__main__':
    t = Thread(target=func, args=("线程",))  # target接收需要执行的函数，args 接收函数的参数，必须是一个元组
    t.start()
    for i in range(1000):
        print("main:", i)
