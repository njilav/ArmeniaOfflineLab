import socket, time, requests, base64

try:
	requests.packages.urllib3.disable_warnings()
except:
	pass
server_script_url = 'https://server_ip/dns.php'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 53))

while True:
	data, addr = sock.recvfrom(200000)
	data_b64 = base64.b64encode(data)
	print("Request received in base64: " + data_b64)
	r = requests.post(server_script_url, data = {'query': data_b64}, verify = False)
	print("Response received in base64: " + r.text)
	sock.sendto(base64.b64decode(r.text), addr)
sock.close()
