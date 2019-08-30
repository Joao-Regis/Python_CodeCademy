import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])
print('rainfall:\n' + str(rainfall) + '\n')
rainfall_sorted = np.sort(rainfall)
print('rainfall sorted:\n' + str(rainfall_sorted) + '\n')

rain_mean = np.mean(rainfall)
print('rainfall mean:\n' + str(rain_mean) + '\n')

rain_median = np.median(rainfall)
print('rainfall median:\n' + str(rain_median) + '\n')

first_quarter = np.percentile(rainfall, 25)
print('rainfall 25th percentile:\n' + str(first_quarter) + '\n')
third_quarter = np.percentile(rainfall, 75)
print('rainfall 75th percentile:\n' + str(third_quarter) + '\n')

interquartile_range = third_quarter - first_quarter
print('interquartile range:\n'+ str(interquartile_range) + '\n')

rain_std = np.std(rainfall)
print('rainfall standard deviation:\n'+ str(rain_std) + '\n')
