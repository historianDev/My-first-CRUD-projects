# pip install mysql-connector-python
import mysql.connector


class Cconnection():

    def conectionDataBase():
        try:
            connection = mysql.connector.connect(user='root', password='historianDev',
                                                 host='127.0.0.1',
                                                 database='Clientsdb',
                                                 port='3306')
            print('Connection successful')
            return connection

        except mysql.connector.Error as error:
            print(f'Error connecting to database {error}')
            return connection

    conectionDataBase()
