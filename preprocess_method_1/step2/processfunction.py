import sys

'''

'''
def argCheck():

    if len(sys.argv) != 2 :
        print ("\n\tUsage  :  python  process.py  [input file name]")
        sys.exit()




'''
    return : list
'''
def readFile (fileName) :

    data = []

    with open(fileName, "r") as f:
        for line in f:
            data.append([row for row in line.strip().split('\t')])

    return data



'''
    input : raw data list (NYxxxx.txt)

    return : dict ['location ID'] = (longitude, latitude)
'''
def record_longi_lati (data):

    dic = {}

    for cnt in range(len(data)) :

        dic[data[cnt][0]] = (data[cnt][1], data[cnt][2])

    return dic



'''
    input : raw data list (NYxxxx.txt)

    return : list : [ [id1, datetime_dict1],
                      [id2, datetime_dict2],
                      .
                      .
                      .
                      [idN, datetime_dictN]
                    ]
'''
def structure_init(data):

    lis = []
    dickey = ["2012Apr", "2012May", "2012Jun", "2012Jul", "2012Aug", "2012Sep", "2012Oct", "2012Nov", "2012Dec", "2013Jan","2013Feb","2013Mar","2013Apr","2013May","2013Jun","2013Jul","2013Aug", "2013Sep"]

    dicName = []
    for cnt in range(len(data)):
        dicName.append(cnt)


    for cnt in range(len(data)) :

        # create each id's dict
        dicName[cnt] = {}
        for cntIn in range(len(dickey)):
            dicName[cnt][dickey[cntIn]] = 0
        

        lis.append([data[cnt][0], dicName[cnt]])
    

    return lis


def accumulate(lis):

      
    for cnt in range (len(lis)):
        lis[cnt][1]["2012May"]+=lis[cnt][1]["2012Apr"]
        lis[cnt][1]["2012Jun"]+=lis[cnt][1]["2012May"]
        lis[cnt][1]["2012Jul"]+=lis[cnt][1]["2012Jun"]
        lis[cnt][1]["2012Aug"]+=lis[cnt][1]["2012Jul"]
        lis[cnt][1]["2012Sep"]+=lis[cnt][1]["2012Aug"]
        lis[cnt][1]["2012Oct"]+=lis[cnt][1]["2012Sep"]
        lis[cnt][1]["2012Nov"]+=lis[cnt][1]["2012Oct"]
        lis[cnt][1]["2012Dec"]+=lis[cnt][1]["2012Nov"]
        lis[cnt][1]["2013Jan"]+=lis[cnt][1]["2012Dec"]
        lis[cnt][1]["2013Feb"]+=lis[cnt][1]["2013Jan"]
        lis[cnt][1]["2013Mar"]+=lis[cnt][1]["2013Feb"]
        lis[cnt][1]["2013Apr"]+=lis[cnt][1]["2013Mar"]
        lis[cnt][1]["2013May"]+=lis[cnt][1]["2013Apr"]
        lis[cnt][1]["2013Jun"]+=lis[cnt][1]["2013May"]
        lis[cnt][1]["2013Jul"]+=lis[cnt][1]["2013Jun"]
        lis[cnt][1]["2013Aug"]+=lis[cnt][1]["2013Jul"]
        lis[cnt][1]["2013Sep"]+=lis[cnt][1]["2013Aug"]
    
    return lis
            


'''
    input : list (return from structure_init())

    return : dict {"id1" : position in input list,
                   "id2" :        ......            
                                .
                                .
                                .
                   "idN" :        ......
                  }
'''
def structure_order(lis):
    
    dic = {}

    for cnt in range(len(lis)):

        dic[lis[cnt][0]] = cnt


    return dic