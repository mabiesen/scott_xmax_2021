def fibonacci(iMax):
	x=[1,2]
	while True:
		xTemp=x[-1]+x[-2]
		if xTemp>iMax:
			return x
		else:
			x.append(xTemp)

def sumevenvalues(x):
	y=0
	for ix in x:
		if ix%2 == 0:
			y=y+ix
	return y

print(sumevenvalues(fibonacci(4000000)))
