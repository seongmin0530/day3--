#******************************************************#
#Q1
#******************************************************#
song = """When an ell grabs your arm,
...And it causes great harm,
...that's -a moray"""

print(song.replace(' m',' M'))      #My answer


#Answer
song_list = song.split()
print(song_list)
song_list[13] = song_list[13].title()
song_string = ' '.join(song_list)
print(song_string)

#******************************************************#
#Q2
#******************************************************#
questions = ["Q1","Q2","Q3"]
answer = ["A1","A2","A3"]
print(f'Q:{questions[0]}')
print(f'A:{answer[0]}')

#******************************************************#
#Q3
#******************************************************#
a = 'roast beef'
b = 'ham'
c = 'head'
d = 'clam'
print("My kitty cat likes %s,\nMy kitty cat likes %s,\nMy kitty cat fell on his %s And now thinks he's a %s" %(a,b,c,d))