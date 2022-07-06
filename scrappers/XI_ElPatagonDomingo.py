import random
from requests_html import HTMLSession
import w3lib.html
import html
#http://www.elpatagondomingo.cl/


def format_date(date):
        return(date.split("T")[0])

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
URL = ["http://web.elpatagondomingo.cl/2022/06/30/trafico-de-datos-moviles-en-aysen-supera-el-promedio-nacional-en-2022/",
"http://web.elpatagondomingo.cl/2022/06/28/tribunal-de-coyhaique-condeno-9-imputados-como-autores-del-delito-de-trafico-de-drogas/",
"http://web.elpatagondomingo.cl/2022/06/28/corte-de-coyhaique-conoce-nueva-querella-de-capitulos-contra-jueza-cecilia-urbina/",
"http://web.elpatagondomingo.cl/2022/06/25/ministerio-de-salud-decreto-alerta-sanitaria-nacional-por-viruela-del-mono/"]

# # # Path a buscar - Titulo - Fecha - Texto
xpath_title="//div//h1"
xpath_date="//time[@class='entry-date published']//@datetime"
xpath_text="//div[@class='entry-content clearfix']//p"

titles = []
dates = []
texts = []

for page in (URL):
        # # # User - Agent
        headers = {'user-agent':random.choice(USER_AGENT_LIST) }
        response = session.get(page,headers=headers)
        
        title = response.html.xpath(xpath_title)[0].text
        date = response.html.xpath(xpath_date)[0]
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
        dates.append(format_date(date))
        texts.append(text)
        
print("Data scrappeada con éxito.\nVerifica los textos ingresando un número entre 0 y",len(URL)-1,"para verificar su información")

def checkData(idx,URL=URL, titles=titles, dates=dates, texts=texts):
        print("")
        print(f"URL: {URL[idx]}")
        print(f"Title: {titles[idx]}")
        print(f"Date: {dates[idx]}")
        print(f"Text (50 caracteres): {texts[idx][:50]}")
        print("")

continuar = 1
while(continuar):
        try:
                idx = int(input("Ingresar índice a revisar: "))
                checkData(idx)
                continuar = int(input("Continuar(1): "))
        except:
                print("Ingresar número válido entre: 0 y ",len(URL)-1)