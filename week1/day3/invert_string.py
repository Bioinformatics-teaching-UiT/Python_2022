"""
This scripts has two functions to invert a string
Uppercase is changed to lowercase, and vice versa
"""

## solution 1
## defines first an is_lower function
## (is.lower()) method should exist and work ;)
## but this is a valid way to also do this
def is_lower(singleletterstr):
    if singleletterstr == singleletterstr.lower():
        answer = True
    else:
        answer = False
    return answer
## then defines the inverse function
def str_rev(userstring):
    newstr = ''
    for i in userstring:
        if is_lower(i) == True:
            temp = i
            newstr = newstr + temp.upper()
        else:
            temp = i
            newstr = newstr + temp.lower()
    return newstr

print(str_rev('aaaaaBBBBBB')) # should get: AAAAAbbbbbb
print(str_rev('1234&###!aaBBBB')) # should get: 1234&###!AAbbbb

## solution 2: another way to do this is to make a list of your
## inverted characters, and then join them back into a string afterwards
def invert_str(somestr):
    invertedlist = []
    for char in somestr:
        if char.islower():
            invertedlist.append(char.upper())
        else:
            invertedlist.append(char.lower())
    return ''.join(invertedlist)

print(invert_str('aabbCCCCCC')) # AABBcccccc
print(invert_str('12436ffwejioJOiwefjie')) # 12436FFWEJIOjoIWEFJIE