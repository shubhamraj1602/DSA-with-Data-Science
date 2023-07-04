import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"The execution time of {func.__name__} is {end_time - start_time} seconds.")
        return result
    return wrapper

