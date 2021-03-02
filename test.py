import mysql.connector



# Port 3306 behöver vi inte ange = standard för MySQL

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hejsan123",
  database="testdatabasen"
)

mycursor = mydb.cursor()

sql = "INSERT INTO movies (title,release_year,genre,instock) VALUES (%s, %s, %s, %s)"
val = ("Udda eller jämnt", 1971,"Drama", 12)
mycursor.execute(sql, val)


mydb.commit()

