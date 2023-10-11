import functools
from time import ctime, gmtime, mktime, time


# + Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
# + Реализовать декоратор, который измеряет скорость выполнения функций.
# + Реализовать декоратор, который будет считать, сколько раз выполнялась функция
# + Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение функции, закончено выполнение функции
# + Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать в консоль сообщение об ошибке


class DecoratorCansel(object):

    def __init__(self, argument):
        self.arg = argument
        self.result_time = None
        self.counter = 0

    def __call__(self, func_name):
        @functools.wraps(func_name)
        def decorated(*args, **kwargs):
            start_time = time()
            print(f"Start function {start_time}")

            fun = func_name
            a = 15 ** 15 ** 5
            end_time = time()
            print(f"End function {end_time}")
            self.result_time = round(end_time - start_time, 8)
            # self.result_time = end_time - start_time, 3
            self.counter += 1
            print(f"Function {func_name.__name__} is canseled!      Time={self.result_time}")
            print(self.counter)

        return decorated


class DecoratorError(object):

    def __init__(self, argument):
        self.arg = argument


    def __call__(self, func_name):
        @functools.wraps(func_name)
        def decorated(*args, **kwargs):
            try:
                # print(f"Function {func_name.__name__}")
                fun = func_name()
                print(fun)
            except:
                print(f"Function {func_name.__name__} Error !")
        return decorated

@DecoratorError(f"Try-Except")
def name_int(self):
    name = "idea"
    # print(f"___{int(name)}___")
    print()
    return f"___{name}___"
name_int()

class Test:
    # @DecoratorCansel(f"Can-1")
    # @DecoratorError(f"Can-1")
    def name_int(self):
        name = "idea"
        # print(f"___{int(name)}___")
        print(f"___{name}___")

    @DecoratorCansel(f'Can-2')
    def some_other_function(self):
        print('   ****   ')

    @DecoratorCansel(f'Can-3')
    def new_array(start, end):
        print([i for i in range(start, end)])

    def run(self):
        test_us = Test()
        test_us.name_int()
        test_us.some_other_function()
        test_us.new_array()

# test=Test()
# test.run()