

def strpls(allowedchars = 'qwertyuiopasdfghjklzxcvbnm'):
    allallowed = allowedchars + allowedchars.upper()
    tag = True
    while True:
        userstr = input('Please enter a string: ')
        for char in userstr:
            if not char in allallowed:
                print('This is not a valid character', char)
                tag = False
            print('This is ok: ', char)
        if tag != False:
            continue
        break


strpls()
