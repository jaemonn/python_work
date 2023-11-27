# 4.10
# my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# print(f"The first three items in the list are: {my_foods[:]}")
# print(f"Three items from the middle of the list are: {my_foods[2:]}")
# print(f"The last three items in the list are: {my_foods[-3:]}")

# 4.11
# my_pizzas = ['hawaian', 'pepparoni', 'margarita']
# friends_pizzas = my_pizzas[:]

# my_pizzas.append('oreos')
# friends_pizzas.append('vegetarian')

# print(my_pizzas)
# print(friends_pizzas)

# 4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are')
for food in my_foods :
    print(food)

print('\nMy friend\'s favorite foods are')
for friend_food in friend_foods :
    print(friend_food)
