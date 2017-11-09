# -*- coding: utf-8 -*-
####
#firstDuplicate.py
#metod would find first duplicate number in list number
#new: new list
#ver.1.1
####
def firstDuplicate(a):
    new=[]
    for i in range (0,len(a)):
        for j in range (i+1, len(a)):
            if a[i]== a[j]:
                new.append(j+1)
    if len(new)!=0:
        return a[min(new)-1]
    else:
        return -1
