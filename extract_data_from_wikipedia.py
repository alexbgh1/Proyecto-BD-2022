import extract_person as extract # DATOS DE ELCHELENKO

import wikipedia
wikipedia.set_lang("es")
import pageviewapi
print("wikipedia OK")

from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)
q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)
print("transformers OK")


import warnings
warnings.filterwarnings("ignore")

persons = extract.extract_person() # DATOS DE ELCHELENKO

datos_person= []
for person in persons:        
    #persona mencionada
    print(person)

    #resumen wikipedia
    try:
        results= wikipedia.search(person)
        print(results)
        summary= wikipedia.summary(results[0], sentences=3)
        print(summary)
        #preguntas
        nacimiento = q_a_es(question="¿En qué año nació el o ella?", context=summary)
        print("Nació en "+nacimiento["answer"])

        profesion = q_a_es(question="¿Cuál es su profesión?", context=summary)
        print("Su profesión es "+profesion["answer"])

        nacionalidad = q_a_es(question="¿Cuál es su nacionalidad?", context=summary)
        print("Es "+nacionalidad["answer"])

        datos_person.append([nacimiento["answer"],profesion["answer"],nacionalidad["answer"]])
    except:
        print("Person: ",person, " was not found on wikipedia.")
    # result=pageviewapi.per_article('es.wikipedia', person, '20220705', '20220705',
    #                 access='all-access', agent='all-agents', granularity='daily')

    # for item in result.items():
    #     for article in item[1]:
    #         views=article['views']
    #         print("Su popularidad hoy es: "+str(views)+" visitas en wikipedia español.")

    print("--------------------")

print(datos_person)