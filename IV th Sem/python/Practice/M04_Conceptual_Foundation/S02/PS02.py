'''
def Reverse_list(li):
    res=[]
    stop=-1*(len(li)+1)
    for i in range(-1,stop,-1):
        res.append(li[i])
    return res
print(Reverse_list([1,2,3,4]))
'''

li=[1,2,3,2,4,3,1,5]
d={}
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)


li=[1,2,3,2,4,3,1,5]
d={}
for i in li:
    d[i]=d.get(i,0)+1
print(d)