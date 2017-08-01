from django.test import TestCase

# Create your tests here.
import threading

def func(i, e):
    print(i)
    e.wait() # 表示在这里检测信号。如果检测到为红灯，则停止。如果为绿灯，则放行
    print(i+100)

event = threading.Event()

for i in range(10):
    t = threading.Thread(target=func, args=(i,event))
    t.start()

event.clear() # 全部都停止，设置为红灯

inp = input(">>> ")
if inp == "1":
    event.set()  # 表示放行，设置为绿灯
