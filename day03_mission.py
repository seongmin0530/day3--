#Q 6.2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('Too low')
    elif number > guess_me:
        print('oops')
        break
    else:                           # guess_me == number
        print('found it!')
        break
    number += 1
