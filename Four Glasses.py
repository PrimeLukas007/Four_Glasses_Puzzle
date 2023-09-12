import random

# 0 = sklenicka otocena dolu, 1 = sklenicka otocena nahoru
ring_condition = [0, 0, 0, 0]
ring_condition_2 = [1, 1, 1, 1]
# prazdny list glasses, pres randint pridame nahodne sklenicky
glasses = []
while len(glasses) < 4:
    glasses.append(random.randint(0, 1))


def shuffle_square(square):
    diagonal_indices = [0, 3]
    diagonal_elements = [square[i] for i in diagonal_indices]
    random.shuffle(diagonal_elements)
    for i, idx in enumerate(diagonal_indices):
        square[idx] = diagonal_elements[i]
    return square


def puzzle_solver(glasses):
    if ring_condition == glasses or ring_condition_2 == glasses:
        # print("Vyhrál jsi!")
        return glasses

# nejdrive vezmeme nahodne sklenicky, pokud nektera z nich je otocena dolu, otocime ji nahoru, po tomto kroku musi byt 2/4 sklenicek otoceno nahoru
    if glasses[0] == 0:
        glasses[0] = 1
    if glasses[3] == 0:
        glasses[3] = 1

    # print(glasses)
    if ring_condition == glasses or ring_condition_2 == glasses:
        # print("Vyhrál jsi!")
        return glasses

    # print(str(glasses) + "1")
    glasses = shuffle_square(glasses)
# po tomto kroku jsou urcite 3/4 sklenicek otoceny nahoru
    if glasses[0] == 0:
        glasses[0] = 1
    if glasses[1] == 0:
        glasses[1] = 1

    # print(str(glasses) + "2")
    glasses = shuffle_square(glasses)

    if ring_condition == glasses or ring_condition_2 == glasses:
        # print("Vyhrál jsi!")
        return glasses

# po tomto kroku budou bud vsechny nahore, nebo budeme mit 2/4 nahore, s tim ze sklenicka bude vzdy vedle sebe mit dalsi sklenicku otecenou stejne
    if glasses[0] == 0:
        glasses[0] = 1

    if ring_condition == glasses or ring_condition_2 == glasses:
        # print("Vyhrál jsi!")
        return glasses

    if glasses[3] == 0:
        glasses[3] = 1
    elif glasses[3] == 1:
        glasses[3] = 0
    elif glasses[0] == 0:
        glasses[0] = 1

    if ring_condition == glasses or ring_condition_2 == glasses:
        # print("Vyhrál jsi!")
        return glasses

    # print(str(glasses) + "3")
    glasses = shuffle_square(glasses)
    # po tomto bujd vyhrajeme nebo budeme mit vzdy ty same na diagonale

    if glasses[0] == 0:
        glasses[0] = 1
    elif glasses[0] == 1:
        glasses[0] = 0

    if glasses[1] == 0:
        glasses[1] = 1
    elif glasses[1] == 1:
        glasses[1] = 0
    # print(str(glasses) + "4")
    glasses = shuffle_square(glasses)

    if ring_condition == glasses or ring_condition_2 == glasses:
        # print("Vyhrál jsi!")
        return glasses

    if glasses[0] == 0:
        glasses[0] = 1
    elif glasses[0] == 1:
        glasses[0] = 0

    if glasses[3] == 0:
        glasses[3] = 1
    elif glasses[3] == 1:
        glasses[3] = 0
    # print(str(glasses) + "5")
    glasses = shuffle_square(glasses)

    if ring_condition == glasses or ring_condition_2 == glasses:
        # print("Vyhrál jsi!")
        return glasses
    print("Prohral jsi!")


counter = 0
while True:
    glasses = []
    while len(glasses) < 4:
        glasses.append(random.randint(0, 1))
    print(glasses)
    print(puzzle_solver(glasses))
    if glasses != ring_condition and glasses != ring_condition_2:
        print("Error")
        break
    else:
        print("OK")
    if counter == 5000:
        break
    counter += 1
