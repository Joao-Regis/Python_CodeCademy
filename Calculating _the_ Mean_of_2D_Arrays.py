import numpy as np

allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)
print(total_mean)

trial_mean= np.mean(allergy_trials, axis = 1)
print(trial_mean)

patient_mean = np.mean(allergy_trials, axis = 0)
print(patient_mean)
