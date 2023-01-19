# generator

def a():  # generator
    yield 1  # 반환한 이후에도 종료되지 않고 계속 반환
    yield 2
    yield 3


def b():
    return 1  # return후 종료
    return 2  # 유효하지 않음(실행되지 않음)
    return 3  # 유효하지 않음(실행되지 않음)

print(a())
for i in a():
    print(i)