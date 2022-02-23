import numpy as np

ar = np.arange(1,201)
x = int(input("Enter  the number you will like to see the multiples of: "))
print(ar[ar%x==0])
