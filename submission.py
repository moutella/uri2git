line=True
block = False
comment = {"C": [line, "//"], 
            "C#": [line, "//"], 
            "C==": [line, "//"],
            "C99": [line, "//"],
            "Go": [line, "//"],
            "Java7": [line, "//"],
            "Java8": [line, "//"],
            "JavaScript": [line, "//"],
            "Kotlin": [line, "//"],
            "Lua": [line, "--"],
            "OCaml": [block, ["(*", "*)"]],
            "Pascal": [line, "//"],
            "Python 2": [line, "#"],
            "Python 3": [line, "#"],
            "Ruby": [line, "#"],
            "Scala": [line, "//"],
            "PostgreSQL": [line, "--"]}

endings = {"C": "c", 
            "C#": "cs",
            "C++": "cpp",
            "C++17": "cpp", 
            "C99": "c",     #verificar 
            "Go": "go",
            "Haskell": "hs",
            "Java7": "java",
            "Java8": "java",
            "JavaScript": "js",
            "Kotlin":  "kt",
            "Lua": "lua",
            "OCaml": "ml",
            "Pascal": "pas",
            "Python 2": "py",
            "Python 3": "py",
            "Ruby": "rb",
            "Scala": "scl",
            "PostgreSQL": "sql"}

class Submission:
    def __init__(self, id, nome, result, data, language, version, code):
        self.id = id
        self.ending = endings[language]
        self.nome = nome
        self.result = result
        self.data = data
        self.language = language
        self.version = version
        self.code = code

    
    def createfile(self, submissionFile):
        commentTemplate = comment[self.language]
        if(commentTemplate[0]):
            submissionFile.write(commentTemplate[1] + "Nome: " + self.nome + "\n")
            submissionFile.write(commentTemplate[1] + "Resultado: " + self.result + "\n")
            submissionFile.write(commentTemplate[1] + "Data: " + self.data + "\n")
            submissionFile.write(commentTemplate[1] + "Linguagem: " + self.language + "\n")
            submissionFile.write(commentTemplate[1] + "Versão: " + str(self.version) + "\n")
            submissionFile.write(self.code)
        else:
            submissionFile.write(commentTemplate[1][0] + "Nome: " + self.nome + "\n")
            submissionFile.write( "Resultado: " + self.result + "\n")
            submissionFile.write( "Data: " + self.data + "\n")
            submissionFile.write( "Linguagem: " + self.language + "\n")
            submissionFile.write( "Versão: " + str(self.version) + "\n" + commentTemplate[1][1])
            submissionFile.write(self.code)