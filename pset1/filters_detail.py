"""

This module retrieves the details of an object from a database and displays them 
in a formatted table. The function 'object_details' takes an integer ID parameter 
and displays the object's details with the matching ID using SQL queries to 
extract data from the 'lux.sqlite' database. 

"""
import sys
from contextlib import closing
from sqlite3 import connect
from table import Table

# INITIALIZE CONSTANT

FORMAT_FLAG = ["w", "w", "p", "w"]
FORMAT_SEP = ","
LABEL = ["Label"]
PRODUCED_BY =  ["Part", "Name", "Nationalities", "Timespan"]
CLASSIFIERS = ["Classification"]
INFORMATION = ["Type", "Name"]
DATABASE = 'file:lux.sqlite?mode=ro'
BEGIN_DATE_IND = 3
END_DATE_IND = 4
BEGIN_BCE_IND = 5
END_BCE_IND = 6
TIMESPAN_IND = 3

# ----------------------------------------------------
def replace_null(lst):
    """ This function takes a 2D list as a parameter, 
        and replace the null element to empty for each element of the element in 2D list """
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] is None:
                lst[i][j] = ""

def print_output(query, header, cursor, is_agent = False):
    """ This function is a customize print function.
        If the flag is_agent is on, print the table with specific format"""
    cursor.execute(query)
    row = cursor.fetchone()
    list1 = []
    while row is not None:
        row = list(row)
        if is_agent:
            row = time_span(row)
        list1.append(row)
        row = cursor.fetchone()
    replace_null(list1)
    if is_agent :
        table = Table(header, list1, format_str = FORMAT_FLAG, preformat_sep = FORMAT_SEP)
    else:
        table = Table(header, list1)
    print(table)
    print()

def time_span(lst):
    """ This function extract the data and combine them into time span"""
    if lst[BEGIN_BCE_IND] == 1:
        lst[BEGIN_DATE_IND] = "-" + lst[BEGIN_DATE_IND] + " "
    if lst[END_BCE_IND] == 1:
        lst[END_DATE_IND] = " -" + lst[END_DATE_IND]
    if lst[BEGIN_DATE_IND] is None:
        lst[BEGIN_DATE_IND] = ""
    if lst[END_DATE_IND] is None:
        lst[END_DATE_IND] = ""
    lst[TIMESPAN_IND] = lst[BEGIN_DATE_IND] + "-" + lst[END_DATE_IND]
    return lst[:TIMESPAN_IND + 1]

# ----------------------------------------------------

def object_details(objects_id):
    """
    Retrieves and prints the details of an object with the given ID from art gallery database.

    Arguments:
    - objects_id: An integer representing the ID of the object to retrieve information for.

    Returns:
    - Details of the object to the console.

    Raises an exception and exits the program if there is an error connecting to or querying 
    the database.
    """
    database_url = DATABASE
    try:
        with connect(database_url, isolation_level=None,
        uri=True) as connection:

            with closing(connection.cursor()) as cursor:
                # Create a SQL query
                stmt_str = f"""
                            SELECT label FROM objects
                            WHERE objects.id = {objects_id}"""
                # label
                print_output(stmt_str, LABEL, cursor)
                # produce by
                stmt_str = f"""
                            SELECT part,
                                name,
                                group_concat(DISTINCT descriptor) AS descriptor,
                                strftime('%Y', begin_date) AS begin_date,
                                strftime('%Y', end_date) AS end_date,
                                begin_bce,
                                end_bce
                            FROM objects
                                JOIN
                                productions ON objects.id = productions.obj_id
                                LEFT JOIN
                                agents ON agents.id = productions.agt_id
                                LEFT JOIN
                                agents_nationalities an ON an.agt_id = agents.id
                                LEFT JOIN
                                nationalities n ON n.id = an.nat_id
                            GROUP BY agents.name,
                                    objects.id
                            HAVING objects.id= {objects_id}"""

                print("         Produced By")
                print("-------------------------------")
                print_output(stmt_str, PRODUCED_BY,cursor, True)
                # Classification
                stmt_str = f"""
                            SELECT lower(group_concat(DISTINCT cls.name))
                            FROM objects o
                                LEFT JOIN
                                objects_classifiers ocls ON ocls.obj_id = o.id
                                LEFT JOIN
                                classifiers cls ON cls.id = ocls.cls_id
                            WHERE o.id = {objects_id}"""

                print_output(stmt_str, CLASSIFIERS, cursor)
                # # Information
                stmt_str = f"""
                            SELECT type,
                                content
                            FROM objects o
                                LEFT JOIN
                                [references] r ON r.obj_id = o.id
                            where o.id = {objects_id}"""
                print("         Information: ")
                print("-------------------------------")
                print_output(stmt_str, INFORMATION, cursor)

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)
