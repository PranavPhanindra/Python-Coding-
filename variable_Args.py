def total(a = 10 ,*numbers , **phonebook) :     #Here a = 10 acts as a default value
     print("My favourite number is {} ".format(a))
     for num in numbers :
         print("num - {} ".format(num))

     for name , phonenumbers in phonebook.items() :
         print("{} -- {}".format(name,phonenumbers))

total(1,2,3,45,Jane = 1000 , John = 2312 ,Pranav = 10212    )
total(1,3231,13,123,1,12)
