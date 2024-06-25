#!/usr/bin/python3
"""This module retrieves cities by states
from the states table in a mysql database"""

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
        query = "select cities.name from cities\
                join states on cities.state_id = states.id\
                where binary states.name = %s"
        cur.execute(query, (state,))
        rows = cur.fetchall()
        if (not state or not cur.rowcount):
            print()
        i = 0
        for row in rows:
            i += 1
            for item in row:
                print(item, end=", ")
            if (i == cur.rowcount - 1):
                print(rows[i][0])
                break
    except MySQLdb.Error as e:
        pass

    cur.close()
    db_obj.close()
