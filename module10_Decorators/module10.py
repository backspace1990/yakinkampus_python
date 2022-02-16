import time


def tests():
    print("abcde")


f = tests
tests()
print(type(tests))
print(type(f))
f()
print(50 * "*")


def test2():
    print("test2 is working!!")

    def test3():
        return "test3 is working!!"

    return test3


# test2()

f2 = test2()
print("222")
print(f2.__name__)
print(f2.__dict__.__sizeof__())
print(f2.__sizeof__())
print(f2.__code__)
print(f2.__globals__)
print(f2(), '\n')

print(20 * "****DECORATOR****")


# Decorator

def test4():
    return "test4 is working"


def test5(arg):
    print("test5 is working")
    print(arg())


test5(test4)

print(20 * "****DECORATOR****")


def deco(arg_func):
    def wrapper():
        print("Start")
        print(arg_func())
        print("Finish")

    return wrapper()


deco(test4)
print(20 * "****DECORATOR****")


def prints(arg):
    return arg


def deco1(arg_func, arg_arg_funcs):
    def wrapper():
        return "Start", arg_func(arg_arg_funcs), "Finish"

    return wrapper()


objects = deco1(prints, "dengesiz")

for i in objects:
    print(i)

print(objects)
print(objects.count("Finish"))

print(20 * "****DECORATOR****")


def deco2(arg):
    def wrapper():
        print("Starter Deco")
        arg()
        print("Finish Deco")

    return wrapper


@deco2
def printer():
    print("Printer")


printer()

print(20 * "****DECORATOR****")


def deco3(arg):
    def wrapper(*args):
        print("Starter Deco")
        arg(*args)
        print("Finish Deco")

    return wrapper


@deco3
def plus(a, b):
    print(a + b)


plus(4, 5)

print(20 * "**** DECORATOR(Arguman) ****")


def deco4(arg1, arg2):
    def ara_katman(funcs):
        def wrapper(*args):
            print(arg1)

            funcs(*args)

            print(arg2)

        return wrapper

    return ara_katman


@deco4("Start Deco", "Finish Deco")
def plus2(a, b):
    print(a + b)


plus2(5, 35)

print(20 * "**** DECORATOR(Arguman) ****")


def time_func(func_arg):
    def wrapper(*args):
        starts = time.time()
        print(f"Time Starts : \t {starts}")

        func_arg(*args)

        finish = time.time()
        print(f"Time Finishes : \t {finish}")
        print(f"Time functions : \t {finish - starts}")

    return wrapper


@time_func
def factorial(arg):
    sum = 1

    while arg > 1:
        sum = sum * arg
        arg -= 1

    print(sum)


factorial(5000)
