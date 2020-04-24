import sys
import os.path
import uuid
from glob import glob
from datetime import datetime
import cgi, cgitb

class HttpServer:
	def __init__(self):
		self.sessions={}
		self.types={}
		self.types['.pdf']='application/pdf'
		self.types['.jpg']='image/jpeg'
		self.types['.txt']='text/plain'
		self.types['.html']='text/html'
	def response(self,kode=404,message='Not Found',messagebody='',headers={}):
		tanggal = datetime.now().strftime('%c')
		resp=[]
		resp.append("HTTP/1.0 {} {}\r\n" . format(kode,message))
		resp.append("Date: {}\r\n" . format(tanggal))
		resp.append("Connection: close\r\n")
		resp.append("Server: myserver/1.0\r\n")
		resp.append("Content-Length: {}\r\n" . format(len(messagebody)))
		for kk in headers:
			resp.append("{}:{}\r\n" . format(kk,headers[kk]))
		resp.append("\r\n")
		resp.append("{}" . format(messagebody))
		response_str=''
		for i in resp:	
			response_str="{}{}" . format(response_str,i)
		return response_str

	def proses(self,data):
		
		requests = data.split("\r\n")
		#print(requests)

		baris = requests[0]
		#print(baris)

		all_headers = [n for n in requests[1:] if n!='']

		j = baris.split(" ")
		try:
			method=j[0].upper().strip()
			if (method=='GET'):
				object_address = j[1].strip()
				print("ini addressnya "+object_address)
				return self.http_get(object_address, all_headers)
			if (method=='POST'):
				object_address = j[1].strip()
				val = requests[-1].split("=")
				return self.http_post(object_address, all_headers,val)
			else:
				return self.response(400,'Bad Request dalem','',{})
		except IndexError:
			return self.response(400,'Bad Request','',{})
	def http_get(self,object_address,headers):
		files = glob('./*')
		if os.name == 'nt':
			for n in files:
				temp = [n.replace('\\','/') for n in files]
				files = temp
		file_loc = '.'+object_address
		# print("ini loc"+loc)
		if file_loc not in files:
			return self.response(404, 'Not Found', '', {})
		fp = open(file_loc,'r')
		isi = fp.read()
	
		headers={}
		headers['Content-type']="text/html"
		
		return self.response(200,'OK',isi,headers)
	def http_post(self,object_address,headers,val):
		h = headers
		string = ""
		for i in h:
			string = string+'\n'+i
		print("string = "+string)
		isi = val[1]+"\n"+string
		# isi = "kosong"
		# headers={}
		print(isi)
		return self.response(200,'OK',isi,headers)

if __name__=="__main__":
	httpserver = HttpServer()















