def computepay(H,R):
    if H>40:
        pay=40*R+(H-40)*1.5*R
    else:
        pay=H*R
    return pay

def numcheck_flt(n):
    try:
        N=float(n)
        return N
    except:
        print('error, enter numerical input')
        quit()

hrs=input('enter hours:\n')
h=numcheck_flt(hrs)
rte=input('enter rate:\n')
r=numcheck_flt(rte)

P=computepay(h,r)
print('pay',P)
