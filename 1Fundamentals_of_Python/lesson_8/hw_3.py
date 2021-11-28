from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*nums):
    """this function should convert number to cube"""
    return list(map(lambda x: x ** 3, nums))


print(calc_cube(2, 3))
print(calc_cube.__name__)
print(calc_cube.__doc__)
