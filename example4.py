import statistics
from functools import wraps

def decorator_factory(kind = "mean"):
    def decorator(func):
        @wraps(func)
        def wrapper(numbers):
            if kind == "mean": return func(numbers)
            if kind == "mode": return statistics.mode(numbers)
            return statistics.median(numbers)

        return wrapper
    return decorator

@decorator_factory("mode")
def average(numbers):
    return sum(numbers) / len(numbers)

scores = [90, 62, 85, 62, 92, 88, 62, 88]
print(f"{average(scores)}")
