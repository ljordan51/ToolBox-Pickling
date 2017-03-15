""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    count = 0  # default count is 0, this way all files will be incremented by 1
    # if the file doesn't exist, it will create one and dump the default count in
    if not exists(file_name):
        fin = open(file_name, 'wb')
        dump(count, fin)
        fin.close()
    # if reset is false, the function must first read and load the current counter value
    if not reset:
        fin = open(file_name, 'rb')
        count = load(fin)
        fin.close()
    # in all cases, the counter value is now ready to be incremented by 1 and dumped back into the file
    fout = open(file_name, 'wb')
    dump(count+1, fout)
    fout.close()
    return count+1  # returns the current count for the file


if __name__ == '__main__':
    if len(sys.argv) < 2:  # if there are no input args then the doctest is run
        import doctest
        doctest.testmod(verbose=True)
    else:
        file_name = sys.argv[1]
        reset = False  # by default reset is false
        if len(sys.argv) == 3:
            if sys.argv[2].lower() == 'true':  # if second arg input string is true then reset is changed to True
                reset = True
        print("new value is " + str(update_counter(file_name, reset)))
