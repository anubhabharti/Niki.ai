# -*- coding: utf-8 -*-
"""
Author : Anubha Bharti

"""


def sorting_list(in_list):
    try:
        return sorted(in_list, key=len)
    except Exception as e:
        print " Exception Encountered !! Error : {}".format(e)


if __name__ ==  "__main__":
    try:
        input_list = [x for x in raw_input("Please enter a string separated by spaces: ").split()]
        print sorting_list(input_list)
    except Exception as e:
        print " Exception Encountered in main. Erroneous Input !! Error : {}".format(e)
