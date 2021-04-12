
    
def computepay(workhour,workrate):
hours = input("Enter Hours of work:")
workhours = float(hours)
rate = input("Enter Rate of work:")
workrate = float(rate)
pay = ( workhour * workrate )
if workhours <= 40 :
return(pay)
else :
overhours = (workhour-40)
regular = (workrate*40)
others = overhours * (workrate *1.5)
overpay = (regular + others)
return(ovrpay)
print(computepay(45,10.5))
