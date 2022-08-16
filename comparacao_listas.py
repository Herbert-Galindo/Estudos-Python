def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


li1 = ['a', 'b', 'c', 'd']
li2 = ['a', 'd', 'e', 'f']
print(Diff(li1, li2))
