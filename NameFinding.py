import re
import numpy as np

arr4 = np.arange(100)
arr2 = [None for _ in range(100)]
arr3 = [None for _ in range(100)]
Path1 = input('Enter the path of the Text file: ')
Name_of_Text = input('Enter the name of text file: ')
roll_object2 = open(str(Path1) + '\\' + str(Name_of_Text) + '.txt')
roll_list = roll_object2.readlines()
dictionary = {}
keys = range(1, 101)
values = [None for _ in range(1, 101)]
i = 0
while i < len(roll_list):
    roll_object1 = re.compile(r'(\d\d\d\d)(_)(\S+\s\S+)')
    mo = roll_object1.search(roll_list[i])
    if mo is not None:
        arr4[i] = mo.group(1)
        arr2[i] = mo.group(3)
        dictionary[arr4[i]] = arr2[i]
    i = i + 1
