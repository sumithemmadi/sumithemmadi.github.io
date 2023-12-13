def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 0:
        char1 = matr[e1r][4]
    else:
        char1 = matr[e1r][e1c-1]

    char2 = ''
    if e2c == 0:
        char2 = matr[e2r][4]
    else:
        char2 = matr[e2r][e2c-1]

    return char1, char2


def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 0:
        char1 = matr[4][e1c]
    else:
        char1 = matr[e1r-1][e1c]

    char2 = ''
    if e2r == 0:
        char2 = matr[4][e2c]
    else:
        char2 = matr[e2r-1][e2c]

    return char1, char2


def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2


def decryptByPlayfairCipher(Matrix, cipherList):
    PlainText = []
    for i in range(0, len(cipherList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, cipherList[i][0])
        ele2_x, ele2_y = search(Matrix, cipherList[i][1])

        if ele1_x is not None and ele2_x is not None:
            if ele1_x == ele2_x:
                c1, c2 = decrypt_RowRule(
                    Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            elif ele1_y == ele2_y:
                c1, c2 = decrypt_ColumnRule(
                    Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = decrypt_RectangleRule(
                    Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            continue

        plaintext = c1 + c2
        PlainText.append(plaintext)

    PlainText = ''.join(PlainText).replace('x', '')

    return PlainText


def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText


def Box(text):
    Box = []
    group = 0
    for i in range(2, len(text), 2):
        Box.append(text[group:i])
        group = i
    Box.append(text[group:])
    return Box


def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if (mat[i][j] == element):
                return i, j
    return None, None


def encrypt_text():
    with open('ciphertext.txt', 'r') as file:
        cipherText = file.read()

    cipherText = cipherText.lower()
    CipherTextList = Box(cipherText)

    key = "sumith"
    key = key.lower()
    Matrix = generateKeyTable(key, list1)

    PlainText = decryptByPlayfairCipher(Matrix, CipherTextList)

    with open('recover.txt', 'w') as file:
        file.write(PlainText)

    print("Decrypted Text:", PlainText)
