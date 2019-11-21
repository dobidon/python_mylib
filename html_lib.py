# -*- coding: utf-8 -*-

import os
import re

from file_manager import Create_My_File
import dict_manager as dctm

#def Read_HTML_Template(file_path, html_keys, encoding='iso-8859-9'):
#    html_out = []
#    for i in html_keys:
#        html_out.append('')
#    
#    t_switch = 0
#    
#    f = open(file_path, 'r', encoding=encoding)
#    for x in f:
#        t_pass = False
#        for i in html_keys:
#            if (x.find(i) != -1):
#                t_switch = html_keys.index(i)
#                t_pass = True
#                break
#        if not(t_pass):
#            html_out[t_switch] += x
#    f.close()
#    return html_out

##############################################

def Fill_Templates(dictionary, method='replace'):
    dict_tpl = dictionary.get('template')
    dict_val = dictionary.get('value')
    if dict_tpl == None or dict_val == None:
        return
    if len(dict_val) and (method != 'add'):
        return
    
    t_keys = dctm.dict_keys_get(dictionary, ['value','template'])
    t_val = dict_tpl
    
    # Iterate every key except value and template. These keys are holders of 
    # replacements
    #
    for key in t_keys:
        subdict = dictionary[key]
        if not(isinstance(subdict, dict)):
            pass
        if (subdict.get('template') != None):
            Fill_Templates(subdict, method='replace')
        t_val = t_val.replace(key, subdict['value'])
    
    if method == 'replace':
        dictionary['value'] = t_val
    elif method == 'add':
        dictionary['value'] += t_val
    return dictionary['value']

def Create_HTML_Page(html_page, html_name):
    file_path = Create_My_File(html_name,  html_page)
    html_path = 'file://' + file_path
    return html_path

