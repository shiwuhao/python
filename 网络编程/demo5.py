# /usr/bin/env python3
from socketserver import TCPServer, StreamRequestHandler


class Handle(StreamRequestHandler):

    def Handler(self):
        addr = self.request.getpeername()
        print('Got connect from', addr)
        self.wfile.write('Think you for connecting')


server = TCPServer(('', 1234), Handle)
server.serve_forever()
