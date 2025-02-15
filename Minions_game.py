def sortare(lista):
    lista.sort(key=len)


def extrage_punctaj(lista):
    return len(lista)


def minion_game(cuvant):
    vocale = ['A', 'E', 'I', 'O', 'U']
    consoane = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'Z']
    kevin = []

    for i in range(0, len(cuvant)):
        if cuvant[i] in vocale:
            temp = ''
            for j in range(i, len(cuvant)):
                temp = temp + cuvant[j]
                kevin.append(temp)
    sortare(kevin)

    stuart = []

    for i in range(0, len(cuvant)):
        if cuvant[i] in consoane:
            temp = ''
            for j in range(i, len(cuvant)):
                temp = temp + cuvant[j]
                stuart.append(temp)
    sortare(stuart)

    if (extrage_punctaj(kevin) > extrage_punctaj(stuart)):
        print('Kevin', extrage_punctaj(kevin))
    elif (extrage_punctaj(stuart) > extrage_punctaj(kevin)):
        print('Stuart', extrage_punctaj(stuart))
    else:
        print(extrage_punctaj(kevin), extrage_punctaj(stuart))


if __name__ == '__main__':
    # s = input()
    minion_game('BANAAANA')
# incearca cuvantul BANAANAS
