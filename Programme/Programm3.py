import matplotlib.pyplot as plt

temperatures = [35, 31, 33, 32, 30, 29, 27, 30, 31, 33, 31, 26, 28, 30]

heat_level = []
colors = []
for it in range(len(temperatures)):
    temp = temperatures[it]

    if temp < 28: #too cold -> green
        heat = 0
    elif temp > 32: #not too cold and hot -> red
        heat = 2
    elif heat_level[it - 1] == 2: #not too cold and not too hot and last day was red -> red
        heat = 2
    else: #not too cold and not too hot and last day was NOT red -> yellow
        heat = 1

    heat_level.append(heat)


    if heat == 0:
        colors.append('green')

    if heat == 1:
        colors.append('gold')

    if heat == 2:
        colors.append('red')

plt.scatter(range(len(temperatures)), temperatures, c=colors)
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.show()