import numpy as np
import sys
A = range(100)
print("Dim. fiecarui element din lista: ",sys.getsizeof(A))
print("Dim. listei: ",sys.getsizeof(A)*len(A))
A_numpy = np.arange(100)
print("Dim. fiecarui element din tablou: ",A_numpy.itemsize)
print("Dim. tabloului: ",A_numpy.size*A_numpy.itemsize)
print("Afisare A")
print(A)