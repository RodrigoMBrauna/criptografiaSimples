texto_criptografado = input("Digite o texto a ser descriptografado: ")
texto_original = ""

texto_criptografado = texto_criptografado.upper()

for letra in texto_criptografado:
    if "A" <= letra <= "Z":  # Se for uma letra maiúscula
        if letra == "I":
            texto_original += "A"
        elif letra == "O":
            texto_original += "E"
        elif letra == "U":
            texto_original += "I"
        elif letra == "A":
            texto_original += "O"
        elif letra == "E":
            texto_original += "U"
        elif letra == "H":
            texto_original += "B"
        elif letra == "J":
            texto_original += "C"
        elif letra == "K":
            texto_original += "D"
        elif letra == "L":
            texto_original += "F"
        elif letra == "M":
            texto_original += "G"
        elif letra == "N":
            texto_original += "H"
        elif letra == "P":
            texto_original += "J"
        elif letra == "Q":
            texto_original += "K"
        elif letra == "R":
            texto_original += "L"
        elif letra == "S":
            texto_original += "M"
        elif letra == "T":
            texto_original += "N"
        elif letra == "V":
            texto_original += "P"
        elif letra == "W":
            texto_original += "Q"
        elif letra == "X":
            texto_original += "R"
        elif letra == "Y":
            texto_original += "S"
        elif letra == "Z":
            texto_original += "T"
        elif letra == "B":
            texto_original += "V"
        elif letra == "C":
            texto_original += "W"
        elif letra == "D":
            texto_original += "X"
        elif letra == "F":
            texto_original += "Y"
        elif letra == "G":
            texto_original += "Z"
    elif letra == "-":
        texto_original += " "
    else:
       texto_original += letra  # Mantém caracteres alterados

print(texto_criptografado)
print(texto_original)