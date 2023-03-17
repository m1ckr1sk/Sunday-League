import mysql.connector

class MySqlConnection:
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                          host=self.host, database=self.database)
        self.cursor = self.cnx.cursor()
             
    def create(self, query, values):
        try:
            self.connect()
            self.cursor.execute(query, values)
            self.cnx.commit()
            print("Record created successfully")
        except mysql.connector.Error as error:
            print(f"Failed to create record {error}")
        finally:
            self.disconnect()

    def read(self, query):
        try:
            self.connect()
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as error:
            print(f"Failed to select record {error}")
        finally:
            self.disconnect()

    def update(self, query, values):
        try:
            self.connect()
            self.cursor.execute(query, values)
            self.cnx.commit()
            print("Record updated successfully")
        except mysql.connector.Error as error:
            print(f"Failed to update record {error}")
        finally:
            self.disconnect()

    def delete(self, query, values):
        try:
            self.connect()
            self.cursor.execute(query, values)
            self.cnx.commit()
            print("Record deleted successfully")
        except mysql.connector.Error as error:
            print(f"Failed to update record {error}")
        finally:
            self.disconnect()
            
    def disconnect(self):
        if self.cnx.is_connected():
            self.cursor.close()
            self.cnx.close()
        print("Connection closed")
