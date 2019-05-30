from requests import post, get, session
from bs4 import *
import os
from submission import Submission


class uriUser():
    def __init__(self, userEmail, password):
        self.login(userEmail, password)
        
    def login(self, userEmail, password):
        url = "https://www.urionlinejudge.com.br/"
        self.sess = session()
        siteBase = self.sess.get(url)
        siteSoup = BeautifulSoup(siteBase.text, features="html.parser")
        tagsHidden = siteSoup.find_all("input", type="hidden")
        valores = self.pegavalores(tagsHidden)
        payload = {"email": userEmail, "password": password, "remember_me": "0"}
        payload.update(valores)
        urlLogin = "https://www.urionlinejudge.com.br/judge/en/login"
        resultadoLogin = self.sess.post(urlLogin,
                                        data = payload,
                                        headers = dict(referer=urlLogin))
        if("logout" not in resultadoLogin.text):
            print("Não foi possível logar")
            exit()

    def pegavalores(self, tags): #Retorna os tokens da sessão para utilização no POST
        valores = {"_csrfToken": "", "_Token[fields]": "", "_Token[unlocked]": ""}
        for inp in tags:                ##input é palavra reservada
            if(inp.get('name') in valores):
                if(valores[inp.get('name')]==""):
                    valores[inp.get('name')] = inp.get('value')
        return valores

    def retornaSubmissions(self):
        urlSubmissions = "https://www.urionlinejudge.com.br/judge/pt/runs"
        submissionsPage = self.sess.get(urlSubmissions)
        numPagsSoup = BeautifulSoup(submissionsPage.text, features="html.parser")
        lastPage = numPagsSoup.find("li", {"class": "last"}).a.get('href')
        numeroDePaginas = lastPage[lastPage.find('=')+1:]
        print(lastPage)
        print(numeroDePaginas)
        submissions = []
        for i in range(int(numeroDePaginas),0, -1):
            print("----PAGINA {}----".format(i))
            linkAtual = "https://www.urionlinejudge.com.br/judge/pt/runs?page=" + str(i)
            paginaAtual = self.sess.get(linkAtual)
            paginaSoup = BeautifulSoup(paginaAtual.text, features = "html.parser")
            enviosDaPagina = paginaSoup.find_all("td", {"class": "id"})
            for envio in enviosDaPagina[::-1]:
                submission = self.criaSubmission(envio.a.text)
                submissions.append(submission)
        return submissions
    def criaSubmission(self, id):
        urlSubmission = "https://www.urionlinejudge.com.br/judge/pt/runs/code/" + id
        submissionPage = self.sess.get(urlSubmission)
        submissionSoup = BeautifulSoup(submissionPage.text, features="html.parser")
        dados = submissionSoup.find("div", {"class": "st-big-box"}).find_all("dd")
        idEnome = dados[0].text.split("-")
        resultado = dados[1].text.strip()
        language = dados[2].text.split("(")[0].strip()
        data = dados[5].text.strip()
        id = idEnome[0].strip()
        nome = idEnome[1].strip()
        codeLines = submissionSoup.find("pre", {"id": "code"})
        code = codeLines.text
        submission = Submission(id, nome, resultado, data, language, code)
        return submission
