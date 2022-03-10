"""
Useful modules for the project

1. pathlib
"""

from pathlib import Path

outputdir = Path('/home/yin/UiT/pythoncourse_2022/Python_2022/week2/')
file1 = Path('somefile.txt')

print(file1.stem)
print(file1.suffix)

# make a series of files somefile1.txt, somefile2.txt, somefile3.txt
# with the same content as our somefile.txt

# read in content of file1
# print out content
with open(file1, 'r') as f:
    lines = f.readlines()
print(lines)

# for loop to write into new files
# uses the joinpath function to join a Path object with a string
# or join two Path objects
for i in range(1,4):
    filename = Path(f'{file1.stem}{i}.txt')
    print(filename)
    fulloutputpath = outputdir.joinpath(filename)
    print(fulloutputpath)
    with open(fulloutputpath, 'w') as f:
        f.write(lines[0])


