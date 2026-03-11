class Dictionary:
    def __init__(self):
        self.list = []

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as f:
            for riga in f:
                self.list.append(riga.strip().lower())

    def printAll(self):
        pass

    @property
    def dict(self):
        return self.list