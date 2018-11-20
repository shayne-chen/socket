import socket, base64, os

def sendfile(filepath):
	if not os.path.exists(filepath):
		print ("File is not exists")
	
	sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sk.connect(("127.0.0.1", 12138))
	sk.settimeout(5)
	print (sk.recv(1024))
	
	with open(filepath, "rb") as f:
		datas = base64.b64encode(f.read())
	sk.sendall(datas)

if __name__ == '__main__':
	filepath = "/Users/shawn/Downloads/test.jpg"
	sendfile(filepath)