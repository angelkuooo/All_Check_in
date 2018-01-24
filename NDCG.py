# -*- coding: utf-8 -*-
import sys
import numpy as np
from random import *
from math import sin, asin, cos, radians, fabs, sqrt  
import math 

# return dataReadIn
# ex:readfile('outbar.txt')
def readfile(filename):

	dataReadIn = []

	with open (filename, 'r') as f :
		for line in f :
			dataReadIn.append ([row for row in line.strip().split('\t')])
	f.close ()
	return dataReadIn
	
	

# int_10_list:[74,144,25,78,10,6,87,142,69,4]
# return list:['E','A','G','D','H','I','C','B','F','J']
def sort_list(int_10_list):

	a=sorted(int_10_list,reverse=True)
	#print(a)
	lst=['A','B','C','D','E','F','G','H','I','J']
	dick={}

	for cnt in range(len(lst)):
		dick[lst[cnt]]=a[cnt]
	#print(dick)

	check=[]
	for cnt in range(10):
		check.append(0)

	last_list=[]
	for cnt1 in range(len(lst)):
		for cnt2 in range(len(lst)):
			if(check[cnt2]==0):
				if(int_10_list[cnt1]==dick[lst[cnt2]]):
					last_list.append(lst[cnt2])
					check[cnt2]=1
	return(last_list)
	
	
# return list z
def random5_produce():
	
	lst=[]
	lst=['A','B','C','D','E']
	
	
	from random import shuffle
	x= [i for i in range(5)]
	shuffle(x)
	
	z=[]
	for cnt in range (5):
		z.append(lst[x[cnt]])
	 
	# type(z):list
	return z 


# return list y
def random10_produce():

	lst=['A','B','C','D','E','F','G','H','I','J']
	
	
	#from random import shuffle
	x= [i for i in range(10)]
	shuffle(x)
	

	y=[]
	for cnt in range (10):
		y.append(lst[x[cnt]])
	 
	# type(y):list
	return y 

# s:list   ex:s['A','C','B'......]
# k:NDCG@k	k can be 5 or 10 or other
def get_ndcg_at_k(s,k):
	'''This is a function to get ndcg '''
	
	reflect=['A','B','C','D','E','F','G','H','I','J']
	reflect_dic={}
	reflect_dic={"A":9,"B":8,"C":7,"D":6,"E":5,"F":4,"G":3,"H":2,"I":1,"J":0}
	fir_list=[]
	listsort=[]

	# fir_list: store as original order
	for cnt in range(k):
		fir_list.append(reflect_dic[s[cnt]])
	
	# listsort: big->small
	listsort=sorted(fir_list,reverse=True)
	# max : ideal NDCG
	max=0
	for i in range(k):
		max += reflect_dic[reflect[i]]/math.log(i+2,2)
	#print(max)
	
	dcg=0
	for i in range(k):
		dcg += (fir_list[i]/math.log(i+2,2))
	#print(dcg)
	ndcg=dcg/max
	#print(ndcg)
	return ndcg


''' 
def main () :
	random_file()
'''


	

