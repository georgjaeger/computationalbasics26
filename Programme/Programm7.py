import matplotlib.pyplot as plt 
import random


simulationszeit = 100
windkraft_anzahl = 30
wasserkraft_anzahl = 1

wasserkraft_liste = []
windkraft_liste = []
kohlekraft_liste = []
verbrauch_liste = []

for zeit in range(simulationszeit):
    verbrauch_liste.append(150)
    wasserkraft = wasserkraft_anzahl * 100 * random.gauss(1, 0.1)
    wasserkraft_liste.append(wasserkraft)
    windkraft = 0
    for kraftwerke in range(windkraft_anzahl):
        if random.uniform(0, 100) <= 50:
            # STÖRUNG: kein Strom wird produziert
            windkraft = windkraft + 0
        else:
            # Normalbetrieb: 
            windkraft = windkraft + random.uniform(0, 7)
    windkraft_liste.append(windkraft)
    
    kohlekraft= random.choice((0, 20, 70))
    kohlekraft_liste.append(kohlekraft)

plt.stackplot(range(simulationszeit), kohlekraft_liste, wasserkraft_liste, windkraft_liste,
              colors=('black','darkblue','skyblue'))

# erstes Element der verbrauch_liste auf 200 setzen:
verbrauch_liste[0]=200
# shuffeln der gesamten Liste
random.shuffle(verbrauch_liste)

plt.plot(verbrauch_liste, c = "red", lw = 2)
plt.show()