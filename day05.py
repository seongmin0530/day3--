# function

import random

def make_person():
    """
    인원수, 나이 생성하는 함수
    :return: 인원수, 각각의 나이 리스트
    """
    person_number = random.randint(0, 10)
    ages = [random.randint(1, 50) for age in range(person_number)]
    return person_number, ages


def calculate_free(args):
    """
    놀이공원 요금 계산 프로그램
    :param args: ages
    :return: 지불할 총 입장료, 어른 수, 아이 수
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:
            total = total + 10000
            adults = adults + 1
        elif 1 <= age <= 19:
            total = total + 3000
            kids = kids + 1
        else:
            return False
    return total, kids, adults


person_number, ages = make_person()
total, kids, adults = calculate_free(ages)
print (f'환영합니다.\n총 {person_number}명이 입장하셨습니다.\n그 중 성인은 {adults}명, 학생은 {kids}명이며,\n총 입장료는 {total}원 입니다.')





# def do_nothing():
#     pass
#
#
# do_nothing()
# print(do_nothing())

# mamamoo = ['화사', '솔라', '휘인', '문별']
# print(mamamoo.remove('문별'))
# print(mamamoo)