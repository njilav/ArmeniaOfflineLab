import socket, time, requests, base64

server_script_url = 'https://81.4.103.204/dns.php'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 53))

while True:
	data, addr = sock.recvfrom(200000)
	data_b64 = base64.b64encode(data)
	r = requests.post(server_script_url, data = {'query': data_b64}, verify = False)
	sock.sendto(base64.b64decode(r.text), addr)
sock.close()