def Read_HTML_Template(file_path, encoding='utf-8', sections=None):
    """Read an HTML Template file from `file_path` with an `encoding`.

    Description
    --------
    This function reads an HTML Template file structured as an example below:
    
    # An HTML Template File Structure:
        <!--/HTML_HEAD-->\n
        <!--./HOLDER_1,HOLDER_2-->\n
        <html>\n
            <head><style>\n
                .my_div\n
                {\n
                   width:HOLDER_1;\n
                   height:HOLDER_2;\n
                }\n
            <style></head>\n
        <!--/HTML_BODY-->\n
        <!--./DIV_1-->\n
        <body>\n
            DIV_1\n
        </body>\n
        <!--DIV_1-->\n
        <!--./CLASS_1,TEXT_1-->\n
                <div class="CLASS_1">TEXT_1</div>\n
        <!--/HTML_END-->\n
        </html>
    
    # Holder Tree:
        HTML_HEAD\n
            |----HOLDER_1\n
            |----HOLDER_2\n
        HTML_BODY\n
            |----DIV_1\n
                |----CLASS_1\n
                |----TEXT_1\n
        HTML_END\n
    
    # How the placeholders works:
        1. In an HTML Template File placeholders are defined as HTML Comment Lines.
        The root placeholders are defined starting with '/' before them like a 
        linux file system.:\n
            <!--/HTML_HEAD-->
        2. Placeholders can include nested placeholders with './' inside a 
        previous defined placeholder:\n
            <!--./HOLDER_1-->
        3. Multiple non-root placeholders can be defined separated with comma:\n
            <!--./HOLDER_1,HOLDER_2>\n
        3.1 After defining the placeholders, content of the placeholder can 
        be written:\n
           <html>\n
               <head><style>\n
                    .my_div\n
                    {\n
                       width:HOLDER_1;\n
                       height:HOLDER_2;\n
                    }\n
                <style></head>\n
        4. Inside a created nested placeholder, new placeholders can be 
        included after navigating to that created placeholder.:\n
            <!--/HTML_BODY-->\n
            <!--./DIV_1-->\n
            <body>DIV_1</body>\n
        - Navigation:\n
            <!--DIV_1-->\n
        - Creating nested placeholders:\n
            <!--./CLASS_1,TEXT_1-->\n
                <div class="CLASS_1">TEXT_1</div>\n
        5. Navigating to an earlier created placeholder is possible analog to 
        linux file system:\n
        - Navigating to the holder:\n
            <!--/ROOT_HOLDER_1/HOLDER_2-->
    
    # Output:
        After reading the file, a dictionary tree with placeholders created:\n
            dict{\n
                value: '',\n
                template: 'HTML_HEADHTML_BODYHTML_END',\n
                'HTML_HEAD': {\n
                              value: '',\n
                              template: '<html>\n
                                         <head><style>\n
                                            .my_div\n
                                            {\n
                                               width:HOLDER_1;\n
                                               height:HOLDER_2;\n
                                            }\n
                                         <style></head>',\n
                              'HOLDER_1': {'value': ''}\n
                              'HOLDER_2': {'value': ''}\n
                              }\n
            }

    Arguments
    --------
        file_path: Path to the template
            Template
        encoding: Encoding of the file
            Default is 'utf-8'.
            If 'tr' as encoding given, 'iso-8859-9' will be used.
        sections: HTML Template Sections
            Default is 'None'.
            If HTML Template is written as sections without tree structure,
            use this argument to pass the keys to the sections as a list.
    """

    if encoding == 'tr':
        encoding = 'iso-8859-9'
    # If list of sections were given read the sections separated
    # and return as a list.
    #
    if isinstance(sections, list):
        res_temp = []
        for i in sections:
            res_temp.append('')
        
        t_switch = 0
        
        f = open(file_path, 'r', encoding=encoding)
        for x in f:
            t_pass = False
            for i in sections:
                if (x.find(i) != -1):
                    t_switch = sections.index(i)
                    t_pass = True
                    break
            if not(t_pass):
                res_temp[t_switch] += x
        f.close()
        
    # Read it in dictionary mode
    #
    else:
        # Dictionary to be returned
        #
        res_temp = {'value': ''}
        
        # Pattern for HTML Comment (<!--Comment-->)
        #
        base_ptrn = '(?<=<!--)( *[a-zA-Z0-9_/.,]+ *)(?=-->)'# (\w+)
        ptrn = re.compile(base_ptrn)
        
        # Pointer to the current dictionary writing position
        #
        p_key = res_temp
        
        f = open(file_path, 'r', encoding='iso-8859-9')
        for line in f:
            res = ptrn.findall(line)
            
            # If key is available: <!--...-->
            #
            if len(res) == 1:
                
                # KEY or ./KEY or ...
                #
                res = res[0].strip()
                res_split = res.find('/')
                
                if res.startswith('./'):
                    res = res.replace('./', '').split(',')
                    for i in res:
                        if p_key.get(i) == None:
                            p_key[i] = {'value': ''}
                
                # /KEY/SUBKEY or KEY/SUBKEY
                #
                elif res_split != -1:
                    if res_split == 0:
                        # Return to root
                        #
                        p_key = res_temp
                    
                    res = re.findall('(?<=/).+', res)
                    res = res[0].split('/')
                    for i in res:
                        if p_key.get(i) != None:
                            p_key = p_key[i]
                        else:
                            if res.index(i) < len(res) - 1:
                                return None
                            else:
                                p_key[i] = {'value': '',
                                            'template': ''}
                                p_key = p_key[i]
                # KEY
                #
                else:
                    # Key available, navigate to it and add a template key
                    #
                    if p_key.get(res) != None:
                        p_key = p_key[res]
                        p_key['template'] = ''
                        
            # If no key is present, concatenate the template to the dictionary
            #
            else:
                if p_key != None:
                    p_key['template'] += line
                
        f.close()
        
        keys = dctm.dict_keys_get(res_temp, ignore=['value'])
        if len(keys):
            res_temp['template']=''
            for k in keys:
                res_temp['template'] += k
    
    return res_temp

if __name__ == '__main__':
    print('Running as the main...')
    path = Read_HTML_Template(os.path.join('html','template','html_template.html'))
    print('End')