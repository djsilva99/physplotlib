import matplotlib.pyplot as plt


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



