import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', database='cafe')
cursor = db.cursor(dictionary=True)

