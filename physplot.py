import matplotlib.pyplot as plt



class physplot:

	def __init__(self,fileName,start=0,stop=-1,delim=','):

		f=open(file,'r')
		lines=f.readlines()

		self.header=[]
		for i in range(len(lines[0].split(delim))):
			header.append(lines[0].split(delim)[i])

		self.numberColumns = len(lines[start])

		for i in range(start):
			lines.pop(0)

		self.data = [None for i in range(numberColumns)]			
		for line in lines:
			for i in range(numberColumns):
				self.data[i].append(float(line.split(delim)[i]))				

		f.close()


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





	def plot(self,xColumn,yColumns):

		if xColumn==-1:
			xColumn=range(len(self.data[i]))

		for yColumn in yColumns:
			plt.plot(xColumn,yColumn,'o')

		plt.show()		


"""



#file to be read
file='M6_l2_C5L3_0004.lvm'
f=open(file,'r')
lines=f.readlines()

#reads and selects the data from endurence tests
Ron=[]
Roff=[]
for i in range(1,len(lines)):
	if i%10==0:
		Roff.append(float(lines[i].split('\t')[2]))
	if (i+5)%10==0:
		Ron.append(float(lines[i].split('\t')[2]))
f.close()

#saves the data to file savedFile.csv
savedFile=open('savedFile.csv','w')
for i in range(len(Ron)):
	savedFile.write(str(i)+','+str(Ron[i])+','+str(Roff[i])+'\n')
savedFile.close()

#plots the data
plt.plot(range(len(Ron)),Ron,'ro')
plt.plot(range(len(Roff)),Roff,'bo')
plt.show()


"""
