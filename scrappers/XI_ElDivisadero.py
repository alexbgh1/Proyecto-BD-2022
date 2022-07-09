import random
from requests_html import HTMLSession
import w3lib.html
import html
#https://www.eldivisadero.cl/home


def format_date(date):
        return(date.split("T")[0])

def eldivisadero():
        ## Simular que estamos utilizando un navegador web
        USER_AGENT_LIST = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

        session = HTMLSession()

        # # # URL  a revisar
        URL = ["https://www.eldivisadero.cl/_noticia/Vecinos-de-sectores-pr%C3%B3ximos-a-derrumbes-preocupados-por-p%C3%A9sima-condici%C3%B3n-del-agua-potable/NjczNjU=",
        "https://www.eldivisadero.cl/_noticia/Reporte-de-junio-Actividad-de-volcanes-Hudson-Mac%C3%A1-Cay-Melimoyu-y-Mentolat-se-mantiene-en-Alerta-Verde/NjczNzE=",
        "https://www.eldivisadero.cl/_noticia/Mejoran-acceso-a-las-viviendas-de-adultos-mayores-de-Melinka/NjczNjg="]

        # # # Path a buscar - Titulo - Fecha - Texto
        xpath_title="//div[@class='titular']"
        xpath_date="//section[@class='enc centro']//div[@class='txt']"
        xpath_text="//section[@class='texto centro']//p"

        titles = []
        dates = []
        texts = []

        for page in (URL):
                # # # User - Agent
                headers = {'user-agent':random.choice(USER_AGENT_LIST) }
                response = session.get(page,headers=headers)
                title = response.html.xpath(xpath_title)[0].text
                date = response.html.xpath(xpath_date)[1].text
                list_p = response.html.xpath(xpath_text)
                text = ""
                for p in list_p:
                        content = p.text
                        content = w3lib.html.remove_tags(content)
                        content = w3lib.html.replace_escape_chars(content)
                        content = html.unescape(content)
                        content = content.strip()
                        text=text+" "+content
                
                titles.append(title)
                dates.append(date)
                texts.append(text)

        print("Data scrappeada con éxito.\nEntre 0 y",len(URL)-1," urls.")
        # print("Data scrappeada con éxito.\nVerifica los textos ingresando un número entre 0 y",len(URL)-1,"para verificar su información")

        # def checkData(idx,URL=URL, titles=titles, dates=dates, texts=texts):
        #         print("")
        #         print(f"URL: {URL[idx]}")
        #         print(f"Title: {titles[idx]}")
        #         print(f"Date: {dates[idx]}")
        #         print(f"Text (50 caracteres): {texts[idx][:50]}")
        #         print("")

        # continuar = 1
        # while(continuar):
        #         try:
        #                 idx = int(input("Ingresar índice a revisar: "))
        #                 checkData(idx)
        #                 continuar = int(input("Continuar(1): "))
        #         except:
        #                 print("Ingresar número válido entre: 0 y ",len(URL)-1)

        return URL, titles, dates, texts