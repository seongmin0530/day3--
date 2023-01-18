# function

def answer():
    """
    60 프린트하는 함수
    :return:
    """
    print(60)


def call_func(func):
    """
    매개변수로 함수를 넘겨받아 실행시키는 함수
    :param func:다른 함수
    :return:
    """
    func()


def subtract(num1, num2):
    print(num1-num2)


def run_func(func, arg1, arg2):
    """
    함수를 매개변수로 받아 함수 안에서 해당 함수를 실행
    :param func: 함수
    :param arg1: 정수 값
    :param arg2: 정수 값
    :return:
    """
    func(arg1, arg2)


run_func(subtract, 99, 88)