#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:51:01 2018

@author: alemeneses
"""

#%%

def bubble(lst):
    for j in range(0, len(lst) - 1):
        for i in range(0, len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                
#%%
                
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    return merge(merge_sort(left), merge_sort(right))
