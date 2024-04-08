article = """título: Experiences in Developing a Distributed Agentbased Modeling Toolkit with Python Version 3
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented
details of large-scale complex systems. However, the specialized
knowledge required for developing such ABMs creates barriers to wider
adoption and utilization. Here we present our experiences in
developing an initial implementation of Repast4Py, a Python-based
distributed ABM toolkit. We build on our experiences in developing ABM
toolkits, including Repast for High Performance Computing (Repast
HPC), to identify the key elements of a useful distributed ABM
toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the
largest HPC resources and emerging computing architectures."""
titulo = article.split("\n")[0].split()
titulo.pop(0)
if (len(titulo) <= 10):
    print ("Titulo: ok")
else:
    print ("Titulo: not ok")
resumen = article.split("\n")
resumen.pop(0)
resumen = "".join(resumen)
resumen = resumen.split(".")
print (resumen)
cantOraciones = {"faciles de leer":0,"aceptables de leer":0,"dificil de leer":0,"muy dificil de leer":0}
for oracion in resumen:
    palabras = oracion.split()
    if (len(palabras) == 12):
        cantOraciones["faciles de leer"] += 1
    elif (len(palabras) >= 13 and len(palabras) <= 17):
        cantOraciones["aceptables de leer"] += 1
    elif (len(palabras) >= 18 and len(palabras) <= 25):
        cantOraciones["dificil de leer"] += 1
    else:
        cantOraciones["muy dificil de leer"] += 1
print (cantOraciones)