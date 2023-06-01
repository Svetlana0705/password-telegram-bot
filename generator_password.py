import random
import string

def generator_pswd():
    pswd=''
    length=random.randint(5,15)
    variants=string.ascii_letters+'0123456789'+'*-#'
    for _ in range(length):
        pswd+=random.choice(variants)

    return pswd

