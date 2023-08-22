import math

Radius = input("Hei, lasketaan ympyrän pinta-ala. Antaisitko ympyrän säteen senttimetreinä:")
RadiusStr = float(Radius)
'#declares the variable as the radius asked from the user'
CircleArea = (math.pi*(RadiusStr**2)) # Calculates area of the circle with given radius
print("Ympyrän pinta-ala on "+str(CircleArea)+" neliösenttimetriä.")
