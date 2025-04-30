texto_original = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""

texto_original = texto_original.upper()

for letra in texto_original:
    if "A" <= letra <= "Z":  # Se for uma letra maiúscula
        if letra == "A":
            texto_criptografado += "I"
        elif letra == "E":
            texto_criptografado += "O"
        elif letra == "I":
            texto_criptografado += "U"
        elif letra == "O":
            texto_criptografado += "A"
        elif letra == "U":
            texto_criptografado += "E"
        elif letra == "B":
            texto_criptografado += "H"
        elif letra == "C":
            texto_criptografado += "J"
        elif letra == "D":
            texto_criptografado += "K"
        elif letra == "F":
            texto_criptografado += "L"
        elif letra == "G":
            texto_criptografado += "M"
        elif letra == "H":
            texto_criptografado += "N"
        elif letra == "J":
            texto_criptografado += "P"
        elif letra == "K":
            texto_criptografado += "Q"
        elif letra == "L":
            texto_criptografado += "R"
        elif letra == "M":
            texto_criptografado += "S"
        elif letra == "N":
            texto_criptografado += "T"
        elif letra == "P":
            texto_criptografado += "V"
        elif letra == "Q":
            texto_criptografado += "W"
        elif letra == "R":
            texto_criptografado += "X"
        elif letra == "S":
            texto_criptografado += "Y"
        elif letra == "T":
            texto_criptografado += "Z"
        elif letra == "V":
            texto_criptografado += "B"
        elif letra == "W":
            texto_criptografado += "C"
        elif letra == "X":
            texto_criptografado += "D"
        elif letra == "Y":
            texto_criptografado += "F"
        elif letra == "Z":
            texto_criptografado += "G"
    elif letra == " ":
        texto_criptografado += "-"
    else:
       texto_criptografado += letra  # Mantém caracteres inalterados
print(texto_original)
print(texto_criptografado)