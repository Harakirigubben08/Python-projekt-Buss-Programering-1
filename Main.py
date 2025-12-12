"""
------------------------------- Information --------------------------------

Titel: Bussen
Författare:Emil och Vilgot Su.
Datum: 2025/02/29
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista(Det kan ju en apa förstå).
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand
import math as meth
from Randompassagerarlistor import*

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
    def __init__(self, namn, catchphrase, busighet, ålder):
        self.namn = namn
        self.ålder = ålder
        self.busighet = busighet
        self.catchphrase = catchphrase

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"{self.namn}.\n Min catchphrase är ({self.catchphrase}). \n ({self.busighet}) busig på skalan 0-1 \n ({self.ålder}) år gammal.\n"

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
    
    def getCatchphrase(self):
        return self.catchphrase

#-------------------------Hjälpfunktionsdefiitioner---------------------------#

#Funktionen som låter operatören lägga in helt egna passagerare
def Egenplockaupp(buss):
        namn = Hanteradinput(str,"Vad heter karaktären?-->")
        catchphrase = Hanteradinput(str,"Vad är karaktärens Catchphrase?-->")
        busighet = float(input("På en skala 0-1 hur busig är karaktären? -->"))
        if busighet < 0 or busighet > 1:
            raise ValueError 
        else:
            ålder= Hanteradinput(float,"Hur gammal är karaktären?-->")

        ny_passagerare=Person(namn,catchphrase,busighet,ålder) 
        buss.append(ny_passagerare)

        return buss 

#Funktionen som slumpar fram en ny passagerare ur ett antal listor
def Slumpplockaupp(buss):
    namn = rand.choice(Förnamn) + rand.choice(Efternamn)
    catchphrase = rand.choice(Catchphrase)
    busighet = rand.choice(Busighet)
    ålder = rand.randint(0, 155)
    ny_passagerare=Person(namn,catchphrase,busighet,ålder)
    print(ny_passagerare)
    buss.append(ny_passagerare)
    
    return buss     


# Plockar in en felhanterad input, kräver vilken variabeltyp samt vad man vill veta
def Hanteradinput(variabeltyp, fråga):
    while True:
        try:
            svar = input(f"{fråga}") 
            if variabeltyp == int:
                rätt=int(svar)
                return rätt
            elif variabeltyp == str:
                rätt =str(svar)
                return rätt
            elif variabeltyp == float:
                rätt = float(svar)
                return rätt
            elif variabeltyp == bool:
                rätt = bool(svar)
                return rätt
            else:
                print("läs frågan och svara rätt din mupp!!!")
        except ValueError:
            print("Gör rätt din mupp!!!")

# Sorterar bussen efter ålder
def åldersortera(buss):
    åldrar=[]

    for i in range:
    
        print("hejsan")
        a += 1



# ------------------------- Funktionsdefinitioner ---------------------------- #    

# Lägger till en ny person i bussen.
def plockaUpp(buss):
    Generationsalt = Hanteradinput(int,"1 för att skapa egen karaktär 2 för att slumpa fram en.--> ")
    if Generationsalt == 1:
        Egenplockaupp(buss)
        return(buss)
    elif Generationsalt == 2:
        Slumpplockaupp(buss)
        return(buss)
    else:
        print("SYNTAX ERROR, Gör om gör rätt")
        return(buss)
        
    

# Avlägsnar en person från bussen.
def gåAv(buss):
    print(skrivUt(buss))
    attgåav = Hanteradinput(int,"Se listan ovan, Vem ska gå av? välj nummer --> ")
    del(buss[attgåav]) 
    return buss

# Listar alla passagerare på bussen.
def skrivUt(buss):
    a = len(buss)
    for i in range(a):
        print(f"Bussens passagerare nr:{i+1} är, {buss[i-1]} \n")
        i +=1

    return

# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagdÅlder(buss):
    total_ålder = 0
    for passagerare in buss:
        total_ålder += int(passagerare.getÅlder())
    return total_ålder

# Skriver ut medelåldern på passagerarna i bussen.
def medelÅlder(buss):
    total_ålder = 0
    for passagerare in buss:
        total_ålder += int(passagerare.getÅlder())
    medel_ålder = total_ålder/len(buss)
    return medel_ålder
    

# Skriver ut personen som är äldst på bussen.
def äldst(buss):
    äldsta_passagerare = buss[0]
    for passagerare in buss:
        if int(passagerare.getÅlder()) > int(äldsta_passagerare.getÅlder()):
            äldsta_passagerare = passagerare
    return äldsta_passagerare


# Sorterar bussen, antingen efter busighet eller efter ålder.
def sort_buss(buss):
    hursortera = Hanteradinput(str,("Vill du sortera listan med Namn eller ålder (n/å)? --> "))
    
    if hursortera == "n":

        pass

    elif  hursortera == "å":   
        buss =åldersortera(buss)

        return(buss)
    else:
        print("Hur svårt kan det vara??")
        return buss


    
    
                


    


# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hitta_passagerare(buss):
    ålderspannövre = Hanteradinput(int,"Vad är maxåldern på passageraren??--> ")
    ålderspannlägre = Hanteradinput(int,"Vad är den lägsta ålder?--> ")
    if ålderspannövre > ålderspannlägre and ålderspannövre < 122 and ålderspannlägre > 0:
        for i in range(len(buss)):  
           if buss[i]< ålderspannövre and buss[i] > ålderspannlägre:
               print (buss[i])
           else:
               i+=1 
               pass
        return buss
    else:
        print("Lär dig matte och mänsklig biologi!!!🤓☝️😋🙉")
        return buss
    
    return buss

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(buss):
    passagerarenr = Hanteradinput(int,f"Vilken passagerare vill du peta på? 1-{len(buss)}--> ")
    if passagerarenr < 0 or len(buss)< passagerarenr:
        print("Gör om, gör rätt..") 
        return
    else:
        person = buss[passagerarenr-1]
        print(person.catchphrase) 

    

        return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    p1 = Person("Marre Maräng", "Hurru du din marängskalle", 0.8, 13)
    p2 = Person("Virre", "Snurr snurr", 0.2, 19)
    p3 = Person("Lellegamer22", "Ima tuck you in real good!", 0.7, 9)
    p4 = Person("Lennart Bladh", "Hi again.", 0.9, 62 )
    
    
    buss = [p1,p2,p3,p4]
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                  2. Låt passagerare gå av
            3. Skriv ut alla passagerare                  4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                        6. Hitta äldst person
            7. Sortera bussen                             8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                        q. Avsluta
        ---------------------------------------------------------------------------------------
        """)


        menyVal = input("-> ")

        if menyVal == "1":
            if len(buss) < 25:
                buss = plockaUpp(buss)
                pass
            else: 
                print("bussen är full testa något annat")
                pass
        elif menyVal == "2":
            buss= gåAv(buss)
            pass
        elif menyVal == "3":
            skrivUt(buss)
            pass
        elif menyVal == "4":
            Åldertot = sammanlagdÅlder(buss)
            print(Åldertot)
            pass
        elif menyVal == "5":
            Åldersam = medelÅlder(buss)
            print(Åldersam)
            pass
        elif menyVal == "6":
            Ålderäld = äldst(buss)
            print(Ålderäld)
            pass
        elif menyVal == "7":
            Åldersort = sort_buss(buss)
            print(Åldersort)
            pass
        elif menyVal == "8":
            hitta_passagerare(buss)
            pass 
        elif menyVal == "9":
            peta(buss)
            pass   


main()