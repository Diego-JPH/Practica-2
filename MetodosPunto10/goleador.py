def recorrido(dictionary):
    maxGoals = 0
    for key,value in dictionary.items():
        if (value[0] >= maxGoals):
            name = key
            maxGoals = value[0]
    return name,maxGoals