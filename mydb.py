# Install Mysql on your own machine
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Inferni5'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a db
cursorObject.execute("CREATE DATABASE grootcode21")

print("All done!")