import psycopg2

def getconnection():
    return psycopg2.connect(host='localhost',
                        dbname='postgres',
                        user='postgres',
                        password='postgres')

class userCredentialAccessor:
    def getUser(userCredential):
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Users WHERE UserName=%s and PassWord=%s ', (userCredential.userName, userCredential.password))
            return cursor.fetchall()
    
    def addUser(userCredential):
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Users VALUES(%s, %s, %s)', (userCredential.userName, userCredential.password, userCredential.updateDate))
    
    def checkUserIs(userCredential):
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Users WHERE UserName=%s ', (userCredential.userName, ))
            return cursor.fetchall()
        
