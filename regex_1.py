import re
def check_aei (text):
  result = re.search(r"a.e.i", text,re.IGNORECASE)
  #result = re.search(r"[aei]", text,re.IGNORECASE)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
