import sys

import time

import processfunction as pf

if __name__ == "__main__" :

    ts=time.time()
    
    
    
    inputFile1 = sys.argv[1]

    #outcheck.txt
    dataReadIn1 = []


    with open (inputFile1, 'r') as f :
        for line in f :
            dataReadIn1.append ([row for row in line.strip().split('\t')])
    f.close ()
    
    
    #NYxxxx.txt
    inputFile2 = sys.argv[2]

   
    dataReadIn2 = []


    with open (inputFile2, 'r') as g :
        for line in g :
            dataReadIn2.append ([row for row in line.strip().split('\t')])
    g.close ()
    
    ts1=time.time()
    print("Load Time : %f" % (ts1-ts))
    
    longilati = pf.record_longi_lati(dataReadIn2) #return dic
    bigList1 = pf.structure_init(dataReadIn2) #return list
    listOrder=pf.structure_order(bigList1) #return dic
    
    ts2=time.time()
    print("Preprocessing time : %f" % (ts2-ts1))
    
    listkey=list(listOrder.keys()) #list
    
    for cnt1 in range (len(dataReadIn1)):
        if(str(dataReadIn1[cnt1][0]) in listkey):
            order=listOrder[dataReadIn1[cnt1][0]]
            bigList1[order][1][str(dataReadIn1[cnt1][1])]+= int(dataReadIn1[cnt1][2])
            
    ts3=time.time()
    print("Create each month checkins : %f" % (ts3-ts2))
        
    bigList2=pf.accumulate(bigList1)
    
    ts4=time.time()
    print("Accumulate checkins' time : %f" % (ts4-ts3))
    
    # File output
    outputFile = "outResidential_Building.txt"

    fw = open (outputFile, 'w')
    
    
    for cnt in range (len(bigList2)) :   
        fw.write ("%s\t" % bigList2[cnt][0])
        fw.write ("%s\t" % longilati[(dataReadIn2[cnt][0])][0])
        fw.write ("%s\t" % longilati[(dataReadIn2[cnt][0])][1])
        fw.write ("%s\n" % bigList2[cnt][1]['2013Sep'])

    fw.close ()