#Déclarer la chaine de caractères suivante
chaine = "Durand; Marcel; 2 523.5"

print("-------------------------------")
premier_caractere = chaine[0]
print("Premier caractère:" + premier_caractere)

print("-------------------------------")

longueur_chaine = len(chaine)
print("la longueur de la chaine est:", longueur_chaine)

print("-------------------------------")

print(chaine.index(';'))

print("-------------------------------")

print(chaine[7:14])

print("-------------------------------")

print(chaine[7:14].upper())

print("-------------------------------")

print(chaine[7:14].lower())


print("-------------------------------")
print(chaine.split(';'))
