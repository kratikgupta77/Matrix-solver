n1=int(input('number of rows'))
n2=int(input('number of columns'))
print("enter entry of A")
l2=[]
for i in range(1,n1+1):
    l1=list(map(int,input().split()))
    l2.append(l1)
from sympy import *
m = Matrix(l2).rref()
print ("rref")
k1=m[0]
k2=m[1]
k1=list(k1)
k2=list(k2)
def convertlist(lst, n):
    nested_list = [lst[i:i+n] for i in range(0, len(lst), n)]
    return nested_list
t1=convertlist(k1,n2)
print(t1)
p1=[]
yk=[]
if n2 > n1 :
    for v in t1:
        yk.append(0-v[n2-1])
    p1.append(yk)
k4=0
f=[]
lst=[]
j=1
yt=[]
p5=0
for i in t1:
    if j==n2+1:
        break
    if i[k4]==0:
        f.append(k4)
        if t1.index(i)==0:
           for y in i:
               if p5==0:
                   p5=p5+1
                   continue
               if y!=0:
                   yt.append(i.index(y))
                   break
        k4=k4+1
        j=j+1
    else:
        k4=k4+1
        j=j+1
        continue
if len(yt)>0:
    f.remove(yt[0])
for i in f :
    for j in t1:
        lst.append(0-j[i])
    lst[i]=lst[i]+1
    p1.append(lst)
    lst=[]
lit=[]
print("parametric solution")
for i in range(1,n1+1):
  lit.append(0)
k3=0
s=""
if len(p1)!=0:
 if len(f)==0:
    n2=str(n2-1)
    p1[k3]=str(p1[k3])
    s=s+"+"+"x_"+n2+"*"+p1[k3]
 for i in f:
    i=str(i)
    p1[k3]=str(p1[k3])
    s=s+"+"+"x_"+i+"*"+p1[k3]
    k3=k3+1
lit=str(lit)
s=lit+"+"+s
print(s)
