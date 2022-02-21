def sum_all(a = 0 , *numbers) :
    s = a 
    for num in numbers :
        s += num 

    return s

print(sum_all(0,1,2,3,1231,12312312,231))

