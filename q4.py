import pandas as pd

str2 = "Sorry! No Records Found"
updatedlist = []
notavailable = []

# checking txt file and converting lines into tuples
try:
    studentlist1 = open("M:\Introduction to python\Q4 data\Q4data.txt", "r")
    data = [tuple(line.split(',')) for line in studentlist1]
    dd = [x[:-1] for x in data]
    # print(data)
except:
    print("Sorry! No Records Found")


def myfunc(mylist, mystr):
    x = 0
    b = True
    while(b == True):
        for index, tup in enumerate(mylist):
            # checking the department and appending into updated list 
            a = tup[0]
            b = tup[1]
            c = tup[2]
            if c == mystr:
                updatedlist.append((a, b))
            else:
                x = 1
        df = pd.DataFrame(updatedlist, columns=['Name', 'Reg ID'])
        if len(updatedlist) > 0:
            print(df.sort_values(by=['Reg ID']))
        else:
            print(str2)

        a = input("Press 'Y' to find another Department or Press 0 to exit")
        if a == "Y":
            myfunc(dd,str1)
        else:
            break

str1 = input("Enter Department Name:")
myfunc(dd, str1)