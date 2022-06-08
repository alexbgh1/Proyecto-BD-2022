import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port=3306
)

cur = conn.cursor()
#crea una base de datos en mariadb
cur.execute("CREATE DATABASE noticias_region_aysen")
#se para en la base de datos creada
cur.execute("USE noticias_region_aysen")

#crea las tablas (medios de comunicacion)
cur.execute("CREATE TABLE EPD_noticias (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50),fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Viento_patagon (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50), fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE El_divisadero (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50), fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Diario_aysen (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50), fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE El_chalenko (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50), fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Radio_santa_maria (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50), fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Diario_aysen_opina_coyhaique (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50), fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Tehuelche_noticias (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50), fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Canal_sur_patagonia (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(2550), titulo VARCHAR(200), autor VARCHAR(50),fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Risco_aysen (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50),fechaDePublicacion DATE, contenidoPublicacion TEXT)")
cur.execute("CREATE TABLE Radio_las_nieves_FM (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50),fechaDePublicacion DATE, contenidoPublicacion TEXT)")

#solo sirve para ver que se crearon las tablas
cur.execute("SHOW TABLES")
for row in cur:
  print(row)


