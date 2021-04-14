n = input("")
prevValues = []
step =0
def decrease():
    if n in prevValues:
        return
    else:
        if(n/2==0):
            step=step+1
            n=n/2
        else:
            decrease(n-1)
            decrease(n+1)


while(True):
    if(n==1):
        print(step)
        break
    else:
        prevValues.append(n)
        decrease()

