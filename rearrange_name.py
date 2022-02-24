import re

def rearrange_name(name) :

     result = re.search(r"^([\w.]*).* \s*([\w.]*)" ,name)

     if result is None :
         return name

     else :
         return "{} {}".format(result[2],result[1])


name = input("Kindly enter ur name  : ")

print(rearrange_name(name))
