from functools import wraps


def checker(check_func):
    def _checker(func):
        @wraps(func)
        def wrapper(arg):
            if check_func(arg):
                return func(arg)
            else:
                raise ValueError(f'wrong data: {arg}')
        return wrapper
    return _checker


@checker(lambda x: x > 0)
def calc_cube(num):
    """this function should convert number to cube"""
    return num ** 3


print(calc_cube(int(input('Please enter a number greater than zero: '))))
print(calc_cube.__name__)
print(calc_cube.__doc__)
