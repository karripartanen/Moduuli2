import math

Base = input("Lasketaan suorakulmion piiri ja pinta-ala. Antaisitko suorakulmion kannan pituuden senttimetreissä(cm)?")
LengthStr = float(Base)
Height = input("Antaisitko suorakulmion korkeuden senttimetreissä(cm)?")
HeightStr = float(Height)
#kysyy arvot käyttäjältä ja asettaa ne muuttujiin myöhempää laskutoimitusta varten
RecArea = (LengthStr*HeightStr)
RecPerimeter = (2*LengthStr)+(2*HeightStr)
input("Suorakulmion pinta-ala on "+str(RecArea)+" neliösenttimetriä, ja piiri on "+str(RecPerimeter)+" senttimetriä")
