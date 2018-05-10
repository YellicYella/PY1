score=input('Enter score:')
try:
    SC=float(score)
except:
    print('enter numerical value between 0.0 and 1.0')
    quit()
if SC<=1.0:
    if SC>=0.9:
        print('A')
    elif SC>=0.8:
        print('B')
    elif SC>=0.7:
        print('C')
    elif SC>=0.6:
        print('D')
    elif SC>=0.0:
        print('F')
    elif SC<0.0:
        print('Entered value is out of range')
else:
    print ('Entered value is out of range')
