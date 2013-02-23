import serial
from pygame import mixer

mixer.init()
ping=mixer.Sound("ping.wav")
buzzer=mixer.Sound("buzzer.wav")

def matchCow(cow):
	f = open('cattle.txt')
	for line in f.readlines():
		line = line.strip()
		if cow == line:
			f.close()
			return True
	f.close()
	return False

def countList():
	with open('cattle.txt') as f:
		for i, l in enumerate(f):
			pass
	return str(i + 1)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)
while ser:
	line = ser.readline().decode('ascii').strip()
	if line != '':
		if matchCow(line) == False:
			f = open('cattle.txt','a')
			f.write(line + "\n")
			f.close()
			print(line + ' added to file')
			ping.play()
		else:
			buzzer.play()
		print(countList() + " cattle on list\n")
ser.close()