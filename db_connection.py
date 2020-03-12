import pyodbc

# make the connection
server = '127.0.0.1:1433'
database = 'Northwind'
user_id = 'SA'
password = 'Passw0rd2018'

# making the connection
conn = pyodbc.connect('DSN=MYMSSQL;DATABASE=Northwind;UID=SA;PWD=Passw0rd2018')

# creating a cursor object from connection
# imagine like a real cursor on your Azure Data Studio
# This will maintain state
crsr = conn.cursor()

# Running SQL queries using .execute()
rows = crsr.execute("select * FROM Customers")

# Cursor maintains state
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)
#
# # each row has all the columns of that entry
# # getting individual data is easy from this row
# print(row.CompanyName)
# print(row.ContactName)
# print(row.Fax)

# Checking the headers of the columns
# print(crsr.description)

# using the .fetchall() - it is dangerous
# it's dangerous because you can stall/crash your servers if there's a lot of data
# if there is a lot of data, it will bottleneck the system
crsr.execute("select * FROM Customers")
all_rows = crsr.fetchall()
print(all_rows)

counter = 1
for item in all_rows:
    print(counter, item.ContactName, '-', 'Fax', item.Fax)
    counter += 1

# best practice is to use a while loop and fetchone()
# until your entry is none
rows = crsr.execute("select * FROM Customers")
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.ContactName)

# Another example of whille loop with fetchone but with products table
rows = crsr.execute("SELECT * FROM Products")
new_values = []

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice * 200)
    new_values.append(record.UnitPrice * 200)

print(new_values)
