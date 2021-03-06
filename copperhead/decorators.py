# AUTOGENERATED! DO NOT EDIT! File to edit: decorators.ipynb (unless otherwise specified).

__all__ = ['trace']

# Cell

def trace(func):
    """ Prints the argument and return values of a function call. Especially useful for recursive functions. """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}:({args!r}, {kwargs!r}) -> {result!r}")
        return result
    return wrapper