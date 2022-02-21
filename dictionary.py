#Here we are going to work with dictionaries
mycar = {"brand" : "Ferrari Sports",
        "model" : "Some random series ",
        "year" : "not 2020"
        } #this is a basic dictionary
print(mycar)
#we can create the same using a constructer also
mygreen = dict(fruit="green apples",vegetables = "cabbage")
print(mygreen)

#count key value pairs
print(len(mygreen))

mycar["year"]=2016
print(mycar)

#get value of a specified key
print(mycar.get("year"),"New value of  year in mycar")

#updating a dictionary to add new value
mycar.update({"Color" : "Blue"})
print(mycar)

#keys and values returns list of all keys and values respectively in an array from  a dictionary
print(mycar.keys())
print(mycar.values())

#we can remove by delete or pop
mycar.pop("Color")
print("After removing Color")
print(mycar)
del mycar["model"]
print("After removing model")
print(mycar)
print(mycar.items())
