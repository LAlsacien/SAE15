import pandas as pd

# Lecture du fichier "resultat.csv et définition des variables :

df = pd.read_csv('..\..\data\processed\\resultat.csv')
pourcentage = 0
rvm = []
tvm = 0


# Calcul des valeurs manquantes par colonne :

for i in range(0, df.shape[1]):
    valeursmanquantes = (df.isnull().iloc[:,i] == True).sum()
    rvm.append(valeursmanquantes)
    tvm += valeursmanquantes

# Pourcentage des valeurs manquantes par colonne :

for i in range(0, df.shape[1]):
    pourcentage = rvm[i] / df.shape[0] * 100
    rvm[i] = (round(pourcentage,2))
    if pourcentage != 0:
        print(f"Il y a {rvm[i]}% de valeurs manquantes dans la la colonne {i}")
    else:
        continue

# Total et pourcentage des valeurs manquantes :

print("\n")
print(f"Il y a au total {tvm} valeurs manquantes dans le fichier \"resultat.csv\".")
print(f"Cela représente un pourcentage de {round(tvm / ((df.shape[1] * df.shape[0])) * 100, 3)}%.")