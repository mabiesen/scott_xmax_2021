def factor(iMax):
	x=[]
	for i in range(iMax):
		if i%3==0 or i%5==0:
			x.append(i)
	return x

def sumarray(x):
	xsum=0
	for i in x:
		xsum=xsum+i
	return xsum

result=sumarray(factor(1000))
print(result)	
