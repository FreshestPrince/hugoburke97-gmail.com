import random


def rouletteWheelFitnessSelection(choices):
    max = sum(choices)
    pick = random.uniform(0, max)
    current = 0
    for key, value in enumerate(choices):
        current += value
        if current > pick:
            parent1 = key
            parent2 = key
            break
    while (parent1 == parent2):
        pick = random.uniform(0, max)
        current = 0
        for key, value in enumerate(choices):
            current += value
            if current > pick:
                parent2 = key
                break
    return parent1, parent2

fitness = [9,12,13,41,51]
a, b = rouletteWheelFitnessSelection(fitness)
print(a, b)
