from asyncio.windows_events import NULL
import random
from requests_html import HTMLSession
import w3lib.html
import html
import scrappers.XI_ElChelenko as EC # DATOS DE ELCHELENKO <- con crawl url automaticas
import scrappers.XI_ElDivisadero as ED # DATOS DE ELDIVISADERO <- si crawl, url manual
import extract_person as extract
import extract_data_from_wikipedia as extract_wiki
# URL, titles, dates, texts = EC.elchelenko()

#=== Seleccionar Scrapping de datos
URL, titles, dates, texts = ED.eldivisadero()
print("Información de página recibida.") # Recolecta varias URL

#=== Utilizar su función de retorno de datos y extraer personas
persons = extract.extract_person(URL, titles, dates, texts)
print("Personas recibidas.")

#=== Utilizar su función de retorno de datos y extraer personas
datos_persons = extract_wiki.extract_wiki(persons)
print("Datos de personas recibidas.")

# print(URL,"\n")
# print(titles,"\n")
# print(dates,"\n")
# print(texts,"\n")

# print(persons,"\n")

print(datos_persons)