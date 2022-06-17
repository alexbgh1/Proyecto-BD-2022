import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="password", #root
        host="127.0.0.1",
        port=3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Create Database
def createDatabase():
    query_create = "CREATE DATABASE Sophia3"
    cur.execute(query_create)

# Create tables (modelo relacional)
def createTables():
    cur.execute("USE Sophia3")
    #id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50),fechaDePublicacion DATE, contenidoPublicacion TEXT
    cur.execute("CREATE TABLE Person (person_id INT AUTO_INCREMENT PRIMARY KEY, profesion VARCHAR(100), fecha_nac DATE, name VARCHAR(100), wikipedia BOOL, wikipedia_url VARCHAR(250))") #Persona PK
    cur.execute("CREATE TABLE News_outlet (news_outlet_url PRIMARY KEY, name VARCHAR(100), creation_date DATE, region INT, country VARCHAR(50), language VARCHAR(50))") #Medios PK
    cur.execute("CREATE TABLE Owner (owner_id PRIMARY KEY, name VARCHAR(100), is_person BOOL)") #Dueño PK
    cur.execute("CREATE TABLE Owns ()") #Posee FK (Medios y Dueños)
    cur.execute("CREATE TABLE New ()") #Noticia FK (Mendios)
    cur.execute("CREATE TABLE Mention ()") #Menciones FK (Noticia y Persona)
    cur.execute("CREATE TABLE Score ()") #Puntaje FK (Persona)

createDatabase()
createTables()
#cur.execute("DRPO DATABASE Sophia3")
conn.commit() 
conn.close()