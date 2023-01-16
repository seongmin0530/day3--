# prime number 반복횟수 줄이기 + 연산과정 줄이기

number = int(input('정수 입력.: '))

is_prime = True                 # count +=1에서의 2개의 연산과정 줄일 수 있음 + True/False타입이 더 작음

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break                   # 의미 없는 반복 줄이기 위함 -> 소수가 아닐 때 성능 up
if is_prime:
    print(f'{number} is prime Number.')
else:
    print(f'{number} is not prime Number.')

