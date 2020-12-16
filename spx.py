import yfinance as yf

spx = yf.Ticker("^GSPC")
hist = spx.history(period="50y")
hist=hist.reset_index()


def wdfun(mywd,delta):
  print(mywd, " ", delta)
  p = delta%5
  if int(mywd) > p:
    print(str((int(mywd) - p)))
  else:
    print(str(5 + (int(mywd) - p)))
  
  c=0
  cup=0
  for i in hist.index: 
    wd=hist.Date[i].strftime("%w")
    if wd==mywd:  #0Sunday, 1Monday,2345, 6-Saturday
      if i-delta>=0:
        c=c+1
        if hist.Close[i]>hist.Close[i-delta]:
          cup=cup+1 
  perc=cup/c        
  return(perc)
  
p=wdfun("5",1)          #arg1=weekday, arg2: 1- from previouse day, 2- from previous 2 days
print("cup/c={:.2f}".format(p))


"""
def avgdays(days):
  loop (i-days..i):
   sum hist.Close[i]/days
"""
