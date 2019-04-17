import time 
import datetime
from datetime import date, datetime, timedelta
import mysql.connector                                        




#FUNCTION THAT CHECKS WETHER TABLE 'table' exists.
def notExistTable(cursor,table):
    _SQL = """SHOW TABLES"""
    cursor.execute(_SQL)
    results = cursor.fetchall()

    print('All existing tables:', results) # Returned as a list of tuples

    results_list = [item[0] for item in results] # Conversion to list of str

    if table in results_list:
        return False
    else:
        return True
                                                  

notAvailable=True
while notAvailable:
    try:
        #cnx = mysql.connector.connect(user='confluent', password='confluent', host='192.168.99.100', database='connect_test')
        cnx = mysql.connector.connect(user='confluent', password='confluent', host='mysql_python', database='connect_test')
        notAvailable=False
    except:
        print("Mysql connection not available");
        time.sleep(30)


cursor = cnx.cursor()

#*******************************#
#        CREATE TABLE           #
#*******************************#

#This table will become a topic in Kafka due to the Kafka JDBC Source Connector



#Define table structure
table_name = 'employees'
table_description = ("CREATE TABLE `employees` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


print("Creating table {}: ".format(table_name), end='')
try:
    print("Creating table {}: ".format(table_name), end='')
    #Create table
    cursor.execute(table_description)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
    else:
        print(err.msg)
else:
    print("OK")


#*******************************#
#        UPDATE TABLE           #
#*******************************#


#The tuples inserted in the table will become a message within topic in Kafka due to the Kafka JDBC Source Connector

add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")

d_date =  datetime.now()
tomorrow = d_date + timedelta(days=1)


data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))


cursor.execute(add_employee, data_employee)
cnx.commit()


#*******************************#
#         READ TABLE            #
#*******************************#


#A table ratings is expected. Whenever a My-TRAC module creates a topic "ratings" Kakfa JDBC Sink Connector will create 
#automatically a table called also ratings.
#To checck this part deploy My-TRAC and use CSVToKafkaTopic to load ratings3.csv. This will create a ratings topic within My-TRAC.


while notExistTable(cursor,"ratings"):
    print("Table ratings does not exist yet")
    time.sleep(30)


#QUERY TABLE
while True:
    query = ("SELECT user_id, activity_id, rating FROM ratings ")
    cursor.execute(query)
    for (user_id, activity_id, rating) in cursor:
        print("User {} rated activity {} with {}".format(user_id,activity_id,rating))


cursor.close()
cnx.close()

