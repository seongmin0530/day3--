#Q 5.6,5.7,5.8
Ducky = 'Duck'
Gourdy = 'Gourd'
Spitzy = 'Sitz'

latter = '{0}y Mc{0}face'
print('%sy Mc%sface' %(Ducky,Ducky))             #5.6
print('%sy Mc%sface' %(Gourdy,Gourdy))
print('%sy Mc%sface' %(Spitzy,Spitzy))
print()
print(latter.format(Ducky))                     #5.7
print(latter.format(Gourdy))
print(latter.format(Spitzy))
print()
print(f'{Ducky}y Mc{Ducky}face')                 #5.8
print(f'{Gourdy}y Mc{Gourdy}face')
print(f'{Spitzy}y Mc{Spitzy}face')