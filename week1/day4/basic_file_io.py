"""
Basic file operations in Python
"""

# open a file
f = open('gcseqs.fasta', "r")
# save the lines in a list
listoflines = f.readlines()
print(listoflines)
# save the lines in a list without newline characters
listofnewlines = []
for line in listoflines:
    listofnewlines.append(line.strip())
print(listofnewlines)
# don't forget to close the file
f.close()

# how to write into a file
# open a file
# careful!! the 'w' tag will overwrite the file each time you call it
# use 'a' for append if you want to add to an existing file
newfile = open('samplefile.txt', 'w')
# write some lines in a file
newfile.write('This is the first line of our file\n')
newfile.write('1\t2\t3\t4\n')
# close the file
newfile.close()

