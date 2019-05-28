from requests import post, get, session
from bs4 import *
import os


#### ---------------------LOGIN functions----------------------
def pegavalores(tags): #Retorna os tokens da sessão para utilização no POST
    valores = {"_csrfToken": "", "_Token[fields]": "", "_Token[unlocked]": ""}
    for inp in tags:
        if(inp.get('name') in valores):
            if(valores[inp.get('name')]==""):
                valores[inp.get('name')] = inp.get('value')
    return valores






### ---------------- BLOCO DO LOGIN ------------------
url = "https://www.urionlinejudge.com.br"

session = session()
siteBase = session.get(url)
siteSoup = BeautifulSoup(siteBase.text, features="html.parser")
tagsHidden = siteSoup.find_all("input", type="hidden")
valores = pegavalores(tagsHidden)
print(valores)


