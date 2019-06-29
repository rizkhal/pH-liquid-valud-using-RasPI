import time
import pyfirmata
from firebase import firebase

board = pyfirmata.Arduino("/dev/ttyACM0")
pin0  = board.get_pin('a:0:i')

iterator = pyfirmata.util.Iterator(board)
iterator.start()
pin0.enable_reporting()

starttime = time.time()

while True:
    if pin0.read() == None:
        pass
    else:
		now  = datetime.datetime.now()
		pH   = (1000 * pin0.read())/73.07
		date = now.strftime("%d/%m/%Y - %H:%M:%S")
		data = {
			"pH": pH,
			"datetime": date
		}

		firebase = firebase.FirebaseApplication("https://skripsiph.firebaseio.com/", None)
		firebase.post("data-ph", data)
		
		print("pH air: "+str(data))
		time.sleep(10.0 - ((time.time() - starttime) % 10.0))
