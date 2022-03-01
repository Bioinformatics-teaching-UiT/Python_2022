"""
This script contains the basics for operating with
dictionaries - declaring, getting the length,
adding entries, and getting lists of keys and values
"""

# declare a dictionary
alpha_num_dict = {'a':1, 'b':2, 'c':3}
print(alpha_num_dict)

# how long is my dictionary?
print(len(alpha_num_dict))

# access a certain value from a dictionary using the key
print(alpha_num_dict['a'])

# how to add to a dictionary
alpha_num_dict['d'] = 4

# get a list of keys and or values from your dictionary
mykeys = list(alpha_num_dict.keys())
print(mykeys)
myvalues = list(alpha_num_dict.values())
print(myvalues)

# very useful loop with dictionaries
# you can actually loop over pairs instead of one i
for k, v in alpha_num_dict.items():
    print(k, v)