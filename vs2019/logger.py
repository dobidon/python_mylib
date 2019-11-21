# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:42:06 2019

@author: omemi
"""

# -*- coding: utf-8 -*-

import os
from datetime import datetime
import traceback

from file_manager import Clean_Folder

def Exception_Log(dir_log, msg=None):
    '''
    Logs the exception with traceback in a log folder of the changing directory)
    
    Arguments
    ---------
    - msg:
        Error to be logged. Default is the traceback from exception
    - dir_log:
        Log directory relative to the function's start directory
    - return:
        Absolute path to the log file.
    '''
    dt_obj = datetime.now()
    log_file = dt_obj.strftime('ErrorLog_%Y-%m-%d__%H.%M.%S.log')
    
    if len(os.listdir(dir_log)) > 100:
        Clean_Folder(dir_log, 50)
    
    out = ''
    out += 'Date: ' + str(dt_obj.date()) + '\n'
    out += 'Time: ' + str(dt_obj.time()) + '\n'
    out += 'Date-time: ' + str(dt_obj) + '\n\n'
    
    if (msg == None):
        out += str(traceback.format_exc())
    else:
        out += msg
    
    cur_cwd = os.getcwd()
    os.chdir(dir_log)
    
    log_cwd = os.getcwd()
    logf = open(log_file, 'w')
    logf.write(out)
    logf.close()
    
    os.chdir(cur_cwd)
    return log_cwd + '/' + log_file

def Dict_to_XML(inp_dict, path, ids=False):
    '''
    Description
    -----------
    Converts `inp_dict` into pretty XML and saves it to `path`.

    Arguments
    -----------
    - inp_dict:
        Input dict
    - path:
        Path to the output XML file
    - ids:
        True: Elements in XML has unique id.
    '''
    import dicttoxml
    from xml.dom.minidom import parseString
    
    f = open(path, 'w')
    f.write(parseString(dicttoxml.dicttoxml(inp_dict, ids=ids)).toprettyxml())
    f.close()