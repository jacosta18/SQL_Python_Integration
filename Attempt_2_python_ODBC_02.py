import pyodbc

class Northwind():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'sa'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def create(self):
        my_db = Northwind
        table_name = input("Name your table: ")
        try:
            my_db.cursor.execute("CREATE TABLE" + " " + table_name + " "
                "(SpartanID int NOT NULL PRIMARY KEY, "
                "SpartanTitle varchar(255), "
                "SpartanFirstName varchar(255), "
                "SpartanLastName varchar (255)"
                ")")
        except:
            print("Something has gone wrong. Please check again!")

        finally:
            my_db.docker_Northwind.commit()
            my_db.docker_Northwind.close()
            print("\n"+table_name+"has been successfully created!*\n")
            return

    def read(self):
        my_db = Northwind

