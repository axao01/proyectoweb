from random import randrange
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import variables
import time
import csv

with open("C:/Users/lucas/OneDrive - Universidad Austral de Chile/2023/Segundo_Semestre/ELEL210(DiseñoSistemas)/Proyecto_ELEL210/mysite/DatosVA.csv") as csv_file:
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

maximoH = 0
minimoH = 100
for i in matriz2[1:]:
    if float(i[1]) > maximoH and i[1]!='':
        maximoH = float(i[1])
    if float(i[1]) < minimoH and i[1]!='':
        minimoH = float(i[1])





# Create your views here.
def home(request):
    return render(request, "base.html", context={"minimoT": minimo, "maximoT": maximo, "minimoH": minimoH,"maximoH":maximoH})



def get_chart(request):
    valor_inicio = None




    chart = option = {
  'legend': {},
  'tooltip': {
      'show':'true',
      'trigger': 'axis',
      'triggerOn': 'mousemove|click',
  },
  'dataZoom':[
            valor_inicio,
            {
                'type': 'inside'
            },
              {
                  'show': 'true'
              }
        ],

  'dataset': [{
    'id': 'data1',
    'source': matriz1,

  },
      {
          'id': 'data2',
          'source': matriz2,

      }
  ],

  'xAxis': { 'type': 'time'},

  'yAxis': [{'name': 'Temperatura [°C]',
            'nameLocation': 'middle',
            'nameGap':30,
            'nameTextStyle': {'fontSize': 20, 'color': 'rgb(0,0,0)'}},
            {
            'name': 'Humedad relativa porcentual [%]',
            'nameLocation': 'middle',
            'nameGap':30,
            'nameTextStyle': {'fontSize': 20, 'color': 'rgb(0,0,0)'}}
            ],

  'series': [{ 'type': 'line','datasetId': 'data1', 'color': 'rgb(231, 26, 26 )'  },
             { 'type': 'line','datasetId': 'data2','yAxisIndex': 1, 'color': 'rgb(5, 39, 190 )'}
             ],
  'toolbox': {'show': 'true', 'feature': {'saveAsImage': {}, 'dataZoom': {}} },

}
    return JsonResponse(chart)

