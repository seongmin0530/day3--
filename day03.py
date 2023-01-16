#mission in class
#1. 숫자 2개 입력받음
#2. 입력 받은 값 들 사이의 소수 구하는 프로그램 작성

num1, num2 = map(int, input("두개 정수 입력 : ").split())           #시작점 끝점 입력받음

if num1 > num2 :
    num1, num2 = num2,num1                                     #파이썬만 가능한 문법

for i in range (num1, num2+1):                                # 입력한 수 만큼 소수 찾기 반복하는 for문
    #is_prime = True                                       # 소수 판단 변수 초기화(필요 없음 if문이 있기때문)
    if i <= 1:
        continue
    for j in range(2,i):                              # 소수 판단 위한 for문
        if i % j == 0:                                # if 1
            #is_prime = False
            break
    else:                                            # if 1과 매칭되는 else문
        print(i, end = '\t')


