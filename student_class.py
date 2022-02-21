class student :
    static
    def __init__(self, name = "Student" , regno = 000000 ) :
        #Set a default constructor
        self.name = name 
        self.regno = regno
    def __str__(self) :
        return "{name} -- {regno}".format(name = self.name , regno = self.regno)


s1 = student()
print(s1)

s2 = student("Pranav",181214)
print(s2)



