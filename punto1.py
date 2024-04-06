texto = """NumPy is a community-driven open source project developed by a diverse group of contributors. The NumPy leadership has made
           a strong commitment to creating an open, inclusive, and positive community. Please read the NumPy Code of Conduct for 
           guidance on how to interact with others in a way that makes our community thrive."""
vocales = ["a","e","i","o","u"]
texto = texto.split("\n")
for linea in texto:
    parrafo = linea.split()
    segunda_palabra = parrafo[1]
    if segunda_palabra[0].lower() in vocales:
        print (linea) 