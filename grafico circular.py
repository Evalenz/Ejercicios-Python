import matplotlib.pyplot as plt

tamanos = (40, 20, 25, 15)
colores = ("blue", "orange", "green", "red")
etiquetas = ("Python", "Java", "C++", "JavaScript")

plt.pie(tamanos, colors=colores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
plt.title("Lenguajes de programación más populares en 2024")
plt.show ()


