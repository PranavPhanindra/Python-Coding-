class Clothing:
    """
    This is a class that contains the account of name ,material and amount of a certain
    class of clothes can be shirt or pant current_stock
    Each of the attribute is a mutable object of list and contained in a dictionary
    """
    stock={ 'name': [],'material' :[], 'amount':[]}

    def __init__(self,name):
        material = ""
        self.name = name

    def __str__(self) :
        for i in Clothing.stock['name']:
            print(i)

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['amount'].append(amount)
        Clothing.stock['material'].append(self.material)
    def Stock_by_Material(self, material):
        count=0
        n=0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n+=1
        return count
class shirt(Clothing):
    material="Cotton"

class pants(Clothing):
    material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")

polo.add_item(polo.name, polo.material, 4)

sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
print(polo.name)
print(polo.material)
print(polo.stock)
