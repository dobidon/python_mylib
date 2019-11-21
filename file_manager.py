# -*- coding: utf-8 -*-
import os, pathlib

def Create_My_File(file_name, file_content, encoding='iso-8859-9'):
    g = open(file_name, 'w+', encoding=encoding)
    g.write(file_content)
    g.close()
    return os.path.abspath(file_name)

def Read_My_File(file_name, encoding='utf-8'):
    output_var = ''
    if (encoding == 'tr'):
        encoding = 'iso-8859-9'
    f = open(file_name, 'r', encoding=encoding)
    for x in f:
        output_var += x
    f.close()
    return output_var

def Clean_Folder(folder_path, count=0):
    file_array = os.listdir(folder_path)
    file_array.sort()
    t_count = 0
    
    if count < 0:
        count = 0
    
    if not(count):
        count = len(file_array)
        
    for the_file in file_array:
        if t_count >= count:
            return
        file_path = os.path.join(folder_path, the_file)
        try:
            if os.path.isfile(file_path) and not(the_file.startswith('.')):
                os.unlink(file_path)
                t_count += 1
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception:
            return

def Files_Check(file_list):
    ans = True
    for i in file_list:
        t_list = i.split('/')
        path = pathlib.Path(os.path.abspath(os.path.join(*t_list)))
        if path.exists() == False:
            ans = False
            break
    return ans

def Folders_Check(folder_list, create=False):
    if create:
        ans = []
    else:
        ans = True
    
    for i in folder_list:
        t_list = i.split('/')
        path = pathlib.Path(os.path.abspath(os.path.join(*t_list)))
        if (os.path.isdir(path) == False):
            if create:
                os.mkdir(path)
                ans.append(path)
            else:
                ans = False
                break
    return ans