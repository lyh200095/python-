#4-1
pizzas=['p1','p2','p3','p4','p5']
for pizza in pizzas:
    print("I like "+pizza)
print("I really like pizza"+"!\n")

#4-2
pets=['dogs','cats','pigs']
for pet in pets:
    print("A "+pet+" would make a great pet.")
print("Any of these animals would make a great pet"+"!\n")

#4-3
for value in range(1,21):
    print(value)

#4-4
values=list(range(1,11))
for value in values:
    print(value)
print(values)

#4-5
values=list(range(1,11))
print(min(values))
print(max(values))
print(sum(values))

#4-6
values=list(range(1,20,2))
for value in values:
    print(value)

#4-7
values=list(range(3,31,3))
for value in values:
    print(value)

#4-8
sq=[]
for value in range(1,11):
    value=value**3
    sq.append(value)
print(sq)

#4-9
sq=[value**3 for value in range(1,11)]
print(sq)

#4-10
animals = ['cat','dog','bird','Hamster','rabbit']
print("The first three items in the list are:")
print(animals[0:3])
print("three items from the middle of the list are:")
print(animals[1:4])
print("The last three items in the list are:")
print(animals[2:5])

#4-11
friend_pizzas=pizzas[:]
pizzas.append('p6')
friend_pizzas.append('f7')
print("my favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

#4-12
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)
print("My friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)

#4-13
foods=('fd1','fd2','fd3','fd4','fd5')
for food in foods:
    print(food)
foods=('fd1','fd2','fd3','f4','f5')
for food in foods:
    print(food)