import pyodbc
#
# class NwProducts():
#     def __init__(self):
#         self.server = 'localhost,1433'
#         self.database = 'Northwind'
#         self.username = 'sa'
#         self.password = 'Passw0rd2018'
#         self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
#         self.cursor = self.docker_Northwind.cursor()
#
# my_db = NwProducts()
#
# result = my_db.cursor.execute("SELECT * FROM Products")
# rows = result.fetchall()
# for row in rows:
#     print(row.ProductID,row.ProductName, row.UnitPrice)


#--------------------------------------------HOMEWORK----------------------------######
#
# conn = pyodbc.connect(
#     'DRIVER={SQL Server};'
#     'SERVER=localhost,1433;'
#     'DATABASE=Northwind;'
#     'UID=;sa;'
#     'PWD=Passw0rd2018;'
#     'Trusted_Connection=yes;'
# )
#
# def read(conn):
#     print("Read")
#     cursor =conn.cursor()
#     cursor.execute("SELECT * FROM Products")
#     for row in cursor:
#         print(f'row = {row}')
#     print()
#
# def create(conn):
#     print("Create")
#     cursor = conn.cursor()
#     cursor.execute(
#         'INSERT into Products(UnitPrice,ProductName) values (?,?);',
#         (300,'Washing Machine')
#     )
#     conn.commit()
#     read(conn)
#
#
# def update(conn):
#     print("Update")
#     cursor = conn.cursor()
#     cursor.execute(
#         'UPDATE Products set ProductName = ? where UnitPrice = ?;',
#         ('Washing Machine', 300)
#     )
#     conn.commit()
#     read(conn)
#
# def delete(conn):
#     print("Delete")
#     cursor = conn.cursor()
#     cursor.execute(
#         'DELETE from Products <=20;'
#     )
#     conn.commit()
#     read(conn)
#
# read(conn)
# # create(conn)
# # update(conn)
# # delete(conn)
#
# conn.close()
# #
# #

#----------------------------------------------HOMEWORK PART II Attempt-----------------------####


class Northwind():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'sa'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def read(self):
        print("Read")
        my_db = Northwind
        cursor =my_db.cursor()
        cursor.execute("SELECT * FROM Products")
        for row in cursor:
            print(f'row = {row}')
        print()

    def create(self):
        print("Create")
        my_db = Northwind
        cursor = my_db.cursor()
        cursor.execute(
            'INSERT into Products (UnitPrice,ProductName) values (?,?);',
            (300, 'Washing Machine')
    )
        my_db.commit()
        #create(my_db)

    def update(my_db):
        print("Update")
        my_db = Northwind
        cursor = my_db.cursor()
        cursor.execute(
            'UPDATE Products set ProductName = ? where UnitPrice = ?;',
            ('Washing Machine', 300)
    )
        my_db.commit()
        #update(my_db)

    def delete(my_db):
        print("Delete")
        my_db = Northwind
        cursor = my_db.cursor()
        cursor.execute(
            'DELETE from Products <=20;'
    )
        my_db.commit()
        #delete(my_db)

my_db = Northwind()

#read(my_db)
#create(my_db)
#update(my_db)
#delete(my_db)

my_db.Northwind.close()

# result = my_db.cursor.execute("SELECT * FROM Products")
# rows = result.fetchall()
# for row in rows:
#     print(row.ProductID,row.ProductName, row.UnitPrice)

