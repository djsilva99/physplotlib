import matplotlib.pyplot as plt
import numpy as np







class statplot:





	"""
	The statplot class allows one to load data from txt files, make simple treatment and plot the data 
	in a fast and efficient way, without refreshing constantly while the sourse file is being changed
	"""





	def __init__(self):

		self.header=[]
		self.data=[]
		self.file_name=[]
		self.header_saved = None
		self.data_saved = None






	def loadFile(self,file_name,header=True,delim=','):



		"""
		This method load the data of file_name
		filemName is the file name
		header is a bolean that tells if the file has a header
		delim is a string that indicates the separation of the column
		"""



		self.data.append([])
		f=open(file_name,'r')
		lines=f.readlines()
		self.header.append([])
		number_columns = len(lines[0].split(delim))
		self.file_name.append(file_name)
		if header==True:
			for i in range(len(lines[0].split(delim))):
				self.header[-1].append(lines[0].split(delim)[i])
		lines.pop(0)
		self.data[-1] = [[] for i in range(number_columns)]			
		for line in lines:
			for i in range(number_columns):
				self.data[-1][i].append(float(line.split(delim)[i]))				
		f.close()

		#loads the initial data if method reset is used afterwards
		self.file_name.append(file_name)
		self.header_saved = self.header[:]
		self.data_saved = self.data[:]





	def loadData(self,header,data,dataName):



		"""
		This method loads data from python lists
		header is the matrix saved in self.header
		data is the matrix saved in self.data
		dataName is the list of names (equivalent of file names)
		"""



		self.header.append(header)
		self.data.append(data)
		self.file_name.append(dataName)
		self.header_saved = self.header
		self.data_saved = self.data





	def reset(self):



		"""
		This method resets all the data from file_name
		"""



		self.header=self.header_saved
		self.data=self.data_saved





	def verticalPlot(self,data_index_list,list_x_Column,list_y_Column_list,xtype='lin',ytype='lin',symbol='default',
		title=None,legenda='default',x_title=None,y_title=None,legend_position='upper right',
		legend_size=10,x_limits='default',y_limits='default'):



		"""
		this method plots each entry of the input list yColumnList as a function of the input list list_x_Column
		data_index_list is a list of data list index
		list_x_Column is a list of X Columns (for each dataList)
		list_y_Column is a list of Y Columns (for each dataList)
		xtype is the x scale mode of the plot
		ytype is the y scale mode of the plot
		symbol is the symbol of the plot
		title is the title of the plot
		legenda is a list of legend with respect to the ploted data
		x_title is the x axis title
		y_title is the y axis title
		legend_position is the position of the legend (given by matplotlib)
		legend_size is the size of the legend
		x_limits is a list of 2 element: the first the minimum x value and the second the maximum x value to be plotted
		y_limits is a list of 2 element: the first the minimum y value and the second the maximum y value to be plotted
		"""



		if x_title != None:
			plt.xlabel(x_title)

		if y_title != None:
			plt.ylabel(y_title)

		if symbol=='default':
			symbol=['o-' for i in range(len(data_index_list))]

		#for only one plot
		if len(data_index_list)==1 and len(list_y_Column_list[0])==1:
			if len(list_y_Column_list[0])==1:
				plt.title(self.file_name[data_index_list[0]])
				if x_title == 'default':
					plt.xlabel(self.header[data_index_list[0]][list_x_Column[0]])
				if x_title == 'default':
					plt.ylabel(self.header[data_index_list[0]][list_y_Column_list[0][0]])
				plt.plot(self.data[data_index_list[0]][list_x_Column[0]],
					self.data[data_index_list[0]][list_y_Column_list[0][0]],symbol[0])
				if xtype!='lin':
					plt.xscale(xtype)
				if ytype!='lin':
					plt.yscale(ytype)

		#for multiplots
		else:

			if title != None:
				plt.title(title)

			for k in range(len(data_index_list)):
				j=0
				for i in list_y_Column_list[k]:
					if legenda == 'default':
						labell = self.file_name[data_index_list[k]]+'::'+self.header[data_index_list[k]][list_x_Column[k]]+'::'+self.header[data_index_list[k]][i]
					else:
						labell = legenda[k][j]
					plt.plot(self.data[data_index_list[k]][list_x_Column[k]],
						self.data[data_index_list[k]][i],symbol[k],
						label=labell)
					j=j+1
			plt.legend(loc=legend_position, shadow=False,prop={'size': legend_size})
			if xtype!='lin':
				plt.xscale(xtype)
			if ytype!='lin':
				plt.yscale(ytype)

		if x_limits!='default':
			plt.xlim(x_limits)
		if y_limits!='default':
			plt.xlim(y_limits)
		plt.show()











	def horizontalPlot(self, data_index_list, x_line_list, columns_list, x_line_value='default', x_column='default',
		symbol='o-', limits='default', xlabel='file column index', ylabel='value', x_shift='default', x_length='default',
		title='default',legend_position='upper right',legend_size=10,xtype='lin',ytype='lin'):



		"""
		This method plots the values of a line of the file as a function of column index
		data_index_list is a list of data list index
		x_line_list is a list of lists of the lines to be ploted. 
			If x_line_value is True, x_line_list is the value of the x_column.
		columns_list is a list of lists that indicate the range of indexes to be ploted
		xtype is the x scale mode of the plot
		ytype is the y scale mode of the plot
		x_column is a list of columns for the x values
		symbol is the symbol of the plot
		limits are the limits of the y scale
		xlabel is the name of the x axis
		ylabel is the name of the y axis
		x_shift is alists of the index correction
		x_length is a list of the space step. If default the x axis will only show the indexes. If a float number, the x
			axis will show the length accordingly
		legend_position is the position of the legend (given by matplotlib)
		legend_size is the size of the legend
		title is the title of the plot
		"""



		if x_line_value=='default':
			x_line_value=[True for i in range(len(data_index_list))]

		if x_column=='default':
			x_column=[0 for i in range(len(data_index_list))]

		if x_length=='default':
			x_length=['default' for i in range(len(data_index_list))]

		if x_shift=='default':
			x_shift=[0 for i in range(len(data_index_list))]

		if symbol=='default':
			symbol=['o-' for i in range(len(data_index_list))]

		if title !='default':
			plt.title(title)

		if len(x_line_list)==1:
			if len(data_index_list) == 1 and len(x_line_list[0]) == 1:
				title=self.file_name[data_index_list[0]]+'\n'+self.header[data_index_list[0]][x_column[0]].split('(')[0]+' ('+str(self.data[data_index_list[0]][x_column[0]][x_line_list[data_index_list[0]][0]])+' '+self.header[data_index_list[0]][x_column[0]].split('(')[1].split(')')[0]+')'
			else:
				title=self.file_name[data_index_list[0]]
			plt.title(title)

		for o in range(len(data_index_list)):

			if x_line_value[o]==True:
				templist=[]
				for value in x_line_list[o]:
					for j in self.data[data_index_list[o]][x_column[o]]:
						if value<j:
							templist.append(j)
							break
				x_line_list[o]=templist
				x_line_list[o] = [self.data[data_index_list[o]][x_column[o]].index(xline) for xline in x_line_list[o]]

			for k in range(len(x_line_list[o])):
				x=[]
				li=[]
				for i in range(columns_list[o][0],columns_list[o][1]):
					x.append(i-x_shift[o])
					li.append(self.data[data_index_list[o]][i][x_line_list[o][k]])
				if len(data_index_list) == 1:
					label=self.header[data_index_list[o]][x_column[o]].split('(')[0]+' = '+str(self.data[data_index_list[o]][x_column[o]][x_line_list[o][k]])+' '+self.header[data_index_list[o]][x_column[o]].split('(')[1].split(')')[0]
				else:
					label=self.header[data_index_list[o]][x_column[o]].split('(')[0]+' = '+str(self.data[data_index_list[o]][x_column[o]][x_line_list[o][k]])+' '+self.header[data_index_list[o]][x_column[o]].split('(')[1].split(')')[0]+' ('+self.file_name[o]+')'
				if x_length[o] != 'default':
					x=[i*x_length[o] for i in x]	
				if len(data_index_list) != 1 or len(x_line_list[o]) != 1:
					plt.plot(x,li,symbol,label=label)
				else:
					plt.plot(x,li,symbol)

		plt.legend(loc='upper left', shadow=True)
		if limits != 'default':
			plt.ylim(limits)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		if xtype!='lin':
			plt.xscale(xtype)
		if ytype!='lin':
			plt.yscale(ytype)
		plt.legend(loc=legend_position, shadow=False,prop={'size': legend_size})
		plt.show()