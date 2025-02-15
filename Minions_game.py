def minion_game(cuvant):
    vocale = ['A', 'E', 'I', 'O', 'U']
    consoane = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'Z']
    kevin = []
    cuvant_list=list(cuvant)
    print(cuvant_list)
    '''
    for c in vocale:
        if c in cuvant:
            temp = ''
            for x in range(cuvant.index(c), len(cuvant)):
                temp = temp + cuvant[x]
                kevin.append(temp)

    kevin.sort(key=len)

    scor_kevin = 0

    for temp in kevin:
        start = 0
        while True:
            index = cuvant.find(temp, start)
            if index == -1:
                break
            scor_kevin = scor_kevin + 1
            start = index + 1

    scor_stuart = 0
    start_stuart = 0
    stuart = []
    for c in consoane:
        if c in cuvant:
            temp = ''
            for x in range(cuvant.index(c), len(cuvant)):
                temp = temp + cuvant[x]
                stuart.append(temp)
    stuart.sort(key=len)

    scor_stuart = 0

    for temp in stuart:
        start = 0
        while True:
            index = cuvant.find(temp, start)
            if index == -1:
                break
            scor_stuart = scor_stuart + 1
            start = index + 1

    if max(scor_kevin, scor_stuart) == scor_kevin:
        print("Kevin", scor_kevin)
    else:
        print("Stuart", scor_stuart)

'''
if __name__ == '__main__':
    #s = input()
    minion_game('BANANA')
# incearca cuvantul BANAANAS
