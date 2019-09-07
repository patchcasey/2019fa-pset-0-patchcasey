#!/usr/bin/env python3
########################################################################################################################
# Code for CSCI-e-29 Pset0 relating to the pyramid question
# Submitted by Casey Patch on 9/4/2019
########################################################################################################################

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from math import ceil


def print_pyramid(rows):
    """Main start of function

    :param rows: int
    :return: None
    """
    # Count of number of dashes across pyramid structure
    columns = rows + rows - 1
    # Sequence of positions of dashes in pyramid
    sequence = list(range(columns))
    middle = ceil((len(sequence) - 1) / 2)
    position = []

    for i in range(0, rows):
        # Tip of pyramid will always have one =
        if i == 0:
            position.append(sequence.index(middle))

        # Append to list positions that should be = instead of -
        else:
            position.append(sequence.index(middle) - i)
            position.append(sequence.index(middle) + i)

        # Draw the pyramid, inserting = in indicated positions
        for j in range(0, columns):
            if j in position:
                print("=", end="")
            else:
                print("-", end="")

        print()


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
