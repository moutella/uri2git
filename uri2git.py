import json
import shutil
import os
from git import *
from submission import Submission
from uriscrapper import uriUser, retornaDataDaString

email = ''
senha = ''
with open('config') as auth:
    dados = json.load(auth)
    email = dados['uri'][0]['user-email']
    senha = dados['uri'][0]['password']


usuario = uriUser(email, senha)
submissions = usuario.retornaSubmissions()

repositoryName = "repo"
repo = None
if not os.path.exists(repositoryName):
	repo = Repo.init(os.path.join(os.curdir, 'repo'))
else:
	repo = Repo(repositoryName)

repo.config_reader()             # get a config reader for read-only access
with repo.config_writer():       # get a config writer to change configuration
    pass                         # call release() to be sure changes are written and locks are released
print(repo.working_tree_dir)


for sub in submissions:
    if not os.path.exists("repo/" + sub.language):
	    os.mkdir("repo/" + sub.language)
    submissionFile = open("{}/{}/{}.{}".format(repositoryName, sub.language, sub.id, sub.ending), "w+")
    sub.createfile(submissionFile)
    submissionFile.close()
    filepath = os.path.join(repo.working_tree_dir, sub.language + "/" + sub.id + "." + sub.ending)
    date = str(retornaDataDaString(sub.data))
    os.environ["GIT_AUTHOR_DATE"] = date
    os.environ["GIT_COMMITTER_DATE"] = date
    repo.index.add([filepath])
    comm = Commit(repo, Commit.NULL_BIN_SHA, repo.index.write_tree(), repo.index.commit("Desafio " + sub.id))
