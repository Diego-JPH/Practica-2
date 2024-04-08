def calcularMasInfluyente(dictionary):
    goalsInFavor = lambda x: x * 1.5
    goalsAvoided = lambda x: x * 1.25
    maxPoints = 0
    for key, value in dictionary.items():
        points = 0
        points += goalsInFavor(value[0])
        points += goalsAvoided(value[1])
        points += value[2]
        if (points >= maxPoints):
            name = key
            maxPoints = points
    return name