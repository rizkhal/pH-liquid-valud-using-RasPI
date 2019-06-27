import pyfirmata
import time
from firebase import firebase
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
        #print(pin0.read())
        data = (1000 * pin0.read())/73.07
        print("pH air: "+str(data))
        #firebase = firebase.FirebaseApplication("https://skripsiph.firebaseio.com/")
        #try:
        #    result = firebase.post('/data-ph', data)
        #except:
        #    print("Connection failed!")
time.sleep(1)

