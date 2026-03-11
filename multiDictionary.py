import dictionary as d
import richWord as rw
from richWord import RichWord


class MultiDictionary:

    def __init__(self):
       self.dizionario_corrente = d.Dictionary()

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        path = f"./resources/{language.capitalize()}.txt"
        self.dizionario_corrente.loadDictionary(path)

        risultato = []
        diz_lista = self.dizionario_corrente.dict

        for w in words:
            rw = RichWord(w)
            if w.lower() in diz_lista:
                rw.corretta = True
            else:
                rw.corretta = False
            risultato.append(rw)
        return risultato

    def searchWordLinear(self, words, language):
        path = f"./resources/{language.capitalize()}.txt"
        self.dizionario_corrente.loadDictionary(path)
        diz_lista = self.dizionario_corrente.dict
        risultato = []
        for w in words:
            rw = RichWord(w.lower())
            trovata = False
            for parola in diz_lista:
                if w.lower() == parola:
                    trovata = True
                    break
            rw._corretta = trovata
            risultato.append(rw)
        return risultato

    def searchWordDichotomic(self, words, language):
        path = f"./resources/{language.capitalize()}.txt"
        self.dizionario_corrente.loadDictionary(path)
        diz_lista = self.dizionario_corrente.dict
        risultato = []
        for w in words:
            rw = RichWord(w.lower())
            trovata = False
            inizio = 0
            fine = len(diz_lista)-1
            while inizio <= fine:
                meta = (inizio + fine)//2
                punto_medio = diz_lista[meta]
                if punto_medio == w.lower():
                    trovata = True
                    break
                elif punto_medio > w.lower():
                    fine = meta -1
                else:
                    inizio = meta + 1
            rw._corretta = trovata
            risultato.append(rw)
        return risultato





