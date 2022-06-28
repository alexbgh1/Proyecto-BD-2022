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
    cur.execute("CREATE TABLE News_outlet (news_outlet_url VARCHAR(250) PRIMARY KEY, name VARCHAR(100), creation_date DATE, region INT, country VARCHAR(50), language VARCHAR(50))") #Medios PK
    cur.execute("CREATE TABLE Owner (owner_id VARCHAR(250) PRIMARY KEY, name VARCHAR(100), is_person BOOL)") #Dueño PK
    
    #### LA LINEA QUE SIGUE ESTÁ MAL
    # No supe poner las dos Foreign Key como PK (quizás se tenga que cambiar también el tipo de las otras pk para que coincida)
    ##cur.execute("CREATE TABLE Owns (owns_id VARCHAR(250) PRIMARY KEY, FOREIGN KEY (owns_id) REFERENCES News_outlet(news_outlet_url), REFERENCES (owns_id) Owner(owner_id), fecha_inicio DATE, fecha_fin DATE)") #Posee FK (Medios y Dueños)
    

    cur.execute("CREATE TABLE New (new_url VARCHAR(250) PRIMARY KEY, FOREIGN KEY (new_url) REFERENCES News_outlet(news_outlet_url), author_new VARCHAR(100), title_new VARCHAR(100), text_new TEXT, fecha_new DATE)") #Noticia FK (Medios)
    #### LA LINEA QUE SIGUE ESTÁ MAL
    ##cur.execute("CREATE TABLE Mention (mention_id PRIMARY KEY , FOREIGN KEY (mention_id) REFERENCES New(mention_id),FOREIGN KEY (new_url) REFERENCES Person(person_id) )") #Menciones FK (Noticia y Persona)


    cur.execute("CREATE TABLE Score (score_id INT PRIMARY KEY, FOREIGN KEY (score_id) REFERENCES Person(person_id), fecha_score DATE, value INT)") #Puntaje FK (Persona)

createDatabase()
createTables()
#cur.execute("DRPO DATABASE Sophia3")
conn.commit() 
conn.close()