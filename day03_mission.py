#Q 6.3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print('Too low')
    elif number > guess_me:
        print('oops')
        break
    else:                           # guess_me == number
        print('found it!')
        break
