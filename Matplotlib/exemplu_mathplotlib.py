import matplotlib.pyplot as plt
figura,axe=plt.subplots()
elevi=['a IX-a','a X-a','a XI-a','a XII-a']
medii=[9.43,8.23,7.45,9.87]
etichete=elevi
culori=['tab:red','tab:blue','tab:green','tab:orange']
axe.bar(elevi,medii,label=etichete,color=culori)
axe.set_ylabel("Note")
axe.set_title("Mediile elevilor")
axe.legend(title="Clase")
plt.show()
