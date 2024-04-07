import string
jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks, code, and data. JupyterLab is
flexible: configure and arrange the user interface to support a wide
range of workflows in data science, scientific computing, and machine
learning. JupyterLab is extensible and modular: write plugins that add
new components and integrate with existing ones. """
letra = str(input("Ingrese la letra: ")).lower()
if (letra in string.ascii_lowercase or letra in string.ascii_uppercase):
    for elem in jupyter_info.split():
        if (letra in elem.lower()):
            print (elem)
else:
    print ("El caracter ingresado no es una letra...")