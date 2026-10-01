import matplotlib.pyplot as plt
import random


class Person:
    def __init__(self):
        #eine neue Person wird initialisiert
        
        #sie bekommt eine zufällig Heimadresse
        self.home = [random.randint(0,10),random.randint(0,10)]
        #und eine Arbeitsadresse aus einer Liste
        self.work = random.choice([[5,5],[5,5],[5,5],[4,1],[4,1],[7,9]])
        
    def zeichnen(self):
        #Die Personen zeichnen ihre Heimatadresse
        #s ist die Größe des Markers, die Form "s" steht für square
        plt.scatter(self.home[0],self.home[1], s = 100, marker = "s", c = "forestgreen")
        #Und ihren Arbeitsort
        plt.scatter(self.work[0],self.work[1], s = 100, marker = "s", c = "deepskyblue")
    
    def fahren(self):
        #Wir zeichnen zwei Linien:
        #Linie 1 geht in der x-Richtung von home nach work, y bleibt konstant bei home
        #Linie 2 geht in y-Richtung von home nach work, x bleibt konstant bei work
        plt.plot([self.home[0],self.work[0]],[self.home[1],self.home[1]],c = "black", alpha = 0.1, lw = 4)
        plt.plot([self.work[0],self.work[0]],[self.home[1],self.work[1]],c = "black", alpha = 0.1, lw = 4)
        
    def arbeitsweg(self):
        #der Weg errechnet sieh hier aus dem Abstand in x-Richtung + dem Abstand in y-Richtung
        dist = abs(self.home[0]-self.work[0]) + abs(self.home[1]-self.work[1])
        return dist
        
    def umziehen(self):
        #Methode um den Heimatort zu wechseln
        
        #wir speichern den aktuellen Weg und den aktuellen Heimatort
        alterweg = self.arbeitsweg()
        oldhome = self.home
        
        #die Person zieht auf ein zufällige Position um
        self.home = [random.randint(0,10),random.randint(0,10)]
        
        #Wenn der Weg dadurch länger geworden ist...
        if self.arbeitsweg() > alterweg:
            #... wird die Änderung rückgängig gemacht
            self.home = oldhome

            
def gesamtstrecke():
    #wir berechnen die Gesamtstrecke
    gesamt = 0
    #Wir gehen in einer Schleife über alle Personen
    for p in allepersonen:
        #und summieren die Arbeitswege
        gesamt = gesamt + p.arbeitsweg()
    
    print("Gesamtstrecke:")
    print(gesamt)
        
        
#----hier beginnt das eigentliche Programm----  
    
        
#Wir erstellen eine leere Liste
allepersonen=[]        

#Wir fügen neue Personen
for it in range(20):
    allepersonen.append(Person())

#Wir iterieren über alle Personen
for p in allepersonen:
    #Jede Person benutzt die Methode zeichnen und fahren
    p.zeichnen()
    p.fahren()
    
#Der Plot wird angezeigt    
plt.show()
#Die Gesamtstrecke wird berechnet
gesamtstrecke()

#Wir lassen die Personen umziehen
for it in range(10):
    for p in allepersonen:
        p.umziehen()
     
    
#Eine neue Figur wird erstellt         
plt.figure()

#Wieder wird gezeichnet und die Gesamtstrecke berechnet
for p in allepersonen:
    p.zeichnen()
    p.fahren()
plt.show()   
gesamtstrecke()