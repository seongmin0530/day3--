# 구구단 by for문

while True:
    dan = int(input('dan(0 to quit) : '))

    if dan == 0:
        break
    if 1< dan < 10:
        for i in range(1,10):
            print('{0} * {1} = {2}'.format(dan,i,dan*i))
    else:
        print('2에서 9사이의 값을 입력하세요.')