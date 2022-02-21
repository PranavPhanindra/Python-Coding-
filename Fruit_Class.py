class fruit : 
    def __init__(self,color,taste) : 
        self.color = color
        self.taste = taste
    def __str__(self) :
        return "This fruit is {} in color and tastes {}.".format(self.color,self.taste)
class apple(fruit) :
    pass
class grape(fruit) :
    pass


a = apple('red',"sweet")

b = grape('green' , 'tart')

print(a)
print(b)
