print("Statistica Statistici SARS-CoV-2")
cazuri_noi_n=[]
teste_efectuate_n=[]
with open("covid.in","r") as f:
    cazuri_noi_s=f.readline()
    cazuri_noi_s=cazuri_noi_s.replace("\n"," ")
    cazuri_noi_n=list(cazuri_noi_s)
    teste_efectuate_s = f.readline()
    teste_efectuate_s=teste_efectuate_s.replace("\n", " ")
    teste_efectuate_n = list(teste_efectuate_s)


numar=""
cazuri_noi=[] #prelucrare lista cazuri noi
for i in cazuri_noi_n:
    numar=numar+i
    if i==" ":
        cazuri_noi.append(numar)
        numar=""
print(cazuri_noi)

numar=""
teste_efectuate=[] #prelucrare lista teste efectuate
for i in teste_efectuate_n:
    numar=numar+i
    if i==" ":
        teste_efectuate.append(numar)
        numar=""
print(teste_efectuate)

for k in range(len(teste_efectuate)):
    print('Au fost ',int(cazuri_noi[k]), " de cazuri noi, fiind efectuate ",int(teste_efectuate[k])," teste")

#introducere date noi
