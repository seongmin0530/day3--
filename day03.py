# prime number by 'for'

number = int(input('정수 입력.: '))

count = 0
for i in range(1, number+1):
    if number % i == 0:
        count +=1
if count == 2:
    print(f'{number} is prime Number.')
else:
    print(f'{number} is not prime Number.')

