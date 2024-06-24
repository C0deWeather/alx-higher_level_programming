#!/usr/bin/python3
"""This module connects to a mysql database
a makes a query to retrieve data"""
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db_obj = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            database=db_name)
        cur = db_obj.cursor()
        cur.execute("select * from states")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        pass
    cur.close()
    db_obj.close()


if __name__ == "__main__":
    main()
