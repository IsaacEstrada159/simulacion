from random import randint
import matpotlib.pyplot as plt

humedadtierra = []
lluvia = []
humedadaire = []
temperatura = []
x = []

for i in range(50):
    humedadtierra.append(randint(81,86))
    lluvia.append(randint(0,9))
    humedadaire.append(randint(65,69))
    temperatura.append(randint(25,28))
    x.append(i)

plt.plot(x, temperatura)
plt.plot(x, lluvia)
plt.plot(x, humedadaire)
plt.plot(x, humedadtierra)