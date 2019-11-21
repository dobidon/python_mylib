# -*- coding: utf-8 -*-

from pathlib import Path
import subprocess

def Sh_Script_Write(scr_path, scr_lines):
    """Write `scr_lines` to the `scr_path`.
    
    Arguments
    --------
        scr_path: Path to Script
            If path exists, it will be deleted before
        scr_lines: File lines
            Lines to be written on the file
    """
    path = Path(scr_path)
    if path.exists() == True:
        subprocess.run(['rm', scr_path])
        
    f=open(scr_path, 'w')
    for i in scr_lines:
        f.write(i+'\n')
    f.close()
    
    scr_path = '"' + scr_path + '"'
    if scr_path.endswith('.sh'):
        subprocess.run(['chmod', '+x', scr_path])
    elif scr_path.endswith('.py'):
        scr_path = 'python3 ' + scr_path
    
    return scr_path