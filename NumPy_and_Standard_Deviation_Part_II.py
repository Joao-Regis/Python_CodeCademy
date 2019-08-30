import numpy as np

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_sorted = np.sort(pumpkin)
print('pumpkin sorted:\n '+ str(pumpkin_sorted))
acorn_squash_sorted = np.sort(acorn_squash)
print('acorn squash sorted:\n' + str(acorn_squash_sorted))

pumpkin_avg = np.mean(pumpkin)
print('pumpking avg: '+ str(pumpkin_avg))

acorn_squash_avg = np.mean(acorn_squash)
print('acorn squash avg: ' + str(acorn_squash_avg))

pumpkin_std = np.std(pumpkin)
print('pumpkin standard deveiation: ' + str(pumpkin_std))
acorn_squash_std = np.std(acorn_squash)
print('acorn squash standard deveiation: ' + str(acorn_squash_std))

winner = pumpkin
