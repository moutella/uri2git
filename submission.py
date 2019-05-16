block = True
line=False
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
            "OCaml": [block, "(*\ncomment\n*)"],
            "Pascal": [line, "//"],
            "Python 2": [line, "#"],
            "Python 3": [line, "#"],
            "Ruby": [line, "#"],
            "Scala": [line, "//"],
            "PostgreSQL": [line, "--"]}

multiComment = {"C": ["/*", "*/"], 
                "C#": ["/*", "*/"], 
                "Python3": ["\"\"\"", "\"\"\""]}
class Submission:
    def __init__(self, code, data, tries, language, versao):
        self.code = code
        self.tries = tries
        self.data = data
        self.language = language
        self.versao = versao