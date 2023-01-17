# list

# scores = ('B+', 'A+', 'C+')
# print(scores[1],scores[2])
# temp = list(scores)
# temp[1] = 'c+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores[1],scores[2])

big_bang = ['GD','태양', 'TOP','대성', '승리']
exo = ['백현', '첸']

big_bang.append('인하')  #list 맨뒤에 요소 추가
print('append. : ', big_bang)

big_bang.insert(1,'KEB')  #list 중간에 요소 추가
print('insert. :', big_bang)

print('list의 복제 :', big_bang * 2)  #list의 복제

exo.extend(big_bang)  #list의 결합 == exo = exo + big_bang
print('extend. :',exo)

#print(exo.pop())  #빅뱅 전체 pop
print(exo[2].pop())  #빅뱅의 승리 pop
print(exo.[2].pop(-2))  #빅뱅의 탑 pop
exo.remove('인하')  #인하 삭제

#+del

