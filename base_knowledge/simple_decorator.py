def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('yep')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def my_sum(x, y):
    return x+y


my_sum(1, 2)
