import matplotlib.pyplot as plt
import numpy as np






class treatfile:





	"""
	The treatfileplot class allows one to load data from txt files, filter the values that comes after a given string
	and plot the result
	"""





	def __init__(self,file_name,filter):



		"""
		filemName is the file name
		filter is a list of 2 string lists to use in the filter: strings before and after the desired value. The 
			second string can be neglected
		"""



		#loads the data
		f=open(file_name,'r')
		lines=f.readlines()
		f.close()

		#first data filter
		self.data=[[] for i in range(len(filter))]
		i=0
		for j in range(len(filter)):
			for line in lines:
				splitLine = line.split(filter[j][0])
				if len(splitLine) != 1:
					if len(filter[j]) == 1: #filterEnd==False:
						try:
							self.data[i].append(float(splitLine[1]))
						except ValueError:
							self.data[i].append(splitLine[1])
					else:
						try:
							self.data[i].append(float(splitLine[1].split(filter[j][1])[0]))
						except ValueError:
							self.data[i].append(splitLine[1].split(filter[j][1])[0])
			i=i+1

		#other important definitions
		self.file_name=file_name
		self.header=[name[0] for name in filter]

		#saves original self variables
		self.data_saved = self.data[:]
		self.header_saved = self.header[:]





	def filter(self,column,values):



		"""
		this method filters the data with the values (list) in column
		column is the column to be filtered for the values in the values list
		values is the list of values used for the filter
		"""



		newData=[[] for i in range(len(self.data))]
		for i in range(len(self.data[column])):
			if self.data[column][i] in values:
				for j in range(len(self.data)):
					newData[j].append(self.data[j][i])
		self.data = newData





	def reset(self):



		"""
		this method resets all the data from file_name
		"""



		self.data = self.data_saved
		self.header = self.header_saved





	def removeColumn(self,column):



		"""
		This method removes column from self.data
		"""



		self.header.pop(column)
		self.data.pop(column)





	def removeLine(self,line):



		"""
		This method removes line line from all columns
		"""


		for i in range(len(self.data)):
			self.data[i].pop(line)





	def calculate(self,column,operation):



		"""
		This method creates a new column with the data from column treated with operation
		"""


		#converts time format H:M:S to seconds
		if operation == 'H:M:S to sec':

			self.data.append([])
			for i in self.data[column]:
				H,M,S=i.split(':')
				H=float(H)
				M=float(M)
				S=float(S)
				self.data[-1].append(3600*H+60*M+S)

		self.header.append(self.header[column]+' ('+operation+')')
			

