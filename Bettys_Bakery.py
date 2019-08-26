import numpy as np
print("Betty's Bakery - Output")

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
print('Cupcakes:\n ' + str(cupcakes))
print('\n')

recipes = np.genfromtxt('recipes.csv', delimiter = ',')
print('Recipe:\n ' + str(recipes))
print('\n')

eggs = recipes[:, 2]
print('Eggs:\n ' + str(eggs))
print('\n')

one_egg_t_or_f = recipes[:, 2] == 1
one_egg = recipes[(eggs == 1)]
print('One egg recipes T or F:\n ' + str(one_egg_t_or_f))
print('One egg recipes:\n ' + str(one_egg))
print('\n')

cookies = recipes[2, :]
print('Cookies:\n' + str(cookies))
print('\n')

double_batch = cupcakes * 2
print(double_batch)
print('\n')

grocery_list = cookies + double_batch
print(grocery_list)
