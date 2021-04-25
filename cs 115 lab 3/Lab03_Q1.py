def is_vowel(string):
    """takes a string as input and return True if the string has a vowel"""
    for i in string:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            return True
        else:
            return False


"""return: if string has a vowel return True (bool)
if not return False (bool)"""

"""calculate how number of vowels in the string"""


def count_vowels(string):
    number_of_vowels = 0
    for i in string:
        if (is_vowel(i)):
            number_of_vowels += 1
    print('There are {} number of vowels'.format(number_of_vowels))


"""takes a string and if string has all vowel return True 
otherwise return False"""


def all_vowels(string):
    for i in string:
        if (is_vowel(i)):
            if (i not in ('a' and 'e' and 'i' and 'o' and 'u')):
                return False
            else:
                print('All Vowels exist in the given string')
                return True


"""takes a string and prints all the vowels in the string
parameter:string
parameter type:string
return:vowels(string)"""


def display_which_vowels(string):
    vowels = ''
    for i in string:
        if (is_vowel(i)): 
            i=i.lower()
            if (i not in vowels):
                vowels += i
                print('"{}"'.format(i), 'exists in', '"{}"'.format(string))


"""takes a string and prints the vowels as capital letter
parameter:string
parameter and return type:string"""


def capitalize_vowels(string):
    new_str = ''
    for letter in string:
        if (is_vowel(letter)):
            new_str += letter.upper()
        else:
            new_str += letter
    print('New String:', new_str)


string = input('Enter a string:')
count_vowels(string)
all_vowels(string)
display_which_vowels(string)
capitalize_vowels(string)