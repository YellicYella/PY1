hrs=input('enter hours:\n')
rte=input('enter rate:\n')
H=float(hrs)
R=float(rte)
if H>40:
    pay=40*R+(H-40)*1.5*R
else:
    pay=H*R
print(pay)
