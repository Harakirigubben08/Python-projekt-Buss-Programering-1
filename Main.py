"""
------------------------------- Information --------------------------------

Titel: Bussen
Författare:Emil och vilgot
Datum: 2025/02/29
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista(Det kan ju en apa förstå).
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand

#-------------------------------Buss utskrivt-----------------------------------#

print(
        """
                         _____________     _____________                              /
                       _/_|[][][][][] |   /|[][][][][][]\    |       Transport       /
                      (      Bussen   |  / Djurtransport \   |______________________/
                      =--OO-------OO--=@--=-OO--------OO--=-@--OO--------------OOO--|
        """)

# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    """ Person är en klass för att representera personer i bussen. Varje objekt
    som skapas ur klassen har ett namn, cathcphrase, ålder, busighetsnivå samt metoder för att returnera
    alternativt modifiera respektive attribut. """
    def __init__(self, namn,catchphrase, busighet, ålder):
        self.namn = namn
        self.ålder = ålder
        self.busighet = busighet
        self.catchphrase = catchphrase

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Det här är {self.namn}.Dennes catchphrase är {self.catchphrase}. Hen är såhär busig på skalan 0-1 {self.busighet} Hen är {self.ålder} år gammal."

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
def plockaUpp(buss):
    namn = str(input ("namn -->"))
    catchphrase = str(input("Vad ska karaktärens Catchphrase vara?-->"))
    busighet = float(input("På en skala 0 till 5 hur busig är personen?-->"))
    ålder= input("Hur gammal är passageraren?")

    nypassagerare=Person(namn,catchphrase,busighet,ålder) 
    buss.append(nypassagerare)

    return buss 

# Avlägsnar en person från bussen.
def gåAv(buss):
    return

# Listar alla passagerare på bussen.
def skrivUt(buss):
    a = len(buss)
    for i in range(a):
        print(buss[i-1])
        i+=1

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
    p1 = Person("Marre Maräng", "Hurru du din marängskalle", 0.8, 13)
    p2 = Person("Virre", "Snurr snurr", 0.2, 19)
    p3 = Person("Virre", "Snurr snurr", 0.2, 19)
    p4 = Person("Virre", "Snurr snurr", 0.2, 19)
    p5 = Person("Virre", "Snurr snurr", 0.2, 19)
    p6 = Person("Virre", "Snurr snurr", 0.2, 19)
    p7 = Person("Virre", "Snurr snurr", 0.2, 19)
    p8 = Person("Virre", "Snurr snurr", 0.2, 19)
    p9 = Person("Virre", "Snurr snurr", 0.2, 19)
    p10 = Person("Virre", "Snurr snurr", 0.2, 19)
    p11 = Person("Virre", "Snurr snurr", 0.2, 19)
    p12 = Person("Virre", "Snurr snurr", 0.2, 19)
    p13 = Person("Virre", "Snurr snurr", 0.2, 19)
    p14 = Person("Virre", "Snurr snurr", 0.2, 19)
    p15 = Person("Virre", "Snurr snurr", 0.2, 19)
    p16 = Person("Virre", "Snurr snurr", 0.2, 19)
    p17 = Person("Virre", "Snurr snurr", 0.2, 19)
    p18 = Person("Virre", "Snurr snurr", 0.2, 19)
    p19 = Person("Virre", "Snurr snurr", 0.2, 19)
    p20 = Person("Virre", "Snurr snurr", 0.2, 19)
    p21 = Person("Virre", "Snurr snurr", 0.2, 19)
    p22 = Person("Virre", "Snurr snurr", 0.2, 19)
    p23 = Person("Virre", "Snurr snurr", 0.2, 19)
    p24 = Person("Virre", "Snurr snurr", 0.2, 19)
    p25 = Person("Virre", "Snurr snurr", 0.2, 19)
    
    
    
    buss = []
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                  2. Låt passagerare gå av
            3. Skriv ut alla passagerare                  4. Beräkna sammanlagd ålder
            4. Beräkna medelåldern                        5. Hitta äldst person
            6. Sortera bussen                             7. Hitta personer inom ett specifikt åldersspann
            8. Peta på passagerare                        q. Avsluta
        ---------------------------------------------------------------------------------------
        """)


        menyVal = input("-> ")

        if menyVal == "1":
            buss = plockaUpp(buss)
            pass
        elif menyVal == "2":
            buss= gåAv(buss)
            pass
        elif menyVal == "3":
            skrivUt(buss)
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