import mysql.connector

con = mysql.connector.connect(
user = "a0_student",
password = "a_student",
host = "111.111.111.111",
database = "_______pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")
