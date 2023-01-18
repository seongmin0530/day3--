# function lamba
# 람다 = 일회성 익명 함수 =>함수를 1회용할 때 사용

import random
#
#
# def process(num_list, func):
#     for num in num_list:
#         print(func(num), end='\t')
#
#
# def squares(n):
#     """
#     매개변수를 제곱하여 return하는 한ㅁ수
#     :param n: intager
#     :return: intager
#     """
#     return n**2
#
#
# numbers = [random.randint(1, 100) for i in range(5)]
# print(numbers)
# process(numbers, squares)


# ******************************************************
# Use lambda
# ******************************************************
def process(num_list, func):
    for num in num_list:
        print(func(num), end='\t')


numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x * x)
