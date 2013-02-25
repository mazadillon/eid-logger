import serial
from pygame import mixer
from datetime import date

mixer.init()
ping=mixer.Sound("ping.wav")
buzzer=mixer.Sound("buzzer.wav")
date = datetime.today()

def logFile():
	try:
		# If USB disk is mounted then use that
	   f = open('/media/usb/eid-logger.cfg')
	   log = '/media/usb/'+date.isoformat()+'-cattle.txt'
	   f.close()
	except IOError as e:
		# Otherwise use local log file
	   log = date.isoformat()+'-cattle.txt'
	return log

def matchCow(cow):
	f = open(logFile())
	for line in f.readlines():
		line = line.strip()
		if cow == line:
			f.close()
			return True
	f.close()
	return False

def countList():
	with open(logFile()) as f:
		for i, l in enumerate(f):
			pass
	return str(i + 1)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)
while ser:
	line = ser.readline().decode('ascii').strip()
	if line != '':
		if matchCow(line) == False:
			f = open(logFile(),'a')
			f.write(line + "\n")
			f.close()
			print(line + ' added to file')
			ping.play()
		else:
			buzzer.play()
		print(countList() + ' cattle on list')
ser.close()