# ๐จ Don't change the code below ๐
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# ๐จ Don't change the code above ๐

#Write your code below this line ๐
# On fait le calcul de l'imc
imc = round(weight / height ** 2)
# On affiche le rรฉsultat
print(f"Votre IMC est de {imc}")
