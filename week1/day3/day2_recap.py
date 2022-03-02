"""
Script to recap key data type concepts from day 2
1. lists
2. dictionaries
5. list/dictionary comprehension

We will practice loops in other exercises
"""

## make a list of three things you like to eat for lunch
lunchitems = ['bread', 'ham', 'orange']
print(lunchitems)

## add two more items
lunchitems.extend(['apple', 'banana'])
print(lunchitems)

## delete the first item, then delete the last item
# del
# pop()

del lunchitems[::4]
print(lunchitems)


## write an if-statement to check if 'cheese' is in your list
## if not, add it
if 'cheese' not in lunchitems:
    lunchitems.append('cheese')
print(lunchitems)

## now make a new list, with the number or amount of these items you eat
## if I had 'bread' in my first list, I would put 4 for 4 slices in the second list
lunchcounts = [10, 2, 1, 5]

## using a dictionary comprehension, join your two lists into a dictionary
## what makes sense as key and what makes sense as values?
## [ expression for i in range() ]

#lunchdict = { lunchitems[i] : lunchcounts[i] for i in range(len(lunchitems))}
#print(lunchdict)
lunchdict = dict(zip(lunchitems, lunchcounts))
print(lunchdict)

## bonus: can you make another dictionary where only items that you eat more than one of are added?
## [ expression for i in range() if condition ]
lunchdict_multiples = { lunchitems[i] : lunchcounts[i] for i in range(len(lunchitems)) if lunchcounts[i] > 1}
print(lunchdict_multiples)