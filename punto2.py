from collections import Counter
texto = """NumPy is a community-driven open source project developed by a creating diverse group of contributors. The NumPy leadership has made
           a strong commitment to creating an open, inclusive, and positive community. Please read creating the NumPy Code of Conduct for 
           guidance on how to interact with others in a way that makes our community creating thrive."""
mayoresA4 = []
texto = texto.split()
for palabra in texto:
    cant = []
    for char in palabra:
        cant.append(char)
    if (len(cant) > 4):
        mayoresA4.append(palabra)
contador = Counter(mayoresA4)
print (mayoresA4)
print (contador.most_common(1)[0])
