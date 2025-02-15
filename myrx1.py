list=[-12,-8,-7,2,6,10]
a=[]
for i in list:
    a.append(abs(i)**2)
a.sort()
print(a)