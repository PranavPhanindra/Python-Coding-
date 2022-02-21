def mynum(a) :
    def num(a) :
        return a+1
    
    r = num(a)
    return r
print(mynum(100))


#Nested fns scope 

def dm(message) :
    "HI"
    def message_sender() :
        "nested fn"
        print(message)
    message_sender()

dm("WHat the hell")
