"""
@author:ming
@file:process_test.py
@time:2021/10/28
"""

from multiprocessing import Process

"""
多进程
"""


# class MyProcess(Process):
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     def run(self) -> None:
#         for i in range(1000):
#             print("MyProcess:", self.name, i)
#
#
# if __name__ == '__main__':
#     p = MyProcess("abc")
#     p.start()
#
#     for i in range(1000):
#         print("main:", i)

def func(name):
    for i in range(1000):
        print("func:", name, i)


if __name__ == '__main__':
    process = Process(target=func, args=("bbb",))
    process.start()

    for i in range(1000):
        print("main:", i)
