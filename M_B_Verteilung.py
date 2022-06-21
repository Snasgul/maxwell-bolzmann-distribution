import matplotlib.pyplot as plt
import math
import scipy.constants
import chemics.atomic_elements as elements
import numpy as np


def Maxwell_Bolzmann_Distribution(v, u, T):
    m = u / 1000 / scipy.constants.N_A
    value = (4 * math.pi *((m / (2 * math.pi * scipy.constants.k * T)) ** (3 / 2)) * (v ** 2) * (math.exp(1) ** (-(m * (v ** 2) / (2 * scipy.constants.k * T)))))
    return(value)


#j = int(input("j: "))

element = ['H', 'N', 'N', 'N']

temperature = [100, 300, 800, 1600]

data = [[], [], [], []]
average = 0

for i in np.arange(0, 3000, 0.1):
    data[0].append(Maxwell_Bolzmann_Distribution(i, elements[element[0]]['atomic_weight'] * 2, temperature[0]))
    data[1].append(Maxwell_Bolzmann_Distribution(i, elements[element[1]]['atomic_weight'] * 2, temperature[1]))
    data[2].append(Maxwell_Bolzmann_Distribution(i, elements[element[2]]['atomic_weight'] * 2, temperature[2]))
    data[3].append(Maxwell_Bolzmann_Distribution(i, elements[element[3]]['atomic_weight'] * 2, temperature[3]))
    #average += Maxwell_Bolzmann_Distribution(i, elements[element[j]]['atomic_weight'] * 2, temperature[j]) * i


#peak = data[j].index(max(data[j]))

#print("Average: " + str(average))
#print("Peak: " + str(peak))

#print("Proportion: " + str(average / peak))
# 1.1283778743458106

# 1.1283686116823386

# 1.1267038055393825

# 1.1267038055393825
# 1.1283602124388628
# 1.1285618339912824
# 1.1278397545504426

plt.grid(True)
plt.title("Maxwell-Bolzmann-Distribution")
plt.xlabel("Velocity")
plt.ylabel("Relative frequency density")

plt.plot(data[0], '-', label="Hydrogen with " + str(temperature[0]) + "K")
plt.plot(data[1], '-', label="Nitrogen with " + str(temperature[1]) + "K")
plt.plot(data[2], '-', label="Nitrogen with " + str(temperature[2]) + "K")
plt.plot(data[3], '-', label="Nitrogen with " + str(temperature[3]) + "K")
plt.legend()

plt.show()