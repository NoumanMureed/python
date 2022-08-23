import numpy as np
#opening a file and raeding first line

file=open('M:\Introduction to python\pythonQ5data.txt','r')
data=file.readline()
data=data.split()
#spliting first line
first=int(data[0])
second=int(data[1])
third=int(data[2])


lst = []
for count in file:
    if count != 0:
        count = count.split()
        lst.append(count)
# converting into numpy array and floating values
lst = np.array(lst, dtype=float)

lst1 = []

for i in lst:
    regno = int(i[0])
    e_marks = i[1]
    #print(e_marks)
    lst2 = []
    lst3 = []
    c_work = []
    #
    for j in range(2,third+2):
        c_work.append(i[j])
    #getting course marks average and converting into 40%
    #getting final marks average and converting into 100% marks
    course_marks = ((sum(c_work))/300)*40
    final_marks = round((e_marks/100)*60 +course_marks)
    lst2.append(regno)
    lst2.append(final_marks)
    lst2.append(course_marks)
    lst1.append(lst2)

reg_res = np.array(lst1)
result = (reg_res[:,:2]).astype(int)
#final result
grade_A = []
grade_B = []
grade_C = []
fail = []
# evaluating grade system
for l in result:
    if l[1]>=70:
        grade_A.append(l)
    elif l[1] >=50:
        if l[1]<70:
            grade_B.append(l)
    elif l[1] >=40:
        if l[1]<50:
            grade_C.append(l)
    else:
        fail.append(l)
# overwriting the result file.
f_open=open('M:\Introduction to python\ResultQ5.txt','w')
f_open.write("Students scoring A grade:\n")
for i in grade_A:
    i = str(i)
    f_open.write(i + '\n')
f_open.write("Students scoring B grade:\n")
for i in grade_B:
    i = str(i)
    f_open.write(i + '\n')
f_open.write("Students scoring C grade:\n")
for i in grade_C:
    i = str(i)
    f_open.write(i + '\n')
f_open.write("Failed Students:\n")
for i in fail:
    i = str(i)
    f_open.write(i + '\n')