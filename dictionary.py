from operator import getitem


class Dictionary:

    def __init__(self):
        self._dict = {}

    @property
    def dict(self):
        return self._dict

    def addWord(self, alienWord, meaning):
        self._dict[alienWord]=meaning

    def addWordAndWrite(self, alienWord, meaning, nameFile):
        with open(nameFile,"a") as f:
            f.write(f"{alienWord.lower()} {meaning.lower()}\n")

    def translate(self, alienWord):
        alienWord=alienWord.lower()
        return self._dict.get(alienWord)

    def translateWordWildCard(self, word):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        valueFound = []

        for c in alphabet:
            myStr = word.replace('?', c)
            if myStr in self._dict:
                valueFound.append(myStr)

        if len(valueFound)==1:
            return self._dict.get(valueFound[0])
        else:
            myStr=""
            for v in valueFound:
                myStr+=self._dict.get(v)+"\n"
            return myStr


    def get(self, query):
        return self._dict.get(query.lower())

    def addTranslation(self,alienWord, translation, nameFile):
        alienWord=alienWord.lower()
        translation=translation.lower()
        r=open(nameFile,"r").readlines()
        f=open(nameFile,"w")

        for line in r:
              if line.split(" ")[0]==alienWord.lower():
                 f.write(line.strip("\n")+" "+translation+"\n")
              else:
                 f.write(line)




        if alienWord in self._dict:
            self._dict[alienWord]=self._dict[alienWord]+" "+translation.lower()
        else:
            self._dict[alienWord]=translation.lower()
            f.write(f"{alienWord} {translation}\n")

        f.close()

        print("Aggiunta!")

    def __str__(self):
        myStr=""

        for element in self._dict:
            myStr+=f"['{element}', '{self._dict.get(element)}']\n"

        return myStr




