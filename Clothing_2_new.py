class Clothing :
    stock = {'name' : [] , "material" : [] , 'amount' : []}

    def __init__(self,name) :
        material = ""
        self.name = name

    def add_item (self , name ,material ,amount) :
        Clothing.stock['name'].append(self.name)
        Clothing.stock['amount'].append(amount)
        Clothing.stock['material'].append(self.material)

    def Stock_by_Material(self,material) :
        count = 0
        n = 0
        for item in Clothing.stock['material'] :
            if item == material :
                count += Clothing.stock['amount'][n]
                n += 1
        return count

class shirt(Clothing) :
    material = "Cotton"

    def __str__(self) :
        return "{name}--{material}".format(name = self.name,material = self.material)

polo = shirt("Polo")
print(polo)

class pants(Clothing) :
    material = "Jeans"

    def __str__(self) :
        return "{name}--{material}".format(name = self.name,material = self.material)

levis = pants("Levis")
print(levis)


polo.add_item(polo.name, polo.material, 4)
print("After adding")
print(polo)

levis.add_item(levis.name, levis.material, 6)
print("After adding")
print(levis)


print(Clothing.stock)
