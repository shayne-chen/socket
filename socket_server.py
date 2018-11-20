import socket, base64, os, threading

def judgefile(file_des):
	if os.path.exists(file_des):
		os.remove(file_des)

def recv_file(conn, file_des):
	while True:
		data = conn.recv(1024)
		if not data:
			break
		else:
			decode_code = base64.b64decode(data)
			with open(file_des, "ab") as f:
				f.write(decode_code)

if __name__ == '__main__':
	sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sk.bind(("127.0.0.1", 12138))
	sk.listen(5)
	img_des = "/Users/shawn/Downloads/test_copy.jpg"
	judgefile(img_des)
	while True:
		conn, addr = sk.accept()
		conn.sendall(bytes("Connected success...", encoding="utf-8"))
		t = threading.Thread(target=recv_file, args=(conn,img_des,))
		t.start()