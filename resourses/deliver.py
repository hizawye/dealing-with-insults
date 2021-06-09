"""
deleviring insults to main
"""

def insults():
	ins = []
	insults_ = []
	with open("resourses/insults.txt" , "r") as f :
		insults = f.readlines()
		for i in insults :
			ins.append(i)
	for i in ins :
		i = i[:-1]
		insults_.append(i)
	return tuple(insults_[::-2])
