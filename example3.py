from functools import wraps

def decorator_factory(*d_args, **d_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value

        return wrapper
    return decorator

@decorator_factory(*d_args, **d_kwargs)
def foo(*args, **kwargs):
    pass
