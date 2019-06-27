import pyfirmata
import time
import http.client, urllib

board = pyfirmata.Arduino("/dev/ttyACM0")
pin0  = board.get_pin('a:0:i')

iterator = pyfirmata.util.Iterator(board)
iterator.start()
pin0.enable_reporting()

while True:
	if pin0.read() == None:
		pass
	else:
		x = (1000 * pin0.read())/73.07
		print("pH air: "+str(x))
		params = urllib.parse.urlencode({'field1': x, 'key': 'GH5Q05V3AUXZ66GX'})
		headers = {"Content-typZZe": "application/x-www-forn-urlencoded", "Accept": "text/plain"}
		conn = http.client.HTTPConnection("api.thingspeak.com:80")
		try:
			conn.request("POST", "/update", params, headers)
			response = conn.getresponse()
			print(response.status, response.reason)
			data = response.read()
			conn.close()
		except:
			print("Connection failed")

time.sleep(2)

