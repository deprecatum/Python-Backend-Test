
import SocketServer

port=8080

#need to make a custom handler to interact with a requests content
class custom_handler(SocketServer.StreamRequestHandler):
#use streamrequest instead of base, so its possible to manipulate data as files

    def handle(self):
        print 'something'
        #output = self.rfile.readline()
        #print output

    


handler=custom_handler

server=SocketServer.TCPServer(("localhost",port),handler)
server.serve_forever()
