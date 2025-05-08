pizzas = ["Quattro Stagioni", "Margerita", "Calzone"]
friend_pizzas = pizzas[:]
#print(pizzas)          # ['Quattro Stagioni', 'Margerita', 'Calzone']
#print(friend_pizzas)   # ['Quattro Stagioni', 'Margerita', 'Calzone']

pizzas.append("Alaska")
friend_pizzas.append("Porcini")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
for pizza in friend_pizzas:
    print(pizza)