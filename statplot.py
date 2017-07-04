import matplotlib.pyplot as plt
import numpy as np







class statplot:





	"""
	The statplot class allows one to load data from txt files, make simple treatment and plot the data 
	in a fast and efficient way, without refreshing constantly while the sourse file is being changed
	"""





	def __init__(self,fileName,header=True,start=0,stop=-1,delim=','):



		"""
		filemName is the file name
		header is a bolean that tells if the file has a header
		start indicates the firs line in the file to be loaded
		stop indicates the last line in the file to be loaded
		delim is a string that indicates the separation of the column
		"""



		#loads the data
		f=open(fileName,'r')
		lines=f.readlines()
		self.header=[]
		self.numberColumns = len(lines[start].split(delim))

		if header==True:
			for i in range(len(lines[0].split(delim))):
				self.header.append(lines[0].split(delim)[i])
				start=1
			
		for i in range(start):
			lines.pop(0)

		self.data = [[] for i in range(self.numberColumns)]			
		for line in lines:
			for i in range(self.numberColumns):
				self.data[i].append(float(line.split(delim)[i]))				

		f.close()

		#loads the initial data if method reset is used afterwards
		self.fileName = fileName
		self.headerCopy = self.header
		self.numberColumnsCopy = self.numberColumns
		self.dataCopy = self.data





	def reset(self):



		"""
		this method resets all the data from fileName
		"""



		self.header=self.headerCopy
		self.numberColumns=self.numberColumnsCopy
		self.data=self.dataCopy





	def verticalPlot(self,xColumn,yColumnList,type='lin',symbol='o-'):



		"""
		this method plots each entry of the input list yColumnList as a function of the input list xColumn
		type is the scale mode of the plot
		symbol is the symbol of the plot
		"""



		plt.title(self.fileName)
		if len(yColumnList)==1:
			plt.xlabel(self.header[xColumn])
			plt.ylabel(self.header[yColumnList[0]])
			plt.plot(self.data[xColumn],self.data[yColumnList[0]],symbol)
			if type!='lin':
				plt.xscale(type)

		else:	
			for i in yColumnList:
				plt.plot(self.data[xColumn],self.data[i],symbol,label=self.header[i])
			plt.xlabel(self.header[xColumn])
			plt.legend(loc='upper left', shadow=True)
			if type!='lin':
				plt.xscale(type)
		plt.show()





	def horizontalPlot(self,xLine,columns,xLineValue=True,xColumn=0,type='lin',symbol='o-',
		limits='default',xlabel='file column index',ylabel='value',xShift=0,xLength='default'):



		"""
		This method plots the values of a line of the file as a function of column index
		xLine is the line to be ploted. If xLineValue is True, xLine is the value of the xColumn.
		columns is a entry lists that indicates the range of indexes to be ploted
		type is the scale mode of the plot
		symbol is the symbol of the plot
		limits are the limits of the y scale
		xlabel is the name of the x axis
		ylabel is the name of the y axis
		xShift is the correction of the index
		xLength is the space step. If default the x axis will only show the indexes. If a float number, the x
			axis will show the length accordingly
		"""



		if xLineValue==True:
			xLine = [self.data[xColumn].index(xline) for xline in xLine]

		if len(xLine)==1:
			title=self.fileName+'\n'+self.header[xColumn].split('(')[0]+' ('+str(self.data[xColumn][xLine[0]])+' '+self.header[xColumn].split('(')[1].split(')')[0]+')'
		else:
			title=self.fileName

		plt.title(title)

		for j in range(len(xLine)):
			x=[]
			li=[]
			for i in range(columns[0],columns[1]):
				x.append(i-xShift)
				li.append(self.data[i][xLine[j]])
			label=self.header[xColumn].split('(')[0]+' = '+str(xLine[j])+' '+self.header[xColumn].split('(')[1].split(')')[0]
			if xLength != 'default':
				x=[i*xLength for i in x]			
			if len(xLine) != 1:
				plt.plot(x,li,symbol,label=label)	
			else:
				plt.plot(x,li,symbol,label=label)	

		if len(xLine) != 1:
			plt.legend(loc='upper left', shadow=True)
		if limits != 'default':
			plt.ylim(limits)

		plt.xlim([min(x),max(x)])
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.show()