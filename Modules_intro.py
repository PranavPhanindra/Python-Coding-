import random
import datetime

now = datetime.datetime.now()
print(random.randint(1,100))
print(now)
print(type(now))
print(now.year)
print(now.hour)
print(now.minute)

#timedelta class
print(now + datetime.timedelta(days = 200))
