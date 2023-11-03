import csv

with open("C:/Users/lucas/Downloads/Pichoy.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    c = 0
    matriz1 = []
    matriz2 = []
    for row in csv_reader:

        if c==0:
            matriz1.append(['', row[1]])
            matriz2.append(['', row[2]])
        elif row[1] == '' or row[2] == '':
            pass
        else:
            a = list(row[0])
            b = a[6]+a[7]+a[8]+a[9]+a[2]+a[3]+a[4]+a[5]+a[0]+a[1]+'T'+a[11]+a[12]+a[13]+a[14]+a[15]+':00Z'
            row[0] = b
            row1 = [row[0], row[1]]
            row2 = [row[0], row[2]]
            matriz1.append(row1)
            matriz2.append(row2)
        c += 1

maximo = -1000
minimo = 1000
for i in matriz1[1:]:
    if float(i[1]) > maximo:
        maximo = float(i[1])
    if float(i[1]) < minimo:
        minimo = float(i[1])
print(minimo)
print(maximo)

maximoH = 0
minimoH = 100
for i in matriz2[1:]:
    if float(i[1]) > maximoH and i[1]!='':
        maximoH = float(i[1])
    if float(i[1]) < minimoH and i[1]!='':
        minimoH = float(i[1])
print(minimoH)
print(maximoH)
#Transforma fecha b = a[6]+a[7]+a[8]+a[9]+a[2]+a[3]+a[4]+a[5]+a[0]+a[1]+'T'+a[11]+a[12]+a[13]+a[14]+a[15]+':00Z'