import matplotlib.pyplot as plt

plt.close()

days = [1,2,3,4,5]
temps = [23.5, 28.5, 17.5, 20.5, 18.9]
sizes = [23.5, 28.5, 17.5, 20.5, 18.9]
plt.scatter(x=days, y=temps, s=sizes)

plt.show()
