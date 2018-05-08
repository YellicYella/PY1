largest=None
smalest=None
while True:
    num=input('enter a number: ')
    if num=='done':
        break
    try:
        numb=int(num)
    except:
        pr='Invalid input'
        continue

    if largest is None:
        largest=numb
    elif numb>largest:
        largest=numb
    if smalest is None:
        smalest=numb
    elif numb<smalest:
        smalest=numb
print(pr)
print('Maximum is ', largest)
print('Minimum is ', smalest)
