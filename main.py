import translator as tr

t = tr.Translator()
str = "dictionary.txt"
t.loadDictionary(str)

while(True):

    t.printMenu()

    txtIn = input("\n")

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn1 = input("Ok, quale parola devo aggiungere?\n")
        t.handleAdd(txtIn1,str)

    if int(txtIn) == 2:
        print()
        txtIn1=input("Ok, quale parola devo cercare?\n")
        t.handleTranslate(txtIn1)

    if int(txtIn) == 3:
        txtIn1 = input("Ok, quale parola devo cercare?\n")
        t.handleWildCard(txtIn1)

    if int(txtIn) == 4:
        print(t.handleDictionaryPrint())

    if int(txtIn) == 5:
        break

#RICORDARE COMMIT
#VEDERE LOWER CASE E SCRITTURA FILE CON PIù TRADUZIONI