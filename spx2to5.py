import yfinance as yf
from datetime import datetime,timedelta

def myfun(bstr,estr):
	print(bstr,estr)
	hist = yf.download("^GSPC", start=bstr, end=estr)
	hist=hist.reset_index()
	#print(hist)

	pclose=hist.Close
	plow=hist.Low
	popen=hist.Open
	pd=hist.Date
	pnum=pclose.size  #size 50: 0-49

	#print("pnum=",str(pnum))
					
	pos=2   #the 1st position

	####### Everyday ####################################################
	c=0
	cup=0

	for i in range(pos, pnum): # i: 1-49, i-1:0-48
		c=c+1
		if pclose[i]>pclose[i-1]:  
			cup=cup+1
	r=cup/c       
	print("Everyday:\t\t\t", c, " ", cup, " cup/c={:.2f}".format(r))    



	####### Tuesday Friday #######################################################
	weekdaylist=['Monday','Tuesday','Wednesday','Thursday','Friday']
	bwd='Tuesday'
	ewd='Friday'

	c=0
	cup=0

	for i in range(pos, pnum): # i: 1-49, i-1:0-4
		d=i+weekdaylist.index(ewd)-weekdaylist.index(bwd)
		#print(str(d))
		
		if  pd[i].strftime("%A")==bwd and d<pnum:
			#if pd[d].strftime("%A")==ewd:
			if pd[d].strftime("%A")==ewd and pclose[i]-pclose[i-1]>0:     #Tuesday in, Friday out, Tuesday > Monday (75%, 63%)
				c=c+1
				#print(pd[i], "\t{:.1f}".format(pclose[i]), "\t{:.1f}".format(pclose[d]), "\t{:.1f}".format(pclose[d]-pclose[i]), end='')              
				if pclose[d]-pclose[i]>0:  
					cup=cup+1
					#print("   *")
				else:
					#print()
					pass            

	if c!=0:
	  r=cup/c       
	  print(bwd, ewd, ":\t\t", c, " ", cup, " cup/c={:.2f}".format(r))    
					
#data = yf.download("^GSPC", start="2021-01-01", end="2017-04-30")
#hist = yf.download("^GSPC", start="2020-08-24")

today = datetime.today()

tomorrow = today + timedelta(days=1)
tstr=tomorrow.strftime("%Y-%m-%d")

n=10
for i in range(1,n):   #1..n-1
  bday = tomorrow - timedelta(days=365*i)
  eday = tomorrow - timedelta(days=365*(i-1))
  bstr=bday.strftime("%Y-%m-%d")
  estr=eday.strftime("%Y-%m-%d")
  #print(bstr, estr)
  myfun(bstr,estr)
print("=====================================================================================")
