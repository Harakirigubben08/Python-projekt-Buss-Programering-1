"""
------------------------------- Information --------------------------------

Titel: Bussen
Författare:Emil och vilgot
Datum: en kväll i juni
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista(Det kan ju en apa förstå).
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand

print("Hej")
# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    """ Person är en klass för att representera personer i bussen. Varje objekt
    som skapas ur klassen har ett namn och en ålder, samt metoder för att returnera
    alternativt modifiera respektive attribut. """
    def __init__(self, namn, busighet, catchphrase, ålder):
        self.namn = namn
        self.ålder = ålder
        self.busighet = busighet
        self.catchphrase = catchphrase

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Det här är {self.namn}. Hen är {self.ålder} år gammal."

    # Setters
    def setNamn(self, nyttNamn):
        self.namn = nyttNamn

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    # Getters
    def getNamn(self):
        return self.namn

    def getÅlder(self):
        return self.ålder

# ------------------------- Funktionsdefinitioner ---------------------------- #

# Lägger till en ny person i bussen.
def plockaUpp(passagerare):
    return

# Avlägsnar en person från bussen.
def gåAv(passagerare):
    return

# Listar alla passagerare på bussen.
def skrivUt():
    return

# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagdÅlder():
    return

# Skriver ut medelåldern på passagerarna i bussen.
def medelÅlder():
    return

# Skriver ut personen som är äldst på bussen.
def äldst():
    return

# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def busSort():
    return

# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hittaPassagerare(åldersSpann):
    return

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(passagerare):
    return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    passagerare = []
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            4. Beräkna medelåldern                              5. Hitta äldst person
            6. Sortera bussen                                   7. Hitta personer inom ett specifikt åldersspann
            8. Peta på passagerare                              q. Avsluta
        ---------------------------------------------------------------------------------------
        """)
        print(
        """
                         _____________     _____________                              /
                       _/_|[][][][][] |   /|[][][][][][]\    |       Transport       /
                      (      Bussen   |  / Djurtransport \   |______________________/
                      =--OO-------OO--=@--=-OO--------OO--=-@--OO--------------OOO--|
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            pass
        elif menyVal == "2":
            pass
        elif menyVal == "3":
            pass
        elif menyVal == "4":
            pass
        elif menyVal == "5":
            pass
        elif menyVal == "6":
            pass
        elif menyVal == "7":
            pass
        elif menyVal == "8":
            pass 



main()