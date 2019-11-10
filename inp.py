import random
out=""
inp=""
for i in range(83200):
	a=random.randint(97,122)
	inp+=chr(a)
	a-=97
	a=(a+3+(4*i**3)%101)%26
	out+=chr(a+97)
inpfile=open("inp.txt","w")
outfile=open("out.txt","w")
inpfile.write(inp)
outfile.write(out)
inpfile.close()
outfile.close()