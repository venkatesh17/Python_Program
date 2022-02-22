"""
Find out the prime Numbers
"""


def prime_fun():
    v = 1010
    numprime = "Prime Number"
    for i in range(2, v-1):
        if v % i == 0:
            numprime = "Not Prime"

    result = str(v) + " is " + numprime

    return result
