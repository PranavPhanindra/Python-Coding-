class Apple :
    #Here we are using __init__ inorder to have the constructor
    #The self key word would refer to the object that calls the function

    """def __init__(self) :
        self.color = "Colorless"
        self.taste = "Tasteless"""
    #__init__ is a special method - special methods start and end with '__'
    def __init__(self,color,taste):
        self.color = color
        self.taste = taste

    #THis is some sort overload to a printing function
    #THis reduces the no of lines to be written inrder to print data of an object
    def __str__(self):
        return "This apple is {} and its tastes {}".format(self.color,self.taste)
    def print_apple(self) :
        print("{} -- {}".format(self.color,self.taste))

"""tim =  Apple()
print(tim)"""
jonagold = Apple("Green","Sour")
jonagold.print_apple()
print(jonagold)
