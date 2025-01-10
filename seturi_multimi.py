# set1 = {1,2,3,4,5,6,7,8,9}
# #afișăm setul creat
# print("Mulțimea este: ",set1)
# #afișăm numărul de elemente
# print("Număr de elemente:",len(set1))
# #folosim unii operatori
# print(1 in set1)
# print(5 not in set1)
# #un alt set cu elemente de tipuri diferite
# set2 = {12.5,8.7,4,"text",("un","tuplu")}
# print("Altă mulțime:",set2
#
# set1 = {'A','B','C'}
# print('Setul inițial:',set1)
# set1.add('D') #doar un element
# set1.update('E','F','G') #mai multe deodată
# print('După adăugări:',set1)
# #ștergem elementul 'E'
# set1.discard('E')
# #ștergem elementul 'B'
# set1.remove('B')
# #afișăm lista modificată
# print('După ștergeri:',set1)

A = {1,2,3,4,5,6,7}
B = {5,6,7,8,9,10}
#reuniunea
print(A|B)
print(A.union(B))
#intersecția
print(A&B)
print(A.intersection(B))
#diferența dintre A și B
print(A-B)
print(A.difference(B))
#diferența dintre B și A
print(B-A)
print(B.difference(A))
#diferența simetrică
print(A^B)

# frozenset
fA = frozenset({1,2,3,4,5})
print(fA)
#obținem eroare dacă ștergem ceva
#fA.discard(1)
#obținem eroare dacă adăugăm ceva
#fA.append(6)

