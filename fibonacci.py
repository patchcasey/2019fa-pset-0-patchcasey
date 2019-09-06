#!/usr/bin/env python3

########################################################################################################################
# Code for CSCI-e-29: Pset0, relating to Fibonacci questions
# Submitted by Casey Patch on 9/4/2019
########################################################################################################################

def last_8(some_int):
    """return last 8 of an integer

    :param some_int: int
    :return: int
    """
    return int(str(some_int)[-8:])

def optimized_fibonacci(f):
    """calculate f-th member of the fibonacci sequence

    :param f: int
    :return: int
    """
    sequence_instance = [0, 1]
    first = sequence_instance[0]
    second = sequence_instance[1]

    # Error Handling
    if f < 0:
        print("Incorrect input")
    elif f == 0:
        return first
    elif f == 1:
        return second

    # Main function iterating through range
    else:
        for i in range(1, f):
            c = first + second
            first = second
            second = c
        return second


class SummableSequence(object):
    """object to hold logic for generalized fibonacci sequence calculation"""

    def __init__(self, *initial):
        """initialization, includes error handling

        :param initial: iterable
        """
        if len(initial) != 3:
            raise TypeError(initial, 'is not of correct length!')
        #TODO - iterate over each and make sure it's an integer
        self.initial = initial
        self.first = self.initial[0]
        self.second = self.initial[1]
        self.third = self.initial[2]

    def __call__(self, i):
        """main function to calculate i-th member of "n=3 fibonacci"

        :param i: int
        :return: int
        """
        assert isinstance(i, int)
        if i < 0:
            print("Incorrect input")
        elif i == 0:
            return self.first
        elif i == 1:
            return self.second
        elif i == 2:
            return self.third

        # Main logic calculating generalized fibonacci number (n = 3)
        else:
            for i in range(2, i):
                c = self.first + self.second + self.third
                self.first = self.second
                self.second = self.third
                self.third = c
            return self.third


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))