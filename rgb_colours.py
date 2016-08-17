# This program knows about the frequencies of various FM radio stations in
# London.
#
# Usage:
#
# $ python radio_freq.py [station_name]
#
# For instance:
#
# $ python radio_freq.py "Radio 4"
# You can listen to Radio 4 on 92.5 FM
#
# or:
#
# $ python radio_freq.py "BBC Radio 5"
# I don't know the frequency of BBC Radio 5

import sys

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]
col_dict = {}

for item in colours:
    key = item[0]
    value = item[1]
    col_dict[key] = value


col_name = sys.argv[1]


hexcode = None

# for key, value in col_dict.items():
    # if value == col_name:
        # hexcode = key
        # break

print (col_dict[col_name])


# if frequency:
    # print("YOu can listen to {} on {}".format(station_name, frequency))

# else:
    # print("I know nothing about this")


# print('I know about {} FM radio stations'.format(len(fm_frequencies)))

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that if the radio station is not found, the user is
#   given a list of all stations that the program does know about.
# * Change the program so that if it is called without arguments, a table of
#   all radio stations and their frequencies is displayed.
