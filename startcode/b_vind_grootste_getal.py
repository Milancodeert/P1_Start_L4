# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.

getallenLijst = []
Cijfer1 =(input("Ik ga je vragen om 5 getallen te typen! begin met een cijfer te typen! "))
Cijfer2 =(input("Nu een ander cijfer! "))
Cijfer3 =(input("Nog een ander cijfer! "))
Cijfer4 =(input("Nog een ander cijfer! "))
Cijfer5 =(input("Nog een ander cijfer! "))
getallenLijst.append(Cijfer1)
getallenLijst.append(Cijfer2)
getallenLijst.append(Cijfer3)
getallenLijst.append(Cijfer4)
getallenLijst.append(Cijfer5)

def vind_grootste_getal_traag(getallenLijst):
    if(len(getallenLijst)<1):
        print("list too short")
        getallenLijst.sort()
        print(getallenLijst[0])






