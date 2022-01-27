# COMP 202 A2 Part 5
# Author: Haochen Liu
# Student ID 260917834

from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
# You may want to define more global variables here
NUM_FRONT = '\u283c'
NUM_END = '\u2830'


####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    # ADD CODE HERE
    
    text = whole_word_contractions(text)  # convert the whole words first because if two-letters are converted first, it will be overlapped
                                          # and the text will not be converted properly.
    text = two_letter_contractions(text)  # Convert two-letters after whole words.
    
    return text


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    
    # ADD CODE HERE
    count = 0

    for i in range(0,len(text)):
        if text[i] =='"':
            count+=1                    # the number of quotes appeared in the text
            if count%2==1:              # if it is the odd-order quote, replace it with “
                text = text[:i]+'“'+ text[i+1:]
            else:                       # if it is the even-order quote, replace it with ”
                text = text[:i]+'”'+ text[i+1:]
    return text
                
                


####################################################
# Put your own helper functions here!


def convert_question_mark(text):
    '''(str)->(str)
    Convert the question marks in French Braille to that in English Braille.
    >>> convert_question_mark('⠢')
    '⠦'
    >>> convert_question_mark('\u2820\u283f \u2829\u2801\u280f\u2811\u280e \u283e \u2809\u2815\u2807\u2833\u2817\u2822')
    '\u2820\u283f \u2829\u2801\u280f\u2811\u280e \u283e \u2809\u2815\u2807\u2833\u2817\u2826'
    >>> convert_question_mark('⠨⠁⠗⠑ ⠽⠕⠥ ⠨⠋⠗⠑⠝⠉⠓⠢ ⠨⠝⠕⠲ ⠨⠊ ⠁⠍ ⠨⠉⠓⠊⠝⠑⠎⠑⠲')
    '⠨⠁⠗⠑ ⠽⠕⠥ ⠨⠋⠗⠑⠝⠉⠓⠦ ⠨⠝⠕⠲ ⠨⠊ ⠁⠍ ⠨⠉⠓⠊⠝⠑⠎⠑⠲'
    '''

    
    for i in range(0,len(text)):    # going through every unicode in text
        if text[i] ==  '\u2822':    # look for the unicode of French question mark
            text = text[:i]+'\u2826'+text[i+1:] # convert it into English question mark and put it back
    return text

def convert_parenthese(text):
    '''(str)->(str)
    Convert the unicode expression of parenthesis in French to that in English.
    >>> convert_parenthese('\u2826\u2834')
    '\u2836\u2836'
    >>> convert_parenthese('⠦⠨⠝⠕⠲ ⠨⠊ ⠁⠍ ⠨⠉⠓⠊⠝⠑⠎⠑⠲⠴')
    '⠶⠨⠝⠕⠲ ⠨⠊ ⠁⠍ ⠨⠉⠓⠊⠝⠑⠎⠑⠲⠶'
    >>> convert_parenthese('⠶⠨⠉⠓⠊⠝⠑⠎⠑⠲⠦')
    '⠶⠨⠉⠓⠊⠝⠑⠎⠑⠲⠶'
    '''
    for i in range(0,len(text)):        # going through every unicode in text
        if text[i] == '\u2826' or text[i] == '\u2834':  # see if the code represents either of the parenthese
            text = text[:i]+'\u2836'+text[i+1:]   # convert it - since in English braille, the two parenthesis have same unicode.
    return text

def convert_quotation(text):
    '''(str)->(str)
    Convert the quotations into its unicode.
    >>> convert_quotation('“”')
    '⠦⠴'
    >>> convert_quotation('“⠨⠉⠓⠊⠝⠑⠎⠑⠲”')
    '⠦⠨⠉⠓⠊⠝⠑⠎⠑⠲⠴'
    >>> convert_quotation('“““⠨⠉⠓⠊⠝⠑⠎⠑⠲”')
    '⠦⠦⠦⠨⠉⠓⠊⠝⠑⠎⠑⠲⠴'
    '''
    for i in range(0,len(text)):        # going through every unicode in the text
        if text[i] == '“':              # since the quotes have already been converted by convert_quotes, we just need to find them in text
            text = text[:i]+'\u2826'+text[i+1:] # replace it with its unicode
        elif text[i]=='”':              # same for this one, just a different unicode
            text = text[:i]+'\u2834'+text[i+1:]
    return text



def english_number(text):
    '''(str)->(str)
    Convert the French braille expression of numbers in to English braille expression.
    >>> english_number('⠼⠁⠼⠃⠼⠉')
    '⠼⠁⠃⠉⠰'
    >>> english_number('⠼⠁ ⠼⠃ ⠼⠉')
    '⠼⠁⠰ ⠼⠃⠰ ⠼⠉⠰'
    >>> english_number('⠼⠁⠼⠃⠼⠉⠨⠉⠓⠊⠝⠑⠎⠑⠲')
    '⠼⠁⠃⠉⠰⠨⠉⠓⠊⠝⠑⠎⠑⠲'
    >>> english_number('⠨⠉⠓⠊⠝⠑⠎⠑⠲⠼⠁⠼⠃⠼')
    '⠨⠉⠓⠊⠝⠑⠎⠑⠲⠼⠁⠃⠼'
    >>> english_number('⠼⠁')
    '⠼⠁⠰'
    '''
    # My general idea of this function is to figure out all possible ways fora number to be in text.
    # For example, in the very end, a single number, and multiple numbers.
    # In that case, there several important branches that need to go through.

    paste=''                         # the string that will be used to place the converted text
    check=False 
    for i in range(len(text)-1): 
        if check == False:  
            if text[i]==NUM_FRONT:   # To check whether (a row of) number(s) starts.

                paste += text[i]     # if it is true, add ⠼
                check = True       

            else:                  
                paste+=text[i]       # if it is not a number, just add the character to paste.  
                

        else:                        # Go to this branch if check is True. This is for the cases when there are multiple numbers in a row.
            if text[i] == NUM_FRONT:  
                pass                 
            else:
                if text[i+1] != NUM_FRONT: # if the character after this one is not still ⠼, then this is the end of this set of number.
                    paste += text[i]+NUM_END  
                    check = False         # the convertion of this set of number is finished
                else:
                    paste += text[i]      # if is not either of those 2 cases above, then the character is a number.
                    check = True          # add it to paste, and check is True because we need to see the following ones 

    # since len(text)-1 is used in the previous part, the last character in text is overlooked. We need to add it back.                  
    if text[len(text)-2]!=NUM_FRONT:        # if it is not a number, then we just need to add the last character back. 
        paste += text[-1]  
    else:                                   # if the text in English ends with a number, then if the number is overlooked and ⠰ is not added.
        paste += text[-1]+NUM_END           # Then add that number and ⠰ back
    
    return paste


                
####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    # You may want to put code after this comment. You can also delete this comment.




    
    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text) 
    
    # You may want to put code after this comment. You can also delete this comment.
    text = convert_quotes(text) # convert quotes before converting parenthese to prevent overlap.





    
    # Run the text through the French Braille translator
    text = text_to_braille(text)
    
    # You may want to put code after this comment. You can also delete this comment.




    
    # Replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))
    
    # You may want to put code after this comment. You can also delete this comment.

    text = convert_parenthese(text) # convert them in this order to avoid overlap.

    text = convert_question_mark(text)

    text = convert_quotation(text)

    # convert numbers in the end because all counting in this functions are based on unicode rather than English letters.
    text = english_number(text)

    
    return text


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
