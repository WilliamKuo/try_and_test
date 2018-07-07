import sys
import json
import hashlib
import random
import MySQLdb
import names


def version(db):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()

    return "Database version : {} ".format(data)

    

def create_table(db, tbl_name):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS {}".format(tbl_name))
    
    # Create table as per requirement
    sql = """CREATE TABLE {} (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )""".format(name)
    
    cursor.execute(sql)
    
    return True


def insert_test(db, tbl_name):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = '''INSERT INTO {tbl_name} (FIRST_NAME,
	   LAST_NAME, AGE, SEX, INCOME)
	   VALUES ("{name_f}", "{name_l}", {age}, "{sex}", {income})'''.format(
           tbl_name=tbl_name,
           name_f = names.get_first_name(),
           name_l = names.get_last_name(),
           age = random.randint(0, 100),
           sex = 'M' if random.randint(0, 1) == 1 else 'F',
           income = random.randint(0, 10000),
           )
    print sql
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except Exception as e:
        print 'bad happen {}'.format(e)
        # Rollback in case there is any error
        db.rollback()

def read_test(db, name_tbl):
    cursor = db.cursor()
    sql = "SELECT * FROM {} WHERE INCOME > '1000'".format(name_tbl)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # Now print fetched result
            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
 		 (fname, lname, age, sex, income )
    except Exception as e:
        print "Error: unable to fecth data {}".format(e)


def update_test(db, name_tbl):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to UPDATE required records
    sql = "UPDATE {} SET AGE = AGE + 1 WHERE SEX = 'M'".format(name_tbl)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()


def delete_test(db, name_tbl):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM {} WHERE AGE > 20".format(name_tbl)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()


# main
# ==============================================
E = 'employee'

# Open database connection
db = MySQLdb.connect("test.chnirgsttdpd.ap-northeast-1.rds.amazonaws.com","admin","adminadmin","testdb" )

# create_table(db, E)

# print version(db)

if 1==1:
    for _ in xrange(10):
	insert_test(db, E)

# read_test(db, E)

# update_test(db, E)

# delete_test(db, E)

# disconnect from server
db.close()

# ==============================================

