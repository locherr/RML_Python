"""pizzas = ["Quattro Stagioni", "Funghi", "Calzone"]

for pizza in pizzas:
    print(f" I like {pizza} pizza")
print("I really love pizza")

reptiles = ["Kreuzotter", "Eidechse", "Ringelnatter"]
for reptile in reptiles:
    print(reptile)

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

squares = [i ** 2 for i in range(1,11)]
print(squares)

numbers = [i for i in range(1,21)]
print(numbers)

hundred = [i for i in range(1,101)]
print(hundred)
print(min(hundred))
print(max(hundred))

uneven = [i for i in range(1,101,2)]
print(uneven)

threes = [i for i in range(3, 31, 3)]
print(threes)


cubes = [i ** 2 for i in range(1, 11)]
print(cubes)
"""

reptiles = ["Kreuzotter", "Eidechse", "Ringelnatter", "Krokodil", "Blindschleiche"]

print(f" The first three items in the list are {reptiles[0:3]}")
print(f" Three reptiles from the middle of the list are {reptiles[1:-1]}")
print(f" The last three reptiles in the list are {reptiles[-3:]}")