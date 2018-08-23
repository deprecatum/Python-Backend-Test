import BaseHTTPServer
import SocketServer

port=8080

#need to make a custom handler to interact with a requests content
class custom_handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def handle(self):
        print 'something'
        output = self.rfile.readline().strip()
        print output

    


handler=custom_handler

server=SocketServer.TCPServer(("localhost",port),handler)

server.serve_forever()

