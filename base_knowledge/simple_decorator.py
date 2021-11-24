# простой декоратор с встроенным таймером

import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('yep')
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        return (end_time - start_time), res, func.__name__
    return wrapper


@my_decorator
def my_sum(x, y):
    return x+y


print(my_sum(1, 2))

