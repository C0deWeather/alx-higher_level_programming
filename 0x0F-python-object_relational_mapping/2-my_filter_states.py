#!/usr/bin/python3
"""This module retrieves data from the states table in a mysql database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]
    try:
        db_obj = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            database=db_name)
        cur = db_obj.cursor()
        query = "select * from states where binary name = '{}'".format(state)
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        pass
    cur.close()
    db_obj.close()
