import string
def check_pass(pswd):
    a=None
    if len(pswd)==8:
        flag_digits=False
        flag_punctuation=False
        flag_islower=False
        flag_isupper=False
        flag_valid=True
        flag_unique=False
        for elem in pswd:
            if elem.isnumeric():
                flag_digits=True
            if elem.islower():
                flag_islower = True
            if elem.isupper():
                flag_isupper = True
            if elem in '*-#':
                flag_punctuation = True
            if not (elem in string.ascii_letters or elem.isdigit() or elem in '*-#'):
                flag_valid = False

        if len(set(pswd))>5:
            flag_unique =True
        if flag_digits==flag_islower==flag_isupper==flag_punctuation==flag_valid ==flag_unique ==True:
            a='Пароль идеален'
        elif flag_digits==False:
            a='Пароль должен содержать числа'
        elif flag_islower == False:
            a='Пароль должен содержать строчные буквы'
        elif flag_isupper == False:
            a='Пароль должен содержать заглавные буквы'
        elif flag_punctuation == False:
            a='Пароль должен содержать специальный символы *-#'
        elif flag_valid == False:
            a = 'Пароль может содержать только латинские буквы, цифры или специальные символы *-#'
        elif flag_unique== False:
            a = 'Пароль должен содержать более 6 уникальных символов'
    if len(pswd) < 8:
        a='Пароль ненадежный'
    if len(pswd) > 8:
        a='Пароль трудно запомнить'
    return a



