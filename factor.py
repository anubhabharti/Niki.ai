# -*- coding: utf-8 -*-
"""
Author : Anubha Bharti
"""


def factor(n):
    """Return factor of number.

    :param n: int, number to be factorized
    :return: tuple, factors
    """
    try:
        factors = set()
        for i in xrange(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(int(n/i))
        return factors

    except Exception as e:
        print "Invalid Input. Error:{}".format(e)
        return -1


if __name__ == "__main__":
    try:
        factors_out = factor(int(raw_input("Enter an integer to factorize:")))

        if len(factors_out) > 1:
            print "Factors of entered number are:", sorted(factors_out)
        else:
            print "The Entered number is a prime number"
    except Exception as e:
        print "Failed to factorize, Erroneous Input. Error: {}".format(e)
