import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port=3306
)
cur = conn.cursor()

def creaData(nombreData):
  cur.execute("CREATE DATABASE "+nombreData)
  listo = "Base de datos creada con exito"
  return listo

def creacion(nombreDataBase,nombreTabla):
  cur.execute("USE "+nombreDataBase)
  cur.execute("CREATE TABLE "+ nombreTabla+" (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), titulo VARCHAR(200), autor VARCHAR(50),fechaDePublicacion DATE, contenidoPublicacion TEXT)")
  listo = "tabla creada!"
  return listo

nombreBase = "noticias_region_aysen"
noticieros= [
  "EPD_noticias","Viento_patagon","El_divisadero","Diario_aysen","El_chalenko","Radio_santa_maria",
  "Diario_aysen_opina","Tehuelche_noticias","Canal_sur_patagonia","Risco_aysen","Radio_las_nieves_FM"
]
creaData(nombreBase)
for i in noticieros:
  creacion(nombreBase,i)

cur.execute("SHOW TABLES")
for row in cur:
  print(row)







listaa= [
  "EPD_noticias","Viento_patagon","El_divisadero","Diario_aysen","El_chalenko","Radio_santa_maria",
  "Diario_aysen_opina","Tehuelche_noticias","Canal_sur_patagonia","Risco_aysen","Radio_las_nieves_FM"
]




