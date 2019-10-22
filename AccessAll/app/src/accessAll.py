import os
import time 
import datetime
from datetime import date, datetime, timedelta
import mysql.connector                                        


#FUNCTION THAT CHECKS WETHER TABLE 'table' exists.
def notExistTable(cursor,table):
    _SQL = """SHOW TABLES"""
    cursor.execute(_SQL)
    results = cursor.fetchall()

    #print('All existing tables:', results) # Returned as a list of tuples

    results_list = [item[0] for item in results] # Conversion to list of str

    if table in results_list:
        return False
    else:
        return True
                                                  


notAvailable=True;
while notAvailable:
    try:
        USER = os.getenv('MYSQL_USER', 'user')
        PW = os.getenv('MYSQL_PASSWORD', 'confluent')
        HOST = os.getenv('MYSQL_HOST','mysql-python')
        DB = os.getenv('MYSQL_DATABASE','connect_test')
        cnx = mysql.connector.connect(user=USER, password=PW, host=HOST, database=DB)
        notAvailable=False
    except:
        print("Mysql connection not available");
        time.sleep(30)


cursor = cnx.cursor()




TABLES_NAMES = os.getenv('SINK_TOPICS',' ')
print ('READING TOPICS: ',TABLES_NAMES)

TABLES = TABLES_NAMES.split(',')

while True:
    for table in TABLES:
#        print('Accessing table: ',table)
        if notExistTable(cursor,table):
#            print ('   it does not exist')
            continue

        query = ("SELECT * from " + table)    
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print (row)

cursor.close()
cnx.close()
