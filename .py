class Skolotajs:
    def __init__(self,stundas, uzvards):
        self.st = None
        self.uzvards = uzvards
        self.stundas = stundas
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self,  uzvards, klase, stundas ):

        self.st = 1
        self.uzvards = uzvards
        self.stundas = stundas
        self.klase = klase
    def izvade(self):
        print(f"Sākumskolas (tips – {self.st}) skolotājs {self.uzvards} māca {self.stundas} stundas {self.klase} klasē.")
class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, ppn,  ssn2, opn, ssn1):
        self.ppn = ppn
        self.ssn1 = ssn1
        self.opn = opn
        self.ssn2 = ssn2
        self.st = 3
        self.uzvards = uzvards
    def ssnk(self):
        return int(self.ssn1) + int(self.ssn2)
    def izvade1(self):
        print(f"Vidusskolas (tips – {self.st}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.ppn} un {self.opn}, kopā {self.ssnk()} stundas.")
    
def sakumskolas_skolotajs():
    uzvards = input("Ievadiet sākumsskolas skolotāja uzvārdu: ")
    klase = input("Ievadiet skolotāja klasi: ")
    stundas = int(input("Ievadiet skolotāja stundu skaitu: "))
    skolotajs = SakumskolasSkolotajs(uzvards, klase, stundas)
    skolotajs.izvade()
def vidusskolas_skolotajs():
    uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
    ppn = input("Ievadiet pirmo pasniegto priekšmetu: ")
    ssn1 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    opn = input("Ievadiet otro pasniegto priekšmetu: ")
    ssn2 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    skolotajs = VidusskolasSkolotajs(uzvards, ppn, ssn1, opn, ssn2)
    skolotajs.izvade1()

sakumskolas_skolotajs()
vidusskolas_skolotajs()