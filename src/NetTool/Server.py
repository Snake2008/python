import socket;

ASSETPORT = 10006

class Server:

    def __init__(self,addr,port = ASSETPORT):
        assert(type(addr) == str)
        self.socket = socket.socket()
        self.socket.bind((addr,port))
        self.socket.listen(1)
        print(self.socket)
    
    def Accept(self, parameter_list):
        pass



