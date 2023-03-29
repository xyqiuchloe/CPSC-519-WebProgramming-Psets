"""
This module provides a command-line interface for displaying details of an object 
in a database. The module requires the argparse function, sqlite database, and 
filters_detail.py to function properly.
"""
import argparse
import sys
import filters_detail

def main():
    """ Function for standard input """
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("integer",metavar = "id",
help = "the id of the object whose details should be shown")
    try:
        args = parser.parse_args()
    except SystemExit:
        print("Please enter a valid command")
        sys.exit(1)
    try:
        filters_detail.object_details(int(args.integer))
    except ValueError:
        print("Please enter a valid id number")



# ---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
 