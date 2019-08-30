#https://youtu.be/U3DrUcQzkIA
import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter =',')
print('Cereal csv (Calorie Stats):\n'+ str(calorie_stats) + '\n')
calorie_stats_sorted = np.sort(calorie_stats)
print('Calorie Stats sorted):\n'+ str(calorie_stats_sorted) + '\n')

calorie_stats_mean = np.mean(calorie_stats)
print('Calorie Stats average:\n'+ str(calorie_stats_mean) + '\n')

crunchie_munchies_avg_calorie_per_serving = 60

average_calories = calorie_stats_mean - crunchie_munchies_avg_calorie_per_serving
print('average calorie difference per serving:\n'+ str(average_calories) + '\n')

median_calories = np.median(calorie_stats)
print('Calorie Stats median:\n'+ str(median_calories) + '\n')

more_calories = 3.29

nth_percentile = np.percentile(calorie_stats, more_calories)
print('percentile greter than 60 avg calories per serving:\n' + str(100 - more_calories) + '\n')

calorie_std = np.std(calorie_stats)
print('Calorie Stats standard deviation\n'+ str(calorie_std) + '\n')

cm_summary = 'crunchie munchies has a lower average calorie count per serving than 96% of other cereals'
print(cm_summary)
