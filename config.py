import json

uriUsermail = input("Digite o seu email do URI: ")
uriPassword = input("Digite a senha do URI: ")
config = {}
config['uri'] = []
config['uri'].append({"user-email" : uriUsermail, "password" : uriPassword})
with open("config", "w") as configFile:
    json.dump(config, configFile)