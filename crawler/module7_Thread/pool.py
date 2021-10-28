"""
@author:ming
@file:pool.py
@time:2021/10/28
"""
import os
from concurrent.futures import ThreadPoolExecutor

"""
线程池
"""


def func(id):
    for j in range(50):
        print("线程:", id, j)
    return str(id) + "ok"


if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(func, id=i) for i in range(50)]
        for future in futures:
            print(future.result())
# with 外的东西要等到with中的执行完毕才能执行
# print(future.result()) # future.result()获取函数的返回值
print("main ok")
