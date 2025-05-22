import numpy as np
import random
import matplotlib.pyplot as plt
#simulate rolling a die 1000 times
rolls_die1 = np.random.randint(1, 7, size=1000)
rolls_die2 = np.random.randint(1, 7, size= 1000)




sum_of_faces = rolls_die1 + rolls_die2

#count the ocurrences of each possible result, from 2 to 12

counts = np.bincount(sum_of_faces)[2:] #skip 0 and 1

#sum values

sum_values = np.arange(2,13) #2 to 12

# plotting the results of the sum

plt.bar(sum_values, counts, color= 'lightcoral', edgecolor='black')

#titles and labels

plt.title("Distribution of two dice sums")
plt.xlabel("Sum of dice")
plt.ylabel("counts")
plt.xticks(sum_values)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()