# function random take out 10 data from the file
# output 2 file: bigremain.txt	&  litremain.txt
def random_file():

	# hotel.txt(movie.txt or park.txt)
	inputFile = sys.argv[1]
	dataReadIn = []

	with open (inputFile, 'r') as f :
		for line in f :
			dataReadIn.append ([row for row in line.strip().split('\t')])
		linenum=len(dataReadIn)
	f.close ()
		
		
	items=[]
	choose=[]
	for cnt in range(linenum):
		items.append(cnt)
	
	
	# sort hotel data with check-ins, from big to small
	data = []
	for cnt in range(len(dataReadIn)) :
		data.append (dataReadIn[cnt])

	data.sort(key=lambda x : int(x[3]), reverse=True)


	# store hotel data into 10 part
	datapart = []
	for cnt in range(10) :
		datapart.append([])
	
	
	'''
	# used in movie(136 kinds)
	for cnt in range(len(data)) :
	
		if int(data[cnt][3]) > 100 :
			datapart[0].append (data[cnt])
		elif int(data[cnt][3]) < 90 and int(data[cnt][3]) > 80 :
			datapart[1].append (data[cnt])
		elif int(data[cnt][3]) < 75 and int(data[cnt][3]) > 45 :
			datapart[2].append (data[cnt])
		elif int(data[cnt][3]) < 40 and int(data[cnt][3]) > 30 :
			datapart[3].append (data[cnt])
		elif int(data[cnt][3]) < 25 and int(data[cnt][3]) > 16 :
			datapart[4].append (data[cnt])
		elif int(data[cnt][3]) < 14 and int(data[cnt][3]) > 9 :
			datapart[5].append (data[cnt])
		elif int(data[cnt][3]) < 8 and int(data[cnt][3]) > 5 :
			datapart[6].append (data[cnt])
		elif int(data[cnt][3]) < 5 and int(data[cnt][3]) > 2 :
			datapart[7].append (data[cnt])
		elif int(data[cnt][3])== 2 :
			datapart[8].append (data[cnt])
		elif int(data[cnt][3])== 1 :
			datapart[9].append (data[cnt])
	'''		
	
	'''
	# used in hotel(648 kinds)
	for cnt in range(len(data)) :
	
		if int(data[cnt][3]) > 170 :
			datapart[0].append (data[cnt])
		elif int(data[cnt][3]) < 160 and int(data[cnt][3]) > 120 :
			datapart[1].append (data[cnt])
		elif int(data[cnt][3]) < 110 and int(data[cnt][3]) > 80 :
			datapart[2].append (data[cnt])
		elif int(data[cnt][3]) < 70 and int(data[cnt][3]) > 50 :
			datapart[3].append (data[cnt])
		elif int(data[cnt][3]) < 45 and int(data[cnt][3]) > 30 :
			datapart[4].append (data[cnt])
		elif int(data[cnt][3]) < 25 and int(data[cnt][3]) > 20 :
			datapart[5].append (data[cnt])
		elif int(data[cnt][3]) < 17 and int(data[cnt][3]) > 13 :
			datapart[6].append (data[cnt])
		elif int(data[cnt][3]) < 11 and int(data[cnt][3]) > 7 :
			datapart[7].append (data[cnt])
		elif int(data[cnt][3]) < 6 and int(data[cnt][3]) > 4 :
			datapart[8].append (data[cnt])
		elif int(data[cnt][3]) < 3 and int(data[cnt][3]) > 1 :
			datapart[9].append (data[cnt])
	'''
	
	
	# used in park(734 kinds)
	for cnt in range(len(data)) :
	
		if int(data[cnt][3]) > 800 :
			datapart[0].append (data[cnt])
		elif int(data[cnt][3]) < 600 and int(data[cnt][3]) > 300 :
			datapart[1].append (data[cnt])
		elif int(data[cnt][3]) < 200 and int(data[cnt][3]) > 110 :
			datapart[2].append (data[cnt])
		elif int(data[cnt][3]) < 100 and int(data[cnt][3]) > 75 :
			datapart[3].append (data[cnt])
		elif int(data[cnt][3]) < 60 and int(data[cnt][3]) > 50 :
			datapart[4].append (data[cnt])
		elif int(data[cnt][3]) < 45 and int(data[cnt][3]) > 35 :
			datapart[5].append (data[cnt])
		elif int(data[cnt][3]) < 28 and int(data[cnt][3]) > 20 :
			datapart[6].append (data[cnt])
		elif int(data[cnt][3]) < 15 and int(data[cnt][3]) > 7 :
			datapart[7].append (data[cnt])
		elif int(data[cnt][3]) < 5 and int(data[cnt][3]) > 2 :
			datapart[8].append (data[cnt])
		elif int(data[cnt][3])== 1 :
			datapart[9].append (data[cnt])

	
	#choose = sample(items, 10)
	
	# random choose one data for each part
	# randloc : random generate location
	randloc = []
	for cnt in range(10) :
		rnum = randint(0, len(datapart[cnt])-1)
		randloc.append (datapart[cnt][rnum])
	
	
	'''
	bigremain=[]
		
	outputFile1 = "bigremain.txt"
		
	fw1 = open (outputFile1, 'w')
	
	for cnt in range (linenum) : 
		if(cnt not in choose):										   
			fw1.write ("%s\t" % dataReadIn[cnt][0])
			fw1.write ("%s\t" % dataReadIn[cnt][1])
			fw1.write ("%s\t" % dataReadIn[cnt][2])
			fw1.write ("%s\n" % dataReadIn[cnt][3])
	fw1.close ()
	'''	
	
	outputFile2 = "park_10.txt"
		
	fw2 = open (outputFile2, 'w')
	
	for cnt in range (10) :	  
		fw2.write ("%s\t" % randloc[cnt][0])
		fw2.write ("%s\t" % randloc[cnt][1])
		fw2.write ("%s\t" % randloc[cnt][2])
		fw2.write ("%s\n" % randloc[cnt][3])
	fw2.close ()



