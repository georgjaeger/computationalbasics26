import matplotlib.pyplot as plt


def mischen(aktuell,start,verlust):
    neu = 0.5 * (start + aktuell * verlust)
    return neu


def recyceln(verlustparameter, startreinheit):
    reinheit = startreinheit
    reinheit_liste = [reinheit]

    for it in range(10):
        reinheit = mischen(reinheit,startreinheit,verlustparameter)
        reinheit_liste.append(reinheit)


    plt.plot(reinheit_liste, label = verlustparameter)
    plt.legend()
    
    return reinheit_liste[-1]

print(recyceln(0.9,1.0))
print(recyceln(0.8,1.0))
print(recyceln(0.7,1.0))
plt.show()



#----------------------------------

def verschmutzen(startwert):
    return startwert + 10

def schmelzen(startwert):
    return startwert * 0.85

schadstoff = 0
schadstoff_liste = [schadstoff]
counter = 0

while schadstoff < 50:   
    schadstoff = schmelzen(verschmutzen(schadstoff))
    schadstoff_liste.append(schadstoff)
    counter = counter + 1
    
plt.plot(schadstoff_liste)
plt.show()

print("Nach")
print(counter)
print("Prozessen ist der Schadstoffgrenzwert überschritten.")