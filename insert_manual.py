from distutils.log import error
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

# Especificamos utilizar la Base de Datos 'Sophia3'
cur.execute("USE Sophia3")


# = = = = = = = = = = =  = = = = = = = = = = = =

#profesion VARCHAR(100), fecha_nac DATE, name VARCHAR(100), wikipedia BOOL, wikipedia_url VARCHAR(250)"
def insertarPersona(profesion, fecha_nac, name, wikipedia, url_wikipedia):
    #print(f"INSERT INTO persona (profesion, fecha_nac, name, wikipedia, wikipedia_url) VALUES ('{profesion}','{fecha_nac}', '{name}', {wikipedia}, '{url_wikipedia}')")
    cur.execute(f"INSERT INTO persona (profesion, fecha_nac, name, wikipedia, wikipedia_url) VALUES ('{profesion}','{fecha_nac}', '{name}', {wikipedia}, '{url_wikipedia}');")

#dueno VARCHAR(250) NOT NULL PRIMARY KEY, name VARCHAR(100), is_person BOOL
def insertDueno(dueno,name,is_person):
    cur.execute(f"INSERT INTO Dueno(dueno,name,is_person) VALUES ('{dueno}','{name}','{is_person}');")

#puntaje INT PRIMARY KEY, persona INT REFERENCES Persona(persona), fechaPuntaje DATE, value INT
def insertScore(puntaje,persona,fechaPuntaje, value):
    cur.execute(f"INSERT INTO Score(puntaje,persona,fechaPuntaje,value) VALUES ({puntaje},{persona},'{fechaPuntaje}',{value});")

#Noticias(noticia_url VARCHAR(250) NOT NULL PRIMARY KEY, author_noticia VARCHAR(100), title_noticia VARCHAR(100), text_noticia TEXT, fecha_noticia DATE, url_medio VARCHAR(250) REFERENCES Medio(url_medio)
def insertNoticias(noticia_url, author_noticia,title_noticia,text_noticia,fecha_noticia,url_medio):
    cur.execute(f"INSERT INTO Noticias(noticia_url,author_noticia,title_noticia,text_noticia,fecha_noticia,url_medio) VALUES ('{noticia_url}','{author_noticia}','{title_noticia}','{text_noticia}','{fecha_noticia}','{url_medio}');")

#Medio(url_medio VARCHAR(250) NOT NULL PRIMARY KEY, name VARCHAR(100), creation_date DATE, region INT, country VARCHAR(50), language VARCHAR(50)
def insertMedio(url_medio,name,creation_date,region,country,language):
    cur.execute(f"INSERT INTO Medio(url_medio,name,creation_date,region,country,language) VALUES ('{url_medio}','{name}','{creation_date}',{region},'{country}','{language}');")

#Menciones(mencionar VARCHAR(200) PRIMARY KEY, noticia VARCHAR(250) NOT NULL, persona INT NOT NULL, FOREIGN KEY(noticia) REFERENCES Noticias(noticia_url), FOREIGN KEY(persona) REFERENCES Persona(persona)
def insertMenciones(mencionar, noticia, persona):
    cur.execute(f"INSERT INTO Menciones(mencionar,noticia,persona) VALUES ('{mencionar}','{noticia}',{persona});")

#Posee(posee VARCHAR(250) PRIMARY KEY, dueno VARCHAR(250) NOT NULL, url_medio VARCHAR(250) NOT NULL, fecha_inicio DATE, fecha_fin DATE, FOREIGN KEY(dueno) REFERENCES Dueno(dueno), FOREIGN KEY(url_medio) REFERENCES Medio(url_medio)
def insertPosee(posee,dueno,url_medio,fecha_inicio,fecha_fin):
    print(f"INSERT INTO Posee(posee,dueno, url_medio, fecha_inicio, fecha_fin) VALUES ('{posee}','{dueno}','{url_medio}', '{fecha_inicio}', '{fecha_fin}');")
    cur.execute(f"INSERT INTO Posee(posee,dueno, url_medio, fecha_inicio, fecha_fin) VALUES ('{posee}','{dueno}','{url_medio}', '{fecha_inicio}', '{fecha_fin}');")


continuar = 1
print("Escribir comandos MYSQL:")
while(continuar):
    try:
        #OK - insertarPersona('ing civil','2012-01-31', 'Manu', 1,'https://es.wikipedia.org/wiki/Manuel_Cabr%C3%A9')
        #OK - insertDueno('pepe2313','pepe',1)
        #OK - insertScore(0,1,'2001-02-04',1923)
        #OK - insertNoticias('http://web.elpatagondomingo.cl/2022/06/28/tribunal-de-coyhaique-condeno-9-imputados-como-autores-del-delito-de-trafico-de-drogas/','pepe','Tribunal de Coyhaique condenó a 9 imputados como autores del delito de tráfico de drogas','El Tribunal de Juicio Oral en lo Penal de Coyhaique dictó este martes veredicto condenatorio en contra de 9 personas por delitos establecidos en la Ley 20.000, sobre tráfico ilícito de estupefacientes.','2022-06-28','http://web.elpatagondomingo.cl/')
        #OK - insertMedio('http://web.elpatagondomingo.cl/','Elpatagondomingo','2015-01-02',11,'Chile','Español')
        #insertMenciones('Cecilia Urbina Pinto','http://web.elpatagondomingo.cl/2022/06/28/tribunal-de-coyhaique-condeno-9-imputados-como-autores-del-delito-de-trafico-de-drogas/', 0)
        #insertPosee('asdasd','http://web.elpatagondomingo.cl/','pepe13','2022-01-01','2022-01-01')

        print('Inserción exitosa')
    except(mariadb.Error) as error:
        print('Error al insertar', error)
    
    continuar = int(input("Continue? Yes(1) No(0): "))



conn.commit() 
conn.close()