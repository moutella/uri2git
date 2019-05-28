from requests import post, get, session
from bs4 import *
import os
import json

email = ''
senha = ''
with open('auths') as auth:
    dados = json.load(auth)
    email = dados['uri'][0]['user-email']
    senha = dados['uri'][0]['password']
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
payload = {"email": email, "password": senha, "remember_me": "0"}
payload.update(valores)
#print(payload)
urlLogin = "https://www.urionlinejudge.com.br/judge/en/login"
resultadoLogin = session.post(urlLogin,
                                data = payload,
                                headers = dict(referer=urlLogin))

## --- BLOCO DE PEGAR TODOS OS ENVIOS ---
urlSubmissions = "https://www.urionlinejudge.com.br/judge/pt/runs"
submissionsPage = session.get(urlSubmissions)
print(submissionsPage.text)
envioSoup = BeautifulSoup(submissionsPage.text, features="html.parser")
enviosDaPagina = envioSoup.find_all("tr")
for envio in enviosDaPagina[1:]:
    print(envio.a)
