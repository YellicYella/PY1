hrs=input('enter hours:\n')
try:
    H=float(hrs)
except:
    print('error, enter numeric input')
    quit()
rte=input('enter rate:\n')
try:
    R=float(rte)
except:
    print('error, enter numeric input')
    quit()
if H>40:
    pay=40*R+(H-40)*1.5*R
else:
    pay=H*R
print('pay is:', pay)
