# function prime number
def is_prime(number):
    """
    매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
    :param number:
    :return: True or False
    """

    if number <= 1:
        return False
    for k in range(2, number):
        if number % k == 0:
            return False
    else:
        return True

start = int(input("시작값을 입력하세요: "))
end = int(input("시작값을 입력하세요: "))

if start > end :
    start, end = end, start

for i in range(start,end+1):
    if is_prime(i):
        print(i, end='\t')
