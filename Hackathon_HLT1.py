import csv

Sens_ID =[]
Dist_Travelled = []
Dist_Rem = []
with open('C:\Users\NTshikovhi\Desktop\ALU\Python\distance_sensors.csv') as TrainData:
    
    reader = csv.reader(TrainData)
    header =reader.next()
    column ={h:[] for h in header}
    for row in reader:
        for h,v in zip(header,row):
            column[h].append(v)

##    print(column)

    
Sens_ID = column['sensor_id']
NewSens_ID = Sens_ID[0:-2]
Sens = [int(i) for i in NewSens_ID]

Dist_Rem = column['distance_remaining']
NewDist_Rem = Dist_Rem[0:-1]
NewDist= [float(k) for k in NewDist_Rem]



Dist_Trav = column['distance_travelled']
NewDist_Trav = Dist_Trav[0:-2]
NewDistTrav = [float(j) for j in NewDist_Trav]

CumulativeSensDist = []
count = 0
while count<501:
    
    CumulativeSensDist.append(sum(NewDistTrav[0:count+1]))
    count =count+1

print(len(CumulativeSensDist))
for element in range(0,499):

    A = CumulativeSensDist[element]+NewDist[element]
    if A < 1011.7:
        print (str(Sens[element]) + ' is out of range')

    else:
        print(str(Sens[element]) + ' is well within range')

    





	    

	    
	    

		
