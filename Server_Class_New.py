import random

class Server :

    def __init__(self) :
        self.connections = {}

    def add_connection(self,connection_id) :
        print("Adding "+connection_id)
        self.connections[connection_id] = random.randint(1,10)
        print("Added " + connection_id)

    def close_connection(self,connection_id) :
        if connection_id in  self.connections.keys() :
            del self.connections[connection_id]
            print("Deleted "+connection_id)

    def load(self) :
        total = 0
        for load in self.connections.values() :
            total += load

        return total

    def __str__(self) :
        return "Total load on server -- {:.2f}%".format(self.load())


#defining a server instance
server = Server()

#Adding a server connection
server.add_connection("192.168.1.1")
server.add_connection("192.168.1.90")

#Printing all the servers and load on each servers as a dictionary
print("Printing all connections...")
print(server.connections)

#Printing total load on each server
print(server.load())
print(server)
#Deleting a connection
server.close_connection("192.168.1.1")

#Printing all connections after removing one of them
print(server.connections)

#Printing total load now after removing a connection
print(server.load())


#defning a LoadBalancing class
class LoadBalancing :

    def __init__(self) :
        #defining an empty dictionary of connections
        self.connections = {}

        """
        Inorder to choose randomly from a server we would defines a
        list of servers having one server minimum
        """
        self.servers = [Server()]

    def add_connection(self,connection_id) :
        """
        Randomly choose a server and to serve the connections
        and then pass connection to the server
        """
        server = random.choice(self.servers)
        #Serve the connection
        self.connections[server] = server
        #Actually now in connections we would have the server as an instace of server class
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self,connection_id) :
        for connection in self.connections.keys() :
            if connection == connection_id :
                server_of_connection = self.connections[connection]
        server_of_connection.close_connection(connection_id)
        del self.connections[connection_id]    
