frase = str(input("Ingrese la frase: "))
string = str(input("Ingrese el string a analizar: "))
contador = 0
for palabra in frase.split():
    if (string.lower() in palabra.lower()):
        contador += 1
print ("Coincidencias: ",contador)