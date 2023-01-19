# 9 - 3
def test(func):
    print(func.__name__)


@test
def start():
    pass


@test
def end():
    pass