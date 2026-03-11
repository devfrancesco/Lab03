import time

import multiDictionary as md


class SpellChecker:

    def __init__(self):
        self.myList = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        new_txtIn = replaceChars(txtIn.lower())
        parole_utente = new_txtIn.split()
        inizio = time.time()
        risultati = self.myList.searchWord(parole_utente, language)
        fine = time.time()
        print(f"Using contains")
        errori = 0
        for r in risultati:
            if not r._corretta: #if r._corretta == False
                print(r._parola)
                errori+=1
        print(f"Numero di errori: {errori}")
        print(f"Time elapsed: {fine-inizio}")
        print("-"*20)

        #Ricerca Lineare
        inizio2 = time.time()
        risultati2 = self.myList.searchWordLinear(parole_utente, language)
        fine2 = time.time()
        print(f"Using Linear search")
        errori2 = 0
        for r in risultati:
            if not r._corretta:  # if r._corretta == False
                print(r._parola)
                errori2 += 1
        print(f"Numero di errori: {errori2}")
        print(f"Time elapsed: {fine2 - inizio2}")
        print("-" * 20)

        #Ricerca Dicotomica
        inizio3 = time.time()
        risultati3 = self.myList.searchWordDichotomic(parole_utente, language)
        fine3 = time.time()
        print(f"Using Dichotomic search")
        errori3 = 0
        for r in risultati3:
            if not r._corretta:  # if r._corretta == False
                print(r._parola)
                errori3 += 1
        print(f"Numero di errori: {errori3}")
        print(f"Time elapsed: {fine3 - inizio3}")
        print("-" * 20)



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'*_()[]{}<#+-.!$%^;,=>"
    for c in chars:
        text = text.replace(c, "")
    return text