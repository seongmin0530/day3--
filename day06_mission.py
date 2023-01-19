# 9 - 4
class OopsException(Exception):
    pass


try:
    words_list = input('문자열을 입력하세요. :').split()
    for word in words_list:
        if word =='Oops' or word == 'oops':
            raise OopsException
except Exception as error:
    print('Caught an oops')


