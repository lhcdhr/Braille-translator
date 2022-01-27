# COMP 202 Assignment 2 Part 3
# Author: Haochen Liu
# Student ID: 260917834

import doctest

INCOMPLETE = -1


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. Provided to students. Do not edit this function.

    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    TODO: For students to complete.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    '''
    binary = ''
    for i in range(1,9):
        if str(i) in s:
            binary = binary+'1'
        else:
            binary = binary+'0'

    return binary


def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    TODO: For students to complete.

    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    '''
    s = s[::-1]         #reverse the string
    s= hex(int(s,2))    #convert the string from binary to hex
    s= int(s,16)+int('2800',16) #add 2800 in base 16 but express in decimal
    s = hex(s)[2:]              #show this string x without the 0x which stands in position 0 and 1
    return s


def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    Provided to students. Do not edit this function.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    TODO: For students to complete.

    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''


    
    # for all the given s, first to check its length.
    #Only the s with length 8 or 11 can work. Return False for the rest cases.
    
    if len(s)==8:
    # check each part of the s to see if it follows the format.
    # Return False if the parameter does not meet the requirement of the o-string format.
        if s[0:2]=='oo' or s[0:2]=='o.' or s[0:2]=='.o'or s[0:2]=='..':  

            if s[2]=='\n':

                if s[3:5]=='oo' or s[3:5]=='o.' or s[3:5]=='.o'or s[3:5]=='..':

                    if s[5]=='\n':

                        if s[6:8]=='oo' or s[6:8]=='o.' or s[6:8]=='.o'or s[6:8]=='..':

                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:

            return False
        


    elif len(s)==11:  # same structure for s with length 11, check each part to see if it follows the format.


        if s[0:2]=='oo' or s[0:2]=='o.' or s[0:2]=='.o'or s[0:2]=='..':

            if s[2]=='\n':

                if s[3:5]=='oo' or s[3:5]=='o.' or s[3:5]=='.o'or s[3:5]=='..':

                    if s[5]=='\n':

                        if s[6:8]=='oo' or s[6:8]=='o.' or s[6:8]=='.o'or s[6:8]=='..':

                            if s[8]=='\n':

                                if s[9:11]=='oo' or s[9:11]=='o.' or s[9:11]=='.o'or s[9:11]=='..':

                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:

            return False
        
    else:

        return False



def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode

    TODO: For students to complete.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    '''
    if is_ostring(s) == True:    # to see if s is following the format of o-string properly
        unicode=hex_to_unicode((binary_to_hex(raisedpos_to_binary(ostring_to_raisedpos(s)))))
        # the steps to convert ostring to unicode
        return unicode  # return the result we get
    else:
        return s # if s does not follow the format, return s as it was.


if __name__ == '__main__':
    doctest.testmod()
