import eel
import mysql.connector

Select_stmt=("Select * from mstcountry")

def runsql(state):
    # Connect to the database file, if it does not exist, create it automatically
    conn=mysql.connector.connect(user='root',password='',host='localhost',database='test')
    c = conn.cursor()

    # Run the sql statement and get the sqlite.cousor object
    cursor = c.execute(state)

    # Read the contents of the cursor
    for i in cursor:
        print(i)

    conn.commit()
    # Close the connection
    conn.close()

    return cursor
    pass


eel.init('web')
eel.show('main.html')