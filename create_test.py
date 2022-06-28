import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root", #root
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
    cur.execute("CREATE TABLE Persona(persona INT AUTO_INCREMENT NOT NULL PRIMARY KEY, profesion VARCHAR(100), fecha_nac DATE, name VARCHAR(100), wikipedia BOOL, wikipedia_url VARCHAR(250))") #Persona PK

    cur.execute("CREATE TABLE Score (puntaje INT PRIMARY KEY, persona INT REFERENCES Persona(persona), fechaPuntaje DATE, value INT)") #Puntaje FK (Persona)

    cur.execute("CREATE TABLE Medio(url_medio VARCHAR(250) NOT NULL PRIMARY KEY, name VARCHAR(100), creation_date DATE, region INT, country VARCHAR(50), language VARCHAR(50))") #Medios PK    

    cur.execute("CREATE TABLE Noticias(noticia_url VARCHAR(250) NOT NULL PRIMARY KEY, author_noticia VARCHAR(100), title_noticia VARCHAR(100), text_noticia TEXT, fecha_noticia DATE, url_medio VARCHAR(250) REFERENCES Medio(url_medio))") #Noticia FK (Medios)

    cur.execute("CREATE TABLE Dueno(dueno VARCHAR(250) NOT NULL PRIMARY KEY, name VARCHAR(100), is_person BOOL)") #Dueño PK

    cur.execute("CREATE TABLE Menciones(mencionar VARCHAR(200) PRIMARY KEY, noticia VARCHAR(250) NOT NULL, persona INT NOT NULL, FOREIGN KEY(noticia) REFERENCES Noticias(noticia_url), FOREIGN KEY(persona) REFERENCES Persona(persona))") #Menciones FK (Noticia y Persona)

    cur.execute("CREATE TABLE Posee(posee VARCHAR(250) PRIMARY KEY, dueno VARCHAR(250) NOT NULL, url_medio VARCHAR(250) NOT NULL, fecha_inicio DATE, fecha_fin DATE, FOREIGN KEY(dueno) REFERENCES Dueno(dueno), FOREIGN KEY(url_medio) REFERENCES Medio(url_medio))") #Posee FK (Medios y Dueños)



    

createDatabase()
createTables()
#cur.execute("DRPO DATABASE Sophia3")
conn.commit() 
conn.close()