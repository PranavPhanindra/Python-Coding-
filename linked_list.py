class node :
  def __init__(self,value) :
    self.value = value
    self.next = None


class linked_list :
  
  def __init__(self, head=None):
    self.head = head
  
  def append(self,new_node) :
    current = self.head 
    if self.head :
      while current.next :
        current = current.next 
      current.next = new_node
    else :
      self.head = new_node
  
  def printing(self) :
    current = self.head 
    while current :
      print(current.value,end = ' -> ')
      current = current.next
    print("NULL")

  #This would return the node in that position
  def get_position(self,position):
    if position >= 1 :
       current = self.head
       p = 1
       while current and p != position :
         current = current.next
         p += 1
       if p < position and current == None :
         print ("The linked list is smaller - we return head ")
         return None
       else :
         return current 
    else :
      print("Incorrect Value for position")
      return
   
e1 = node(1)
e2 = node(2)
e3 = node(3)
e4 = node(4)
e5 = node(5)


ll = linked_list(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)


ll.printing()
print (ll.get_position(100).value)
