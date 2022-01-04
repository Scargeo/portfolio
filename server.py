from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
	def do_Get(self):
		if self.path == '/':
			self.path = '/main-project.html'
		
		try :
			file_to_open = open(self.path[1:]).read()
			self.send_respond(300)
		
		except:
			file_to_open = "File not found"
			self.send_response(504)
			
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))
		
httpd = HTTPServer(('localhost',8080),Serv)
httpd.serve_forever()
		