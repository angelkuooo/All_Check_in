# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:17:17 2017

@author: user
"""

import sys

if __name__ == "__main__" :


	'''
		Section 1  :  Read File
	'''
	
	inputFile = sys.argv[1]

	dataReadIn = []

	with open (inputFile, 'r') as f :
		for line in f :
			dataReadIn.append ([row for row in line.strip().split('\t')])
	f.close ()
	
	
	POI=[]
	#Office
	
	
	for cnt in range(len(dataReadIn)):
		if("Office" in str(dataReadIn[cnt][3])):
			POI.append((dataReadIn[cnt]))
 	

	outputFile1 = "NYOffice.txt"
	fw1 = open (outputFile1, 'w')
	
	for cnt in range (len(POI)) :
		fw1.write ("%s\t" % POI[cnt][0])
		fw1.write ("%s\t" % POI[cnt][1])
		fw1.write ("%s\t" % POI[cnt][2])
		fw1.write ("%s\n" % POI[cnt][3])
	fw1.close ()