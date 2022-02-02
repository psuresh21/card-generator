import datetime
import random

m = ['visa','visaE','mastercard','JCB','discover']

print("---------------------------------------------------------")
mydt = datetime.datetime.now()
print("welcome to credit/debit card generator")
print("it will generate a random cards for you")
print("Copyright (c) " + mydt.strftime("%Y") + " Suresh Pandiyan \n")


option = 1
for op in m:
	print(str(option)+"." +op)
	option += 1
print("if you like to stop the random running, JUST PRESS CONTROL + C at any time")	

ask_q = int(input("choose the number above "))
	
def options(s):
	if s == 1:
		return str(random.randint(4000500030005000,4600600050006000))
	if s == 2:
		return str(random.randint(4000000000000000,4600000000000000))
	if s == 3:
		return str(random.randint(5004003002001000,5506006006005000))
	if s == 4:
		return str(random.randint(3500000000000000,3599999999999999))
	if s == 5:
		return str(random.randint(6510000000000000,6590000000000000))

	
i = 0
while i < 1000000000000:
	rand_num = options(ask_q)
	#rand_num = str(random.randint(4000000000000000,4600000000000000))

	s = ''.join(str(rand_num))

	even = s[0:16:2]

	ss = [int(even[0]) + int(even[0]),int(even[1]) + int(even[1]),int(even[2]) + int(even[2]),int(even[3]) + int(even[3]),int(even[4]) + int(even[4]),int(even[5]) + int(even[5]),int(even[6]) + int(even[6]),int(even[7]) + int(even[7])]



	now = []
	for m in ss:
		now.append(m)
		

	#print(now)

	def sorty(j):
		if j > 9:
			x = str(j)[0:1]
			y = str(j)[1:2]
			z = int(x) + int(y)
			return z
		else:
			return j

	comp = []
	for equal in now:
		comp.append(str(sorty(equal)))

	comp = ''.join(comp)
	#print(comp)

	first = comp[0] + rand_num[1] + comp[1] + rand_num[3] + comp[2] + rand_num[5] + comp[3] + rand_num[7] + comp[4] + rand_num[9] + comp[5] + rand_num[11] + comp[6] + rand_num[13] +  comp[7] + rand_num[15]

	#print(first)


	alls = int(comp[0]) + int(rand_num[1]) + int(comp[1]) + int(rand_num[3]) + int(comp[2]) + int(rand_num[5]) + int(comp[3]) + int(rand_num[7]) + int(comp[4]) + int(rand_num[9]) + int(comp[5]) + int(rand_num[11]) + int(comp[6]) + int(rand_num[13]) +  int(comp[7]) + int(rand_num[15])

	#print(alls)

	def passorfailed():
		try:
			if int(str(alls)[1:2]) == 0:
				return "pass"
			else:
				return "failed"
		except:
			if int(str(alls)[2:3]) == 0:
				return "pass"
			else:
				return "fail"
	
	print(s, passorfailed())
	
