def diceThrows(numDice, numSides, target):
    mat = [[0 for _ in range(target + 1)] for k in range(numDice + 1)]
    mat[0][0] = 1
    for i in range(1, numDice + 1):
        for j in range(i , target + 1):
            if j > i * numSides:
                mat[i][j] = 0
            else:
                shift = min(j, numSides)
                temp = sum(mat[i-1][j-shift:j])
                mat[i][j] = temp

    return mat[-1][-1]

if __name__ == '__main__':
    print(diceThrows(3,6,7))