
from Connection import *


class Cclients:

    def showClients():

        try:
            conect = Cconnection.conectionDataBase()
            cursor = conect.cursor()
            cursor.execute('SELECT * FROM users;')
            myResult = cursor.fetchall()
            conect.commit()
            conect.close()
            return myResult

        except mysql.connector.Error as error:
            print(f'Error displaying data, Error: {error}')

    def enterClients(Names, Surname, Sex):

        try:
            conect = Cconnection.conectionDataBase()
            cursor = conect.cursor()
            sql = 'INSERT INTO users VALUES (null, %s, %s, %s);'

            values = (Names, Surname, Sex)
            cursor.execute(sql, values)
            conect.commit()
            print(cursor.rowcount, 'Record entered')
            conect.close()

        except mysql.connector.Error as error:
            print(f'Data enrty error {error}')

    def modifyClients(userID, Names, Surname, Sex):

        try:
            conect = Cconnection.conectionDataBase()
            cursor = conect.cursor()
            sql = "UPDATE users SET Names = %s, Surnames = %s, Sex = %s WHERE Id = %s;"

            values = (Names, Surname, Sex, userID)
            cursor.execute(sql, values)
            conect.commit()
            print(cursor.rowcount, 'Record updated')
            conect.close()

        except mysql.connector.Error as error:
            print(f'Error updating data. Error {error}')

    def deleteClients(userID):

        try:
            conect = Cconnection.conectionDataBase()
            cursor = conect.cursor()
            sql = "DELETE FROM users WHERE id = %s;"

            values = (userID,)
            cursor.execute(sql, values)
            conect.commit()
            print(cursor.rowcount, 'User Deleted')
            conect.close()

        except mysql.connector.Error as error:
            print(f'Error deleting data. Error {error}')
