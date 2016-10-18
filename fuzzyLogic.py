young = list(range(0, 40))
adult = list(range(25, 75))
old = list(range(60, 100))


veryCheap = list(range(0, 20))
cheap = list(range(15, 35))
fair = list(range(30, 50))
expensive = list(range(45, 65))
veryExpensive = list(range(60, 80))


def getAge(age):
	if age >= 100:
		return 3
	try:
		rangeYoung = young.index(age)
	except Exception:
		rangeYoung = 0
	try:
		rangeAdult = adult.index(age)
	except Exception:
		rangeAdult = 0
	try:
		rangeOld = old.index(age)
	except Exception:
		rangeOld = 0
	
	data = []
	data.append(int(len(young)/2)-rangeYoung)
	data.append(int(len(adult)/2)-rangeAdult)
	data.append(int(len(old)/2)-rangeOld)

	return (data.index(min(data))+1)

def getPrice(price):
	if price >= 80:
		return 5
	try:
		rangeVeryExpensive = veryExpensive.index(price)
	except Exception:
		rangeVeryExpensive = 0
	try:
		rangeExpensive = expensive.index(price)
	except Exception:
		rangeExpensive = 0
	try:
		rangeFair = fair.index(price)
	except Exception:
		rangeFair = 0
	try:
		rangeCheap = cheap.index(price)
	except Exception:
		rangeCheap = 0
	try:
		rangeVeryCheap = veryCheap.index(price)
	except Exception:
		rangeVeryCheap = 0
	
	
	data = []
	data.append(int(len(veryCheap)/2)-rangeVeryCheap)
	data.append(int(len(cheap)/2)-rangeCheap)
	data.append(int(len(fair)/2)-rangeFair)
	data.append(int(len(expensive)/2)-rangeExpensive)
	data.append(int(len(veryExpensive)/2)-rangeVeryExpensive)

	return (data.index(min(data))+1)

