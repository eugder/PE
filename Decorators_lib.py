def test_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        r = func(*args, **kwargs)
        print("After")
        return r
    return wrapper