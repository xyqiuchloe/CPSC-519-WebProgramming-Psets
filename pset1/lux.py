"""
This module rovides a command-line interface for displaying
a table of objects filtered by department, agent, classification, 
and title. The functions used for searching art information 
based on sqlite library are imported from filters_obj.py.
Usage:
    python lux.py [-h] [-d dep] [-a agt] [-c cls] [-l label]
"""
import argparse
import sys
import filters_obj



def main():
    """ Function for standard input """
    parser = argparse.ArgumentParser(allow_abbrev=False)
    #parser.add_argument('-d'#option that takes a value, metavar='dep'#)
    parser.add_argument("-d", metavar = "dep",
    help = "dep show only those objects whose department label contains department")
    parser.add_argument("-a", metavar = "agt",
     help = "agt show only those objects produced by an agent with name containing agentname")
    parser.add_argument("-c", metavar = "cls",
     help = "cls show only those objects classified with a classifier having a name containing cls")
    parser.add_argument("-l", metavar = "label",
    help = "label show only those objects whose label contains label")
    try:
        args = parser.parse_args()
    except SystemExit:
        print("Please enter a valid command")
        sys.exit(1)
    arg_list = []
    if args.d:
        arg_list.append(["dep", args.d])
    if args.a:
        arg_list.append(["agt", args.a])
    if args.c:
        arg_list.append(["cls", args.c])
    if args.l:
        arg_list.append(["label", args.l])

    filters = filters_obj.filter_term2(*arg_list)

    filters_obj.get_filtered_objects(filters)






# ---------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
