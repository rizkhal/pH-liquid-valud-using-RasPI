import pyfirmata
import time
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
        data = (1000 * pin0.read())/73.07
        print("pH air: "+str(data))

time.sleep(10.0 - ((time.time() - starttime) % 10.0))
