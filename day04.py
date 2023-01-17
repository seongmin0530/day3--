# Dictionary

students = {'name': 'kin inha', 'age': 23, 'eyes': [0.9, 1.1]}

# for i in students.key():  #bring only 'key'
# for i in students.values():  # bring only 'value'
# for i in students:  #bring 'key : value'

# ************************************************************************************************
# personal information
# ************************************************************************************************
# for k,v in students.items():  # bring 'key', 'value' by unpacking
#     print(f'{k} : {v}')
#
# print(f'이름은 {students["name"]}, 나이는{students["age"]}세,', end=' ')
# print(f'시력은 좌: {students["eyes"][0]}, 우: {students["eyes"][1]}')


# ************************************************************************************************
# alcohol suggestion
# ************************************************************************************************
import random

alcohol_foods = {
    '맥주' : '치킨',
    '소주' : '골뱅이소면',
    '와인' : '치즈',
    '고량주' : '짬뽕'
}

alcohol_list = list(alcohol_foods)  # only key

# food_list = [food for food in alcohol_foods.values()]  #only value

while True:
    alcohol = input(f'술을 선택하세요 0) 랜덤 1){alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} :')
    print(f'{alcohol}을 선택하셨습니다.')
    if alcohol == '5' :
        print('다음에 또 오세요.')
        break
    elif alcohol == '0' :
        print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {alcohol_foods[random.choice(alcohol_list)]} 입니다.')
#       print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)]} 입니다.')
    elif alcohol == '1' :
        print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]} 입니다.')
    elif alcohol == '2' :
        print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]} 입니다.')
    elif alcohol == '3':
        print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]} 입니다.')
    elif alcohol == '4':
        print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]} 입니다.')
    else:
        print('1~4사이의 메뉴를 입력해주세요.')