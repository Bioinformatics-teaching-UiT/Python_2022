"""
Small practice with if statements
and names
"""
# if your name is between 10 and 20 characters (counting spaces)
# print some silly statements, otherwise if your name is  > 20
# say that it is too long
# if your name is less than 10 then don't say anything
# importance of indentation here to indicate which condition
# the else belongs to
name = input('Please write your full name: ')
if len(name) > 10:
    print('You have a long name!')
    if len(name) < 20:
        print('Your name is not too long.')
    else:
        print('Your name is too long.')

# if there is a specific condition you want to test for
# in this case if name is between 10 and 20,
# state it outright in your if statement, don't nest if statements
# because that is harder to read
# we also have this variable nickname that depending on the length of your
# fullname may or may not be filled, so best practice is to initialise
# this to None in case you reference it later to not run into variable
# doesn't exist errors
name_length = len(name)
nickname = None
if name_length > 10 and name_length < 20:
    print('You have a long name but not too long.')
    nickname = input('What is your nickname? ')
    print(f'Your nickname is {nickname}.')
else:
    print('Your name is either too short or very long.')

# so if you hit the else statement above and now need
# to operate on nickname, you would not enter this if statement below
# because it would still be None
#if nickname:
    # do something with it
#else: