import json
import shutil
import os
from git import *
from submission import Submission

repositoryName = "repo"



#def __init__(self, id, nome, result, data, language, version, code):

teste = Submission(2500, "Problema do Mestre", "Accepted", "24/02/2018", "Python 3", 2
, "nvals = int(input())\nfor i in range(nvals):\n    x = int(input())\n    y = 2015 - x\n    if y <= 0:\n        y -= 1\n        print('{} A.C.'.format(abs(y)))\n    else:\n        print('{} D.C.'.format(y))")
repo = None
if not os.path.exists(repositoryName):
	repo = Repo.init(os.path.join(os.curdir, 'repo'))
else:
	repo = Repo(repositoryName)

repo.config_reader()             # get a config reader for read-only access
with repo.config_writer():       # get a config writer to change configuration
    pass                         # call release() to be sure changes are written and locks are released


print(repo.working_tree_dir)
if not os.path.exists("repo/Python 3"):
	os.mkdir("repo/Python 3")
	

submissionFile = open("{}/{}/{}.{}".format(repositoryName, teste.language, teste.id, teste.ending), "w+")
teste.createfile(submissionFile)

submissionFile.close()
filepath = os.path.join(repo.working_tree_dir, "Python 3/2500.py")
print(filepath)
#index=IndexFile(repo)
print(repo.untracked_files)
print(repo.working_tree_dir)
print(repo.working_dir)
print(repo._working_tree_dir)
repo.index.add([filepath])
#comm = Commit(repo, Commit.NULL_BIN_SHA, repo.index.write_tree(),
#repo.index.commit("Botando o arquivo 2500.py", )
#print(repo.head)
