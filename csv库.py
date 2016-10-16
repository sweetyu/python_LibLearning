#!usr/bin/python
# coding=utf-8
import csv

def read(fileName):	
	with open(fileName,'rb') as csvfile:
		r = csv.reader(csvfile)
		for row in r:
			print row

def write(fileName):
	with open(fileName, 'wb') as csvfile:
		w = csv.writer(csvfile,dialect='excel')
		w.writerows([['a', '1', '1', '2', '2'],['b', '3', '3', '6', '4']])
		w.writerow(['c', '7', '7', '10', '4'])
		w.writerow(['d', '11','11','11', '1'])
		w.writerow(['e', '12','12','14', '3'])

if __name__ == '__main__':
	fileName=r'E:\Python\LibLearning\testCSV.csv'
	write(fileName)
	read(fileName)