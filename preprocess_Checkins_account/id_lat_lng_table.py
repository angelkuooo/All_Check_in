# -*- coding: utf-8 -*-

import sys
import NDCG
import time


#This program is used for all around checkins to decide.
# python id_lat_lng_table.py (no need any parameter)
#########################################################

'''
outputfile="Checkins_account.txt"

		ID		lat			lng			Checkins_num(accumulated from dataset_TIST2015_Checkins_part1-20)
	3fd662...	40.733596	-74.003139		86
	...			...			...				...
	
'''

if __name__ == "__main__" :

	t1=time.time()

	dataReadIn1=[]

	inputFile1="dataset_TIST2015_POIs.txt"
	with open (inputFile1,'r') as f :
		for line in f :
			dataReadIn1.append ([row for row in line.strip().split('\t')])
	f.close ()

	t2=time.time()
	print("Time for reading POI data : " + str(t2-t1) + "sec")


	id_lat_lng_table=[]
	for cnt in range(len(dataReadIn1)):
		id_lat_lng_table.append([])

	for cnt1 in range(len(id_lat_lng_table)):
		for cnt2 in range(3):
			id_lat_lng_table[cnt1].append(dataReadIn1[cnt1][cnt2])
		id_lat_lng_table[cnt1].append(0)
		
	for cnt in range(len(id_lat_lng_table)):
		id_lat_lng_table[cnt][1]=float(id_lat_lng_table[cnt][1])
		id_lat_lng_table[cnt][2]=float(id_lat_lng_table[cnt][2])
	t3=time.time()
	print("Time for constructing table : " + str(t3-t2) + "sec")

	Checkin_id=[]
	
	Checkins_data_1=NDCG.readfile("dataset_TIST2015_Checkins_part1.txt")
	for cnt in range(len(Checkins_data_1)):
		Checkin_id.append(Checkins_data_1[cnt][1])
	Checkins_data_1.clear()
	
	
	Checkins_data_2=NDCG.readfile("dataset_TIST2015_Checkins_part2.txt")
	for cnt in range(len(Checkins_data_2)):
		Checkin_id.append(Checkins_data_2[cnt][1])
	Checkins_data_2.clear()
	
	
	Checkins_data_3=NDCG.readfile("dataset_TIST2015_Checkins_part3.txt")
	for cnt in range(len(Checkins_data_3)):
		Checkin_id.append(Checkins_data_3[cnt][1])
	Checkins_data_3.clear()
	
	
	Checkins_data_4=NDCG.readfile("dataset_TIST2015_Checkins_part4.txt")
	for cnt in range(len(Checkins_data_4)):
		Checkin_id.append(Checkins_data_4[cnt][1])
	Checkins_data_4.clear()
	
	
	Checkins_data_5=NDCG.readfile("dataset_TIST2015_Checkins_part5.txt")
	for cnt in range(len(Checkins_data_5)):
		Checkin_id.append(Checkins_data_5[cnt][1])
	Checkins_data_5.clear()
	
	
	Checkins_data_6=NDCG.readfile("dataset_TIST2015_Checkins_part6.txt")
	for cnt in range(len(Checkins_data_6)):
		Checkin_id.append(Checkins_data_6[cnt][1])
	Checkins_data_6.clear()
	
	
	Checkins_data_7=NDCG.readfile("dataset_TIST2015_Checkins_part7.txt")
	for cnt in range(len(Checkins_data_7)):
		Checkin_id.append(Checkins_data_7[cnt][1])
	Checkins_data_7.clear()
	
	
	Checkins_data_8=NDCG.readfile("dataset_TIST2015_Checkins_part8.txt")
	for cnt in range(len(Checkins_data_8)):
		Checkin_id.append(Checkins_data_8[cnt][1])
	Checkins_data_8.clear()
	
	
	Checkins_data_9=NDCG.readfile("dataset_TIST2015_Checkins_part9.txt")
	for cnt in range(len(Checkins_data_9)):
		Checkin_id.append(Checkins_data_9[cnt][1])
	Checkins_data_9.clear()
	
	
	Checkins_data_10=NDCG.readfile("dataset_TIST2015_Checkins_part10.txt")
	for cnt in range(len(Checkins_data_10)):
		Checkin_id.append(Checkins_data_10[cnt][1])
	Checkins_data_10.clear()
	
	
	Checkins_data_11=NDCG.readfile("dataset_TIST2015_Checkins_part11.txt")
	for cnt in range(len(Checkins_data_11)):
		Checkin_id.append(Checkins_data_11[cnt][1])
	Checkins_data_11.clear()
	
	
	Checkins_data_12=NDCG.readfile("dataset_TIST2015_Checkins_part12.txt")
	for cnt in range(len(Checkins_data_12)):
		Checkin_id.append(Checkins_data_12[cnt][1])
	Checkins_data_12.clear()
	
	
	Checkins_data_13=NDCG.readfile("dataset_TIST2015_Checkins_part13.txt")
	for cnt in range(len(Checkins_data_13)):
		Checkin_id.append(Checkins_data_13[cnt][1])
	Checkins_data_13.clear()
	
	
	Checkins_data_14=NDCG.readfile("dataset_TIST2015_Checkins_part14.txt")
	for cnt in range(len(Checkins_data_14)):
		Checkin_id.append(Checkins_data_14[cnt][1])
	Checkins_data_14.clear()
	
	
	Checkins_data_15=NDCG.readfile("dataset_TIST2015_Checkins_part15.txt")
	for cnt in range(len(Checkins_data_15)):
		Checkin_id.append(Checkins_data_15[cnt][1])
	Checkins_data_15.clear()
	
	
	Checkins_data_16=NDCG.readfile("dataset_TIST2015_Checkins_part16.txt")
	for cnt in range(len(Checkins_data_16)):
		Checkin_id.append(Checkins_data_16[cnt][1])
	Checkins_data_16.clear()
	
	
	Checkins_data_17=NDCG.readfile("dataset_TIST2015_Checkins_part17.txt")
	for cnt in range(len(Checkins_data_17)):
		Checkin_id.append(Checkins_data_17[cnt][1])
	Checkins_data_17.clear()
	
	
	Checkins_data_18=NDCG.readfile("dataset_TIST2015_Checkins_part18.txt")
	for cnt in range(len(Checkins_data_18)):
		Checkin_id.append(Checkins_data_18[cnt][1])
	Checkins_data_18.clear()
	
	
	Checkins_data_19=NDCG.readfile("dataset_TIST2015_Checkins_part19.txt")
	for cnt in range(len(Checkins_data_19)):
		Checkin_id.append(Checkins_data_19[cnt][1])
	Checkins_data_19.clear()
	
	
	Checkins_data_20=NDCG.readfile("dataset_TIST2015_Checkins_part20.txt")
	for cnt in range(len(Checkins_data_20)):
		Checkin_id.append(Checkins_data_20[cnt][1])
	Checkins_data_20.clear()
	
	t4=time.time()
	print("Time for read checkins data : " + str(t4-t3) + "sec")
	
	id_series=[]
	for cnt in range(len(id_lat_lng_table)):
		id_series.append(id_lat_lng_table[cnt][0])
	
	counters={}
	
	for item in Checkin_id:
		if item in counters:
			counters[item]+=1
		else:
			counters[item]=1
	# print(len(counters)==len(id_lat_lng_table)):True
	
	
	for cnt in range(len(id_lat_lng_table)):
		id_lat_lng_table[cnt][3]+= int(counters[id_lat_lng_table[cnt][0]])
	
	outputFile2 = "Checkins_account.txt"
		
	fw = open (outputFile2, 'w')
	
	for cnt in range (len(id_lat_lng_table)) : 
		fw.write ("%s\t" % id_lat_lng_table[cnt][0])
		fw.write ("%s\t" % id_lat_lng_table[cnt][1])
		fw.write ("%s\t" % id_lat_lng_table[cnt][2])
		fw.write ("%s\n" % id_lat_lng_table[cnt][3])
	fw.close ()