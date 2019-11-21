# -*- coding: utf-8 -*-

import configparser

def Config_Get(file_name="config.ini", encoding='utf-8'):
    if (encoding == 'tr'):
        encoding = 'iso-8859-9'
        
    # Load the configuration file
    f = open(file_name, 'r', encoding=encoding)
    sample_config = f.read()
    config = configparser.RawConfigParser(allow_no_value=True)
#    config.readfp(sample_config)
    config.read_string(sample_config)
    f.close()
    
    return config

if __name__ == "__main__":
    
    # Load the configuration file
    #
    config = Config_Get("config.ini")
    
    # List all contents
    #
    print("List all contents")
    for section in config.sections():
        print("Section: %s" % section)
        for options in config.options(section):
            print("x %s:::%s:::%s" % (options,
                                      config.get(section, options),
                                      str(type(options))))
    # Print some contents
#    print("\nPrint some contents")
#    print(config.get('other', 'use_anonymous'))  # Just get the value
#    print(config.getboolean('other', 'use_anonymous'))  # You know the datatype?