# function Closures

def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):
        nonlocal temp
        # x = 11  # local variable
        temp = temp + x + n - y
        return temp
    return add_sub

c1 = calculate()  # c1이 calculate()함수의 번지주소를 가지고 있어 언제든 사용할 수 있게 해줌
for i in range(4):
    print(c1(i),end='\t')  # 일반함수와는 다르게 함수가 종료되어도 지역변수가 남아있음....?
print(type(c1))
print(c1)