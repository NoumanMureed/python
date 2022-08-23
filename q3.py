# String palindrome function
def is_palindrome(s):
    r=s[::-1]
    if r==s:
        return True
    else:
        return False
#print(is_palindrome('ABCDCBA'))


def rep(n):
    x=n.lower()
    s={}
    if len(x)==1:
        return x
    else:
        for i in x:
            if i in s:
                s[i]+=1
            if i not in s:
                s[i]=1
            m=s
            d={}
            for key,value in m.items():
                if value in d:
                    d[value].append(key)
                else:
                    d[value]=[key]
        h=sorted(d.items())
        if len(h)>=3:
            return h[-3][1][0]
        else:
            return h[-1][1][0]
            
#print(rep("damzasaee$%^&*"))

# function convert string, uppercase-letters, lower-case letters, digits and return a tuple
def count(str):
    lowercase=0
    uppercase=0
    digits=0
    for i in str:
        if i.islower()==True:
            lowercase+=1
        if i.isupper()==True:
            uppercase+=1
        if i.isdigit()==True:
            digits+=1
    return ((lowercase,uppercase,digits))

#print(count('MechineRestoration'))