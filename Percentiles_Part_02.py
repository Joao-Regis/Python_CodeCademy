import numpy as np

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

first_quarter = np.percentile(movies_watched, 25)
print(first_quarter)
third_quarter = np.percentile(movies_watched, 75)
print(third_quarter)

interquartile_range = third_quarter - first_quarter
print(interquartile_range)