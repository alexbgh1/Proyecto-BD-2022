import spacy
nlp = spacy.load("es_core_news_md")
print("spacy OK")

import warnings
warnings.filterwarnings("ignore")

def extract_person(URL, titles, dates, texts):

    import scrappers.XI_ElDivisadero as ED # DATOS DE ELDIVISADERO
    # URL, titles, dates, texts = EC.elchelenko()
    persons = []
    print("--------------------")
    print("Escaneando personas")
    print("--------------------")
    for idx, text in enumerate (texts): # idx -> pos de datos ; text -> texto en la posición idx ; url[idx] -> fuente noticia
        doc = nlp(text)
        pp = []
        for ent in doc.ents:
            if ((ent.label_ == "PER") and (" " in ent.text)):
                #persona mencionada
                person = ent.text
                pp.append(person)

        persons.append(pp)

    #Personas mencionadas en el primer texto, url[0] ; NOTA: Muchos 'nombres' son por mayusculas mal usadas o de artefactos tecnologicos (tarjetas, cosas en general)
    return persons
