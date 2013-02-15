import winsound, serial

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

ser = serial.Serial(1, 9600, timeout=0.1)
while ser:
	line = ser.readline().decode('ascii').strip()
	if line != '':
		if matchCow(line) == False:
			f = open('cattle.txt','a')
			f.write(line + "\n")
			f.close()
			print(line + ' added to file')
			winsound.PlaySound("ping.wav",winsound.SND_FILENAME)
		else:
			winsound.PlaySound("buzzer.wav",winsound.SND_FILENAME)
		print(countList() + " cattle on list\n")
ser.close()

