# prime number by 'while'

number = int(input('정수 입력.: '))

count = 0
j = 1
while j <= number:
    if number % j == 0:
        count +=1
    j+=1
if count == 2:
    print(f'{number} is prime Number.')
else:
    print(f'{number} is not prime Number.')

