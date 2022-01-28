import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/processed/resultat.csv')
Taille = df['Taille']
SF = df['SF']
BanPass = []
tauxRedon= df['CodingRate']
TOA = df['TOA']
v = 0

for i in range(0, df.shape[0]):
    if df.iloc[i,9] == 250 or df.iloc[i,9] == 125:
        BanPass.append(df.iloc[i,9])
    else:
        df.drop([i,9])

v = Taille / TOA
print(BanPass)

#Vitesse et SF
plt.title("Vitesse de transmission théorique des données en fonction du facteur d'étalement")
x = SF
y = v
plt.plot(x,y)
plt.xlabel("Facteur d'étalement")
plt.ylabel("Vitesse")
plt.show()

#Vitesse et bande passante
plt.title("Vitesse de transmission théorique des données en fonction de la bande passante")
plt.plot(BanPass, y)
y = v

plt.xlabel("Bande passante")
plt.ylabel("Vitesse")
plt.show()

#Vitesse et taux de redondance
plt.title("Vitesse de transmission théorique des données en fonction du taux de redondance")
x = tauxRedon
y = v
plt.plot(x,y)
plt.xlabel("Taux de redondance")
plt.ylabel("Vitesse")
plt.show()

