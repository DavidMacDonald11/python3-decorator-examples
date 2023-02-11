import math
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(numbers):
        value = func(numbers)
        value /= 10

        decimal = value - math.floor(value)
        value = math.floor(value)

        if decimal < .25: return value * 10
        if decimal < .75: return (value + .5) * 10
        return (value + 1) * 10

    return wrapper

@decorator
def average(numbers):
    return sum(numbers) / len(numbers)

scores = [90, 85, 62, 92, 88]
print(f"{average(scores)}")
