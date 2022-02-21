#initialization of variables
n1,n2 = 15,20

#finds maximum
if(n1 > n2):
    m = n1
else:
    m = n2

while(True):
    if((m % n1 == 0) and (m % n2 == 0)) :
        print(m)
        break;
    m = m+1
    print(m)
print("LCM of 15,20 is " + str(m))
