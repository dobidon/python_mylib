# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:18:27 2019

@author: omemi
"""

def dict_get(dictionary, search, func=None):
    ans = None
    for key, value in dictionary.items():
        if key == search:
            if func != None:
                func(dictionary, key)
            ans = dictionary[key]
            break
        if isinstance(value, dict):
            ans = dict_get(value, search)
            if ans != None:
                break
#            else:
#             print (k,":",v)
    return ans

def dict_findall(dictionary, search, func=None):
#    print('Current keys: '+str(dictionary.keys())) # Debug
    ans = {} if func == None else None
    for key in dictionary.keys():
        if key == search:
            if func != None:
                func(dictionary, key)
            else:
                ans[key] = dictionary[key]
        if isinstance(dictionary[key], dict):
            res = dict_findall(dictionary[key], search, func)
            if res != None:
                ans[key] = res
    return ans

def subdict_update(dictionary, subdict, key, value, method='replace'):
    t_dict = dict_get(dictionary, subdict)
    if t_dict.get(key) != None:
        if method == 'replace':
            t_dict[key] = value
        elif (method == 'add') and (type(t_dict[key]) == type(value)):
            t_dict[key] += value
        else:
            return
def dict_keys_get(dictionary, ignore=['']):
    ans = []
    for key in dictionary.keys():
        is_valid = True
        for i in ignore:
            if key == i:
                is_valid = False
        if is_valid:
            ans.append(key)
    return ans