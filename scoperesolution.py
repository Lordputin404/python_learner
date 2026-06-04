# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

def func3():
    print(x)

def func4():
    print(x)

x = 4

func3()
func4()

from math import e

def func5():
    print(e)

func5()