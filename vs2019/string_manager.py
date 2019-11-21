import re

# Split name to words(space as seperator) and reconstruct them 
# back properly with only one space between words.
# E.g: From '  AB  CD ' to 'AB CD'
#
def Purge_Space(var_text):
    # Split name to words(space as seperator) and clone them into 
    # the list below
    #
    word_list = []
    word_list = re.findall(r'\S+', var_text)
    words_out = ''
    
    for w in word_list:
        t_word = w.strip()
        if t_word[0].isalpha():
            words_out += t_word
            if word_list.index(w) < (len(word_list) - 1):
                words_out += ' '
    
    # Error checking
    #
    if (int(len(words_out)) > 0):
        for t_letter in words_out:
            if (t_letter.isalpha()):
                return words_out
    return None

def First_Words(inp_lines):
    # For every information (District, Address and Phone) on the list
    #
    for i in inp_lines:
        # For every letter in the information (District)
        #
        for j in i:
            # If the letter is alphabetic
            #
            if (j.isalpha()):
                # From '  AB  CD ' to 'AB CD'
                #
                words = Purge_Space(i)
                return words
    return None
