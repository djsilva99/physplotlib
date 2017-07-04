import matplotlib.pyplot as plt
import matplotlib.animation as animation









class dyplot:





	"""
	The dyplot class allows one to load data from txt files, refreshing the plot constantly while the sourse 
	file is being changed
	"""





	def __init__(self,fileName,header=True,delim=','):



		"""
		filemName is the file name
		header is a bolean that tells if the file has a header
		delim is a string that indicates the separation of the column
		"""



		self.delim=delim
		self.fig = None 
		self.xColumn = None
		self.yColumnsList = []
		self.fileName = fileName
		self.initialValue = None
		self.finalValue =None
		self.ax1 = None
		self.headerState=header
		f=open(fileName,'r')
		lines=f.readlines()
		f.close()
		self.header=[]
		if header==True:
			for i in range(len(lines[0].split(delim))):
				self.header.append(lines[0].split(delim)[i])





	def animateVertical(self,i):



		"""
		This method is used to make vertical plots when verticalPlot method is called
		"""



		graph_data = open(self.fileName,'r').read()
		lines = graph_data.split('\n')
		if self.headerState==True:
			lines=lines[1:]
		xs = []
		ys = []
		li = []
		for i in self.yColumnsList:
			li.append([])	
		for line in lines:
			if len(line) > 1:
				lineArray=line.split(self.delim)
				xs.append(lineArray[self.xColumn])
				for i in range(len(self.yColumnsList)):
					li[i].append(float(lineArray[self.yColumnsList[i]]))
		self.ax1.clear()
		for i in range(len(self.yColumnsList)):
			string=str(self.header[self.yColumnsList[i]])
			self.ax1.plot(xs,li[i],'o-',label=string)
			self.ax1.axes.set_xlabel(self.header[self.xColumn])
		legend = self.ax1.legend(loc='upper left', shadow=True)





	def animateHorizontal(self,i):



		"""
		This method is used to make vertical plots when horizontalPlot method is called
		"""



		graph_data = open(self.fileName,'r').read()
		lines = graph_data.split('\n')
		if self.headerState==True:
			lines=lines[1:]
		xs = [i+self.xShift for i in range(self.initialValue,self.finalValue)]
		if self.xLength != 'default':
			xs=[x*self.xLength for x in xs]
		ys = []
		li=lines[-2].split(self.delim)
		li=[float(lis) for lis in li]
		if self.xColumn != 'default':
			title= self.fileName+'\n'+self.header[self.xColumn].split('(')[0]+' = '+str(li[self.xColumn])+' '+self.header[self.xColumn].split('(')[1].split(')')[0] 
		for i in range(self.initialValue):
			li.pop(0)
		for i in range(len(li)-(self.finalValue-self.initialValue)):
			li.pop()
		self.ax1.clear()
		if self.limits != 'default':
			self.ax1.axes.set_ylim(self.limits)
		#print len(xs),len(li)
		self.ax1.plot(xs,li,self.symbol,label='temp')
		#legend = self.ax1.legend(loc='upper left', shadow=True)
		self.ax1.set_xlim([min(xs),max(xs)])
		self.ax1.set_xlabel(self.xlabel)
		self.ax1.set_ylabel(self.ylabel)
		if self.xColumn != 'default':
			self.ax1.set_title(title)





	def verticalPlot(self,xColumn,yColumnsList, timeInterval=1000):



		"""
		this method plots each entry of the input list yColumnList as a function of the input list xColumn
		time interval is the refreshing time step in miliseconds
		"""



		self.fig = plt.figure()
		self.ax1 = self.fig.add_subplot(1,1,1)
		self.xColumn = None
		self.yColumnsList = []
		self.xColumn = xColumn
		self.yColumnsList = yColumnsList
		ani = animation.FuncAnimation(self.fig,self.animateVertical,interval=timeInterval)
		plt.show(block=False)





	def horizontalPlot(self,columns, xColumn='default',limits='default',xShift=0,xLength='default',
		xlabel='file column index',ylabel='value',timeInterval=1000,symbol='o-'):



		"""
		This method plots the values of the last line of the file as a function of column index.
		columns is a entry lists that indicates the range of indexes to be ploted
		time interval is the refreshing time step in miliseconds
		symbol is the symbol of the plot
		xlabel is the name of the x axis
		ylabel is the name of the y axis
		limits are the limits of the y scale
		xShift is the correction of the index
		xLength is the space step. If default the x axis will only show the indexes. If a float number, the x
			axis will show the length accordingly
		"""



		self.symbol=symbol
		self.xlabel=xlabel
		self.ylabel=ylabel
		self.xShift=xShift
		self.xLength=xLength
		self.limits=limits
		self.fig = plt.figure()
		self.ax1 = self.fig.add_subplot(1,1,1)
		self.xColumn = xColumn
		self.yColumnsList = []
		self.initialValue = columns[0]
		self.finalValue = columns[1]
		ani = animation.FuncAnimation(self.fig,self.animateHorizontal,interval=timeInterval)
		plt.show()