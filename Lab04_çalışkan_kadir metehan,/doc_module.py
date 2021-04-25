

def isAllLetter(string):
    """


    Parameters
    ----------
    string
    take a string and check all index in string

    Returns
    -------
    bool
        if string include only letter return True, otherwise False

    """

    alphabet = 'qwertyuıopasdfghjklzxcvbnm'
    for i in string:
        if i not in alphabet:
            return False
    return True


def pluralizeWord(string):
    """


    Parameters
    ----------
    string : 
        take a string and if the string's last index is 'y', replace it with 'ies'. Otherwise, just add 's'

    Returns
    -------
    string : 
        return the plural form of words.

    """

    if (isAllLetter(string)):
        if (string[-1] == 'y'):
            string = string[:-1]
            string = string + 'ies'
        else:
            string = string + 's'
        return string


def pluralizeAllWords(filename):
    """


    Parameters
    ----------
    filename : string
        take a input of filename.Read the file and check all line in file, put the all line in pluralizeword function respectively.Also, create new file and save the all plural words in new file and give the percentage how many lines was pluralized

    Returns
    -------
    None.

    """

    file = open(filename, "r")
    new_file = open('pluralWordList.txt', 'w')
    number_words = 0
    a = ''
    number_plural_words = 0
    for line in file:
        number_words += 1
        new_line = line.replace('\n', '')
        if (isAllLetter(new_line)):
            number_plural_words += 1
            a += (pluralizeWord(new_line) + '\n')
    new_file.write(a)
    new_file.write('{:.2f} % of the words are pluralized'.format((number_plural_words / number_words) * 100))
    new_file.close()
