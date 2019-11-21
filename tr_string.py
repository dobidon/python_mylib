import warnings

# Changes the cases of the letters in the string along Turkish characters
#
# @param inp[in]    : Input
# @param case[in]   : Case, in which the letters are going to be 
#                     ('lower' or 'upper'). Default is 'lower'.
#
# @return           : Converted input
#
# Prototype         : TR_Case_Change('ŞİŞ BIÇAĞI') -> 'şiş bıçağı'
#                   : TR_Case_Change('çığ şütlaç', case='upper')
#                     -> 'ÇIĞ SÜTLAÇ'
#
def TR_Case_Change(inp, case='lower'):
    if (not(len(inp) > 0) or (inp == None) or ((case != 'upper') and \
                                              (case != 'lower'))):
        return None
    
    tr_map = 'ÇĞIİÖŞÜçğıiöşü'
    
    if (case == 'lower'):    
        for i in range(0, int(len(tr_map)/2)):
            inp = inp.replace(tr_map[i], tr_map[int(i+(int(len(tr_map))/2))])
        inp = inp.lower()
    elif (case == 'upper'):
        for i in range(0, int(len(tr_map)/2)):
            inp = inp.replace(tr_map[int(i+(int(len(tr_map))/2))], tr_map[i])
        inp = inp.upper()
    return inp

# Change Turkish characters to their English equalavalent
#
# @param inp[in]    : Input
# 
# @return           : Converted input
#
# Prototype         : TR_to_EN('FIşğÇö') -> 'FIsgCo'
#
def TR_to_EN(inp, case=None):
    if (not(len(inp) > 0) or (inp == None)):
        return None
    
    tr_en_map = 'çğıöşüÇĞİÖŞÜcgiosuCGIOSU'

    for i in range(0, int(len(tr_en_map)/2)):
        bol = tr_en_map[i] in inp
        if (bol == True):
            inp = inp.replace(tr_en_map[i], tr_en_map[int(i+(int(len(tr_en_map))/2))])
    
    if case != None:
        if case == 'lower':
            inp = inp.lower()
        elif case == 'upper':
            inp = inp.upper()
        else:
            warnings.warn("\nUnidentified parameter case. "
                          "Available parameters for case: 'upper', 'lower'.\n"
                          "Returning without casing.")
    return inp