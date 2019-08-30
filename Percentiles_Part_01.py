import numpy as np

patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])
print('Patrons array:\n ' + str(patrons))
patrons_sorted = np.sort(patrons)
print('Patrons array sorted:\n ' + str(patrons_sorted))

thirtieth_percentile = np.percentile(patrons, 30)
print('Thirtieth percentile: ' + str(thirtieth_percentile))

seventieth_percentile = np.percentile(patrons, 70)
print('Seventieth percentile: ' + str(seventieth_percentile))