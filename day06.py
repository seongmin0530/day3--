# decotator
def document_info(func):
    def new_function(*args, **kwargs):
        print('실행중인 함수: ',func.__name__)
        print('위치 기반 인수들 :', args)
        print('키워드 기반 인수들 :', kwargs)
        result = func(*args, **kwargs)
        print('실행결과: ', result)
    return new_function


@document_info
def sub_int(x, y):
    return x - y


@document_info
def mul(x):
    return x * x


print(sub_int(7, 3))
print(mul(4))
