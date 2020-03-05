from django.shortcuts import render
import csv
# Create your views here.


def HomePage(request):
    data = open('MER_T12_06.csv','r')
    csv_reader = list(csv.reader(data, delimiter=','))
    FinalData = [[],[],[],[],[],[],[],[],[]]
    for row in csv_reader[1:]:
        temp = list()
        # temp.append(row[1][0:4]+" "+row[1][4:])
        temp.append(row[1])
        temp.append(row[2])
        FinalData[int(row[3])-1].append(temp)
    # return Json
    print(FinalData[0])
    context = {
        'coal':FinalData[0],
        'FinalData':FinalData[8],
        'FinalData':FinalData[0],
        'FinalData':FinalData[0],
        'FinalData':FinalData[0],
        'FinalData':FinalData[0],
        'FinalData':FinalData[0],
        'FinalData':FinalData[0],
        'FinalData':FinalData[0],
    }
    # CoalElectricPowerEmission = ;
    return render(request,"Syrus/Base.html",context)
