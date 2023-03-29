"""
This module retrieves the detail of an object from a database and displays them 
in a formatted table. The function module defines a set of functions that
takes an integer ID parameter and displays the object's details with the matching
ID using SQL queries to extract data from the 'lux.sqlite' database.
The table.py module is imported to format and display the results in a readable way.
"""
import sys
from contextlib import closing
from sqlite3 import connect
from table import Table


# INITIALIZE CONSTANT
DATABASE = 'file:lux.sqlite?mode=ro'
FORMAT_FLAG = ["w", "w", "w", "w", "w", "p"] 
FORMAT_SEP = ","
HEADER = ["ID", "Label", "Produced By", "Date", "Member of", "Classified As"]


def filter_term2(*args): # args: eg.[["dep", "Yale Gallary"], ["agt", "Van Gogh"]]
    """ This function return the SQL command which is based on the command argument """
    string = ""
    temp = []
    # take the first having clause
    if len(args) > 0:
        temp.append(get_option_name(args[0][0]))
        string += f"HAVING {get_option_name(args[0][0])} like '%{args[0][1]}%' "
    # rest of having clause
    for i in range(1, len(args)):
        temp.append(get_option_name(args[i][0]))
        string += f"AND {get_option_name(args[i][0])} like '%{args[i][1]}%' "
    # order filter
    string += "ORDER BY label ASC, temp1.date ASC "
    if "agents_name" in temp:
        string += ", temp1.name ASC"
        temp.remove("agents_name")
    if "departments_name" in temp:
        string += ", departments_name ASC "
        temp.remove("departments_name")
    if "classifiers_name" in temp:
        string += ", classifiers_name ASC "
        temp.remove("classifiers_name")
    string += " limit 1000"

    return string

def get_option_name(string):
    """ This function return the options specified by user"""
    if string == "dep":
        return "departments_name"
    if string == "agt":
        return "agents_name"
    if string == "cls":
        return "classifiers_name"
    if string == "label":
        return "objects.label"




def get_filtered_objects(filters):
    """  This function takes a string as input and returns the corresponding option name 
    based on the string value. """
    database_url = DATABASE
    try:
        with connect(database_url, isolation_level=None,
        uri=True) as connection:

            with closing(connection.cursor()) as cursor: # cursor is an object which helps to execute the query and fetch the records from the database. 
                #The cursor plays a very important role in executing the query.

                stmt_str = f"""
                            select objects.id,  objects.label, group_concat(distinct (temp1.name || ' ('||temp1.part||')' )) as agents_name ,temp1.date, 
                                group_concat(distinct departments.name) as departments_name, group_concat(distinct temp2.name ) as classifiers_name
                        
                                from
                                (select o.id, p.part, a.name, o.date from
                                    objects  o
                                    left outer join productions p on p.obj_id = o.id
                                        left outer join agents a on a.id = p.agt_id        
                                    order by a.name  ) as temp1 
                                    
                                left join objects on objects.id = temp1.id
                                    left join objects_departments on objects_departments.obj_id = objects.id
                                        left join departments on departments.id = objects_departments.dep_id
                                
                                left join 
                                    (select o.id, lower(c.name) as name
                                        from objects o
                                        left outer join objects_classifiers oc on o.id = oc.obj_id
                                        left outer join classifiers c on oc.cls_id = c.id
                                        order by lower(c.name)) as temp2 on temp2.id = objects.id
                            
                            group by objects.id   {filters}"""

                cursor.execute(stmt_str)
                #cursor.execute(stmt_str,  {"st" : filter}) this prepare statement doesn't work

                row = cursor.fetchone()
                str_list = HEADER
                temp = []
                count = 0

                while row is not None:
                    row = list(row)
                    temp.append(row)
                    count += 1
                    row = cursor.fetchone()
                table = Table(str_list, temp, format_str = FORMAT_FLAG, preformat_sep = FORMAT_SEP)

                print(f"Search produced {count} objects")
                print(table)

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)