# posType : 1 => Theater    2 => Hotel    3 => Park
def get_random_pos (posType):

	# hotel.txt(movie.txt or park.txt)
	if posType == 1 :
		inputFile = "movie.txt"
	elif posType == 2 :
		inputFile = "hotel.txt"
	elif posType == 3 :
		inputFile = "park.txt"
	else :
		print ("Testing File Read Error\n")
		sys.exit()
		
	dataReadIn = []

	with open (inputFile, 'r') as f :
		for line in f :
			dataReadIn.append ([row for row in line.strip().split('\t')])
		linenum=len(dataReadIn)
	f.close ()
		
		
	items=[]
	choose=[]
	for cnt in range(linenum):
		items.append(cnt)
	
	
	# sort hotel data with check-ins, from big to small
	data = []
	for cnt in range(len(dataReadIn)) :
		data.append (dataReadIn[cnt])

	data.sort(key=lambda x : int(x[3]), reverse=True)


	# store hotel data into 10 part
	datapart = []
	for cnt in range(10) :
		datapart.append([])
	
	if posType == 1 :
		# used in movie(136 kinds)
		for cnt in range(len(data)) :
	
			if int(data[cnt][3]) > 100 :
				datapart[0].append (data[cnt])
			elif int(data[cnt][3]) < 90 and int(data[cnt][3]) > 80 :
				datapart[1].append (data[cnt])
			elif int(data[cnt][3]) < 75 and int(data[cnt][3]) > 45 :
				datapart[2].append (data[cnt])
			elif int(data[cnt][3]) < 40 and int(data[cnt][3]) > 30 :
				datapart[3].append (data[cnt])
			elif int(data[cnt][3]) < 25 and int(data[cnt][3]) > 16 :
				datapart[4].append (data[cnt])
			elif int(data[cnt][3]) < 14 and int(data[cnt][3]) > 9 :
				datapart[5].append (data[cnt])
			elif int(data[cnt][3]) < 8 and int(data[cnt][3]) > 5 :
				datapart[6].append (data[cnt])
			elif int(data[cnt][3]) < 5 and int(data[cnt][3]) > 2 :
				datapart[7].append (data[cnt])
			elif int(data[cnt][3])== 2 :
				datapart[8].append (data[cnt])
			elif int(data[cnt][3])== 1 :
				datapart[9].append (data[cnt])

	elif posType == 2 :
		# used in hotel(648 kinds)
		for cnt in range(len(data)) :
	
			if int(data[cnt][3]) > 170 :
				datapart[0].append (data[cnt])
			elif int(data[cnt][3]) < 160 and int(data[cnt][3]) > 120 :
				datapart[1].append (data[cnt])
			elif int(data[cnt][3]) < 110 and int(data[cnt][3]) > 80 :
				datapart[2].append (data[cnt])
			elif int(data[cnt][3]) < 70 and int(data[cnt][3]) > 50 :
				datapart[3].append (data[cnt])
			elif int(data[cnt][3]) < 45 and int(data[cnt][3]) > 30 :
				datapart[4].append (data[cnt])
			elif int(data[cnt][3]) < 25 and int(data[cnt][3]) > 20 :
				datapart[5].append (data[cnt])
			elif int(data[cnt][3]) < 17 and int(data[cnt][3]) > 13 :
				datapart[6].append (data[cnt])
			elif int(data[cnt][3]) < 11 and int(data[cnt][3]) > 7 :
				datapart[7].append (data[cnt])
			elif int(data[cnt][3]) < 6 and int(data[cnt][3]) > 4 :
				datapart[8].append (data[cnt])
			elif int(data[cnt][3]) < 3 and int(data[cnt][3]) > 1 :
				datapart[9].append (data[cnt])

	
	elif posType == 3 :
		# used in park(734 kinds)
		for cnt in range(len(data)) :
	
			if int(data[cnt][3]) > 800 :
				datapart[0].append (data[cnt])
			elif int(data[cnt][3]) < 600 and int(data[cnt][3]) > 300 :
				datapart[1].append (data[cnt])
			elif int(data[cnt][3]) < 200 and int(data[cnt][3]) > 110 :
				datapart[2].append (data[cnt])
			elif int(data[cnt][3]) < 100 and int(data[cnt][3]) > 75 :
				datapart[3].append (data[cnt])
			elif int(data[cnt][3]) < 60 and int(data[cnt][3]) > 50 :
				datapart[4].append (data[cnt])
			elif int(data[cnt][3]) < 45 and int(data[cnt][3]) > 35 :
				datapart[5].append (data[cnt])
			elif int(data[cnt][3]) < 28 and int(data[cnt][3]) > 20 :
				datapart[6].append (data[cnt])
			elif int(data[cnt][3]) < 15 and int(data[cnt][3]) > 7 :
				datapart[7].append (data[cnt])
			elif int(data[cnt][3]) < 5 and int(data[cnt][3]) > 2 :
				datapart[8].append (data[cnt])
			elif int(data[cnt][3])== 1 :
				datapart[9].append (data[cnt])

	else :
		print ("Error in generating Testing Data\n")
		sys.exit()
	
	#choose = sample(items, 10)
	
	# random choose one data for each part
	# randloc : random generate location
	randloc = []
	for cnt in range(10) :
		rnum = randint(0, len(datapart[cnt])-1)
		randloc.append (datapart[cnt][rnum])
	
	return randloc


		
def chunkIt(seq, num):
	avg = len(seq) / float(num)
	out = []
	last = 0.0

	while last < len(seq):
		out.append(seq[int(last):int(last + avg)])
		last += avg

	return out
	print(out)
		
		
def hav(theta):	 
	s = sin(theta / 2)	
	return s * s	

# 算球面兩點距離
#longitude :經度	latitude:緯度
def get_distance_hav(lat0, lng0, lat1, lng1):  
	
	EARTH_RADIUS=6371			# 地球平均半徑，6371km	 
	
	#用haversine公式?算球面???的距离。
	# 經緯度轉換成弧度
	lat0 = radians(lat0)  
	lat1 = radians(lat1)  
	lng0 = radians(lng0)  
	lng1 = radians(lng1)  
   
	dlng = fabs(lng0 - lng1)  
	dlat = fabs(lat0 - lat1)  
	h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)  
	distance = 2 * EARTH_RADIUS * asin(sqrt(h))	 
   
	return distance 
	
'''
if __name__ == "__main__" :
	b=[74,144,25,78,10,6,87,142,69,4]
	sort_list(b)
'''
