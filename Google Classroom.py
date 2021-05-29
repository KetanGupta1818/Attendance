import numpy as np
import re
obj = open('C:\\Users\\Admin\\Documents\\Python practice\\Attendance\\GC_emA.txt')
Lst = obj.readlines()
Number_Students = int(input('Enter the total number of students in the class: '))
present_students1 = np.arange(Number_Students)
j = 0
count = 0
for i in range(len(Lst)):
    obj_regex = re.compile(r'\d\d\d\d')
    mo = obj_regex.search(Lst[i])
    if mo is not None:
        present_students1[j] = mo.group()
        j = j + 1
        count = count + 1
present_students1.sort()
Roll1 = int(input('Enter the roll number of First Student: '))
Total_Student = np.arange(Roll1, Roll1+Number_Students)
Absent_Student = np.arange(Number_Students)
j = 0
p = 0
print("Student's roll numbers who have not joined the Google class-room are: ", end=' ')
while j < Number_Students:
    a = 0
    count1 = 0
    while a < Number_Students:
        if Total_Student[j] == present_students1[a]:
            count1 = count1 + 1
        a = a + 1
    if count1 == 0:
        Absent_Student[p] = Total_Student[j]
        print(Total_Student[j], end=' ')
        p = p + 1
    j = j + 1
print(end='\n')
print(f'{p} students have not joined..')
