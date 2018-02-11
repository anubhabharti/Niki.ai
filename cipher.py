# -*- coding: utf-8 -*-
"""
Author : Anubha Bharti 

"""


def cipher(p, q):
    """Return cipher

    :param p: int, number to be ciphered
    :param q: int, number to be ciphered
    :return: None, prints ciphered alphabet
    """
    try:
        for i in range(p, (q+1)):
            div = i
            string = ""
            while div > 0:
                mod = (div-1)%26
                string = chr(65+mod)+string
                div = int((div-mod)/26)
            print string
        return None
    except Exception as e:
        print " Encountered error when ciphering. Aborting !!! Error: {}".format(e)


if __name__ == "__main__":
    try:
        m, n = [int(x) for x in raw_input("Enter values of m & n here: ").split()]
        cipher(m, n)

    except Exception as e:
        print " Failed !!! Error: {}".format(e)


