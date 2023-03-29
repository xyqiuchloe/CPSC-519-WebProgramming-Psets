
'''
This module helps set up the server side
'''
from os import name
from sys import argv, stderr
import sys
from socket import socket, SOL_SOCKET, SO_REUSEADDR
import pickle
import argparse
from table import Table
import filters_detail
import filters_obj


DATABASE = 'file:lux.sqlite?mode=ro'
MIN_PORT = 0
MAX_WID = 10000
OBJECT = "object"
DETAIL = "detail"

def data_process(table):
    '''
    This function stores the table information.
    '''
    temp = []
    # print(table)
    for row in table:
        temp.append(row)
        print(row)
    return temp

def show_dialog(tables): # can do unit test
    '''
    This function shows dialog of the object.
    '''
    temp = ""
    for i, ele in enumerate(tables):
        if i == 0: # object info index
            temp += "         Object Information\n\n-------------------------------\n\n"
        elif i == 1: # produce_by index
            temp += "         Produced By\n\n-------------------------------\n\n"
        elif i == 3: # info index
            temp += "         Information: \n\n-------------------------------\n\n"
        temp += ele.__str__() + "\n\n"
    return temp



def handle_client(sock):
    '''
    This function handles the client request.
    '''
    flo = sock.makefile(mode = 'rb')
    options = pickle.load(flo)
    # print(options)
    if options[0] == OBJECT:
        options = options[1]
        # print(options)
        filters = filters_obj.filter_term2(*options)
        table = Table(filters_obj.HEADER, filters_obj.get_filtered_objects(filters, DATABASE),
                      preformat_sep = filters_obj.FORMAT_SEP, max_width = MAX_WID, is_object = True)
        print(filters_obj.get_filtered_objects(filters, DATABASE))
        table = data_process(table)

    elif options[0] == DETAIL:
        options = options[1]
        tables = filters_detail.object_details(int(options))
        table = show_dialog(tables)
    flo = sock.makefile(mode='wb')
    pickle.dump(table, flo)
    flo.flush()
    print('Wrote table to client')


#-----------------------------------------------------------------------

def main():
    '''
    This function is server side of our program.
    '''
    parser = argparse.ArgumentParser(allow_abbrev=False,
                                     description = "Server for the YUAG application")
    parser.add_argument("integer",metavar = "port",
                        help = "the port at which the server is listening")

    if len(argv) != 2:
        print(f'Usage: python {argv[0]} port')
        sys.exit(1)

    try:
        port = int(argv[1])
        server_sock = socket()
        print('Opened server socket')
        if name != 'nt':
            server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 0)
        server_sock.bind(('', port))
        print('Bound server socket to port')
        server_sock.listen()
        print('Listening')
        while True:
            try:
                sock, client_addr = server_sock.accept()
                with sock:
                    print('Accepted connection')
                    print('Opened socket')
                    print('Server IP addr and port:',
                        sock.getsockname())
                    print('Client IP addr and port:', client_addr)

                    handle_client(sock)
            except Exception as ex:
                print(ex, file=stderr)
    except Exception as ex:
        print(ex, file=stderr)
        sys.exit(1)

#---------------------------------------------------------------------


if __name__ == '__main__':
    main()
