import dictionary

class Translator:

    def __init__(self):
        self.dict = dictionary.Dictionary()

    def printMenu(self):
        print("--------------------------- \n Translator Alien-Italian \n\n---------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("---------------------------")

    def handleError(self, word):
        for i in range(len(word)):
            if word[i]!=" ":
                if word[i].isalpha() is False:
                    return False

    def handleErrorWizardCard(self, word):
        for i in range(len(word)):
            if word[i]!=" " and word[i]!="?":
                if word[i].isalpha() is False:
                    return False

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        f=open(dict,"r", encoding="utf-8")

        for line in f:
            details=line.strip("\n").split(" ")
            self.dict.addWord(details[0], details[1])

        f.close()

    def handleAdd(self, entry, nameFile):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        details=entry.split(" ")
        if len(details)==2 and (self.dict.get(details[0]) is None):
            if self.handleError(entry) is False:
                raise ValueError(f"Parola non valida. Inserisci solo caratteri alfabetici")
            else:
                self.dict.addWordAndWrite(entry.split(" ")[0].lower(), entry.split(" ")[1].lower(), nameFile)
                print(f"['{entry.split(" ")[0]}', '{entry.split(" ")[1]}']")
        elif len(details)==2 and self.dict.get(details[0]) is not None:
            self.dict.addTranslation(details[0], details[1], nameFile)
        else:
            for i in range(1, len(details)):
                if self.handleError(entry) is False:
                    raise ValueError(f"Parola non valida. Inserisci solo caratteri alfabetici")
                self.dict.addTranslation(details[0], details[i], nameFile)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>

        if self.handleError(query) is False:
            raise ValueError(f"Parola non valida. Inserisci solo caratteri alfabetici")
        else:
            print(self.dict.translate(query.lower()))

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        count = 0
        for c in query:
            if c == '?':
                count=+1

        if count==1:
            if self.handleErrorWizardCard(query) is False:
                raise ValueError(f"Parola non valida. Inserisci solo caratteri alfabetici")
            else:
                print(self.dict.translateWordWildCard(query.lower()))


    def handleDictionaryPrint(self):
        return self.dict.__str__()


