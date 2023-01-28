import functools
from time import time


# + Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
# + Реализовать декоратор, который измеряет скорость выполнения функций.
# + Реализовать декоратор, который будет считать, сколько раз выполнялась функция
# + Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение функции, закончено выполнение функции
# + Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать в консоль сообщение об ошибке




class DecoratorCansel(object):


    def __init__(self, argument):
        self.arg = argument
        self.result_time = None

    def __call__(self, func_name):
        @functools.wraps(func_name)
        def decorated(*args, **kwargs):
            start_time = time()

            # fn(*args, **kwargs)
            end_time = time()
            self.result_time = round(end_time - start_time, 3)
            print(f"   {func_name}     ___  is canseled!      Time={self.result_time}")
        return decorated

class Test:
    @DecoratorCansel(f" SID ")
    def approach(self):
        print(f"  STARR  ")


@DecoratorCansel(f'   def   ')
def some_other_function():
    print('   ****   ')


@DecoratorCansel(f'   test_def   ')
def new_array(start, end):
    print([i for i in range(start, end)])


Test().approach()
some_other_function()
new_array(1, 15)





