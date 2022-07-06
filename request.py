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

def requestData(consulta):
    if consulta.strip()[0:5]=="SELECT":
        try:
            cur.execute(consulta)
        except (mariadb.Error) as error:
            print("Error: ",error)
    else:
        print("Error: No ingreso una consulta")
requestData("SELECT m.name,count(*) FROM Noticias n JOIN Medio m ON m.url_medio=n.url_medio GROUP BY m.url_medio;")
def personasEnDia(fecha):
    requestData(f"SELECT p.name FROM Persona p JOIN Menciones m ON m.persona = p.persona JOIN Noticias n ON n.noticia_url = m.noticia WHERE n.fecha_noticia = '{fecha}' GROUP BY p.persona;")

personasEnDia("2022-07-01");
def popularidad(persona):
    requestData(f"SELECT s.value,s.fechaPuntaje FROM Score s JOIN Persona p ON p.persona = s.persona WHERE p.name = '{persona}' ORDER BY s.fechaPuntaje DESC;")

popularidad("Alex Garnica");
requestData("SELECT m.name,n.creation_date FROM Medio m ORDER BY m.creation_date ASC LIMIT 5;")
conn.commit() 
conn.close()