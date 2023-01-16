# prime number 반복횟수 줄이기

number = int(input('정수 입력.: '))

count = 0

for i in range(2, number):
    if number % i == 0:
        count +=1
if count:                       # count가 0 이 아니면
    print(f'{number} is not prime Number.')
else:
    print(f'{number} is prime Number.')

