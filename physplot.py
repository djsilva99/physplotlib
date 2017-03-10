import matplotlib.pyplot as plt
import numpy as np










"""
The physplot class allows one to load data from txt files, make simple treatment and plot the data 
in a fast and efficient way.
"""



class physplot:

	def __init__(self,fileName,start=1,stop=-1,delim=','):

		f=open(fileName,'r')
		lines=f.readlines()
		if len(lines[0].split(delim))!=len(lines[1].split(delim))+1:
			print 'file corrupted'
			stop
		self.header=[]
		for i in range(len(lines[0].split(delim))):
			self.header.append(lines[0].split(delim)[i])
		self.numberColumns = len(lines[start].split(delim))
		for i in range(start):
			lines.pop(0)
		self.data = [[] for i in range(self.numberColumns)]			
		for line in lines:
			for i in range(self.numberColumns):
				self.data[i].append(float(line.split(delim)[i]))				
		f.close()
		self.headerCopy = self.header
		self.numberColumnsCopy = self.numberColumns
		self.dataCopy = self.data


	def reset(self):

		self.header=self.headerCopy
		self.numberColumns=self.numberColumnsCopy
		self.data=self.dataCopy


	def removePeriodicPoints(self,start,period):

		for i in range(start):
			for j in range(self.numberColumns):
				self.data[j].pop(0)
		n=0
		r=0
		for i in range(len(self.data[0])):
			if n == period:
				n=0
				r=r+1
			if n != period:
				for k in range(self.numberColumns):
					self.data[k].pop(r+n)
				n=n+1


	def singlePlot(self,xColumn,yColumn,type='lin'):

		plt.title(self.header[0])
		plt.xlabel(self.header[xColumn+1])
		plt.ylabel(self.header[yColumn+1])
		xColumn=self.data[xColumn]
		plt.plot(xColumn,self.data[yColumn],'o')
		if type!='lin':
			plt.xscale(type)
		plt.show()


	def average(self,column):

		uniqueValueList = [[] for i in range(len(self.data)+1)]

		for i in range(len(self.data[column])):
			if not (self.data[column][i] in uniqueValueList[column]):
				for j in range(self.numberColumns):
					uniqueValueList[j].append(self.data[j][i])
				uniqueValueList[-1].append(1.)
			else:
				index = uniqueValueList[column].index(self.data[column][i])
				for j in range(self.numberColumns):
					if j!=column:
						uniqueValueList[j][index]=self.data[j][i]+uniqueValueList[j][index]
				uniqueValueList[-1][index]=uniqueValueList[-1][index]+1.
		print uniqueValueList
		for i in range(len(uniqueValueList[0])):
			for j in range(self.numberColumns):
				if j!=column:
					uniqueValueList[j][i]=uniqueValueList[j][i]/uniqueValueList[-1][i]
		uniqueValueList.pop()
		self.data=uniqueValueList


	def save(self,fileName):

		f=open(fileName,'w')
		for head in self.header[:-1]:
			f.write(head+',')
		f.write(self.header[-1])
		for i in range(len(self.data[0])):
			for j in range(self.numberColumns-1):
				f.write(str(self.data[j][i])+',')
			f.write(str(self.data[-1][i])+'\n')
		f.close()


	def removeValues(self,xColumn,value):

		removeList=[]
		for i in range(len(self.data[0])):
			if self.data[xColumn][i]==value:
				removeList.append(i)
		for i in [k for k in reversed(removeList)]:
			for j in range(self.numberColumns):
				self.data[j].pop(i)


	def plotHist(self,column,min=0.00001,max=100000000,steps=20,type='lin'):

		if type=='lin':
			plt.hist(self.data[column],bins='auto')
		elif type=='log':
			bin = 10 ** np.linspace(np.log10(min), np.log10(max), steps)
			plt.hist(self.data[column],bins=bin)
			plt.xscale('log')
		else:
			'type input incorrect'
		plt.xlabel(self.header[column+1])
		plt.show()