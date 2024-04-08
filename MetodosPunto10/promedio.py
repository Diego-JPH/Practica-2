def totalGoals (dictionary):
    total = 0
    for goal in dictionary.values():
        total += goal[0]
    return total