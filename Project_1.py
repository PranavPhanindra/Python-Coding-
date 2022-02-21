"""
Report that tracks the use of machines.
Write a script that generates a report of which users are logged in to which machines at that time.


"""

#Event class
class Event:
    """
    This is an event class
    Here we describe about the event with atttributes
    type,date,on which machine it occured and the user by which it occured
    event_types = login / logout
    """
    def __init__(self,date,type,machine_name,user_name) :
        """This is the constructor"""
        self.date = date
        self.type = type
        self.machine_name = machine_name
        self.user_name = user_name


"""
To remember is sort() is a method on lists that modifies the list itself and sorted()
is a function that takes a parameter and returns a new sorted list but doesnt modify
the existing list
sort method takes a key as sorting key it can be anything

"""
events = [
Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
"""
print("Printing the events ...")
for event in events :
    print("{}--{}--{}--{}".format(event.type,event.date,event.machine_name,event.user_name))
"""

"""
 Since it is important to have the events ordered in chronological order we would order
 the list of events using the time as key
 login we would add the user to the list of users that are logged in else we would rmeove the user
 we would use a set to store all the users and we would make a dictionary of machine : users
 """
"""
First in order to sort the events chronologically we would try to get the date
and use that as key and ordered
"""
def get_event_date(event) :
    return event.date

"""
print("Printing dates of list of events.......")
for event in events :
    print(get_event_date(event))
"""
"""
Now we try to find users who are currently logged in
"""
def current_users(events) :
    """1st we sort the list in a chronological order """
    events.sort(key = get_event_date)
    """
    Since we planned to have a dictionary of machine_name : set of user_names
    Initialize an empty dictionary
    """
    machines = {}
    for event in events :
        """If its the 1st occurance """
        if event.machine_name not in machines.keys() :
            machines[event.machine_name] = set()
        """
        If we have a machine we would check the event type
        If its a login we would add user_name of that machine_name's value in machines' dictionary
        """
        if event.type == "login" :
            machines[event.machine_name].add(event.user_name)
            """
            If we have the event to be logout we must 1st check if user_name is in
            the set or not if it is we would simply remove
            If it is not that would mean his login event must have been not recorded
            or some unusual way it must have occured
            """
        elif (event.type == "logout") and (event.user_name in machines[event.machine_name]) :
            machines[event.machine_name].remove(event.user_name)
        else :
            print("Undefined Login --- " + event.user_name + " on " + event.machine_name)
    return machines

def print_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

users = current_users(events)
print(users)
print_report(users)
