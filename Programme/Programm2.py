import matplotlib.pyplot as plt #wir importieren das Modul matplotlib.pyplot und geben ihm die Abkürzung plt
# die nächste Zeile bewirkt, dass die Grafiken direkt in der Zelle angezeigt werden

simulationszeit = 30
#simulationszeit: Die Zeit in Jahren, die der Froschteich simuliert wird

froschanzahl = 0
froschanzahl_liste = [] #leere Liste wird erstellt
froschanzahl_liste.append(froschanzahl) #erster Eintrag (0 Frösche) wird angehängt

for it in range(simulationszeit):    
    froschanzahl = froschanzahl + 3
    #am Ende jedes Schleifendurchgangs wird die aktuelle Zahl an die Liste angehängt
    froschanzahl_liste.append(froschanzahl) 

plt.plot(froschanzahl_liste)
plt.plot(froschanzahl_liste, color = 'green')
plt.xlabel('Zeit (Jahre)')
plt.ylabel('Frösche')
plt.show()