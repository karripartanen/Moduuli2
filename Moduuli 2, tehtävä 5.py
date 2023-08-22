Leiviska = input("Anna leiviskät")
LeivStr = float(Leiviska)
Naula = input("Anna naulat")
NaulaStr = float(Naula)
Luoti = input("Anna luodit")
LuotiStr = float(Luoti)

MassaKg = ((LeivStr*(20*(32*0.0133))+(NaulaStr*(32*0.0133))+(LuotiStr*0.0133))) #laskee massat yhteen ja muuntaa ne kiloiksi
MassaG = (MassaKg*1000) #muuntaa kilot grammoiksi
MassaKilo = 0
while MassaG > 1000: #Credit: Matias
    MassaKilo +=1
    MassaG -= 1000
print("Antamiesi arvojen paino kiloissa on yhteensä "+str(MassaKilo)+" kiloa ja "+str(MassaG)+" grammaa")
