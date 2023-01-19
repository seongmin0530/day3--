# exception
try:
    raise Exception("쉬는 시간")
    expr = input('분자,분모 입력 : ').split()
    print(int(expr[0]) / int(expr[1]))

except ValueError as err:
    print('숫자를 입력해주세요.')

except ZeroDivisionError as err:
    print('분모에 0이 올 수 없습니다.')
except IndexError as err
    print('범위에 문제가 있습니다.')
except Exception as other:
    print('예외 발생')
else:  #예:외가 발생하지 않앗을 때
    print('프로그램 정상 ', end = ' ')
finally():  #예외 발생 여부와 상관 없이 무조건 실행

print('종료')






# def div_calc(a, b):
#     """
#     나누기 함수
#     :param a:분자
#     :param b: 분모
#     :return: 계산결과
#     """
#     return a / b
#
# print(div_calc(15, 3))
# print(div_calc(15, 0))  # 에러 발생 (분자가 0이기 때문에 나눌 수 없음)