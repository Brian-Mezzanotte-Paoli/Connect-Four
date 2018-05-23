import serial
from time import sleep

TIME_ELEV = 35 	#Tempo di pausa per un viaggio di ascensore
TIME_CHECK = 1 	#Tempo di attesa per normali servomotori
TIME_COMB = 7.5 #Tempo di attera per il pettine

class Commands:
	OPEN_DOOR_PLAYER = 7		#Apertura sportello giocatore
	CLOSE_DOOR_PLAYER = 17		#Chiusura sportello giocatore
	OPEN_DOORS_UP = [0,1,2,3,4,5,6]				#Apertura delle porte in alto
	CLOSE_DOORS_UP = [10,11,12,13,14,15,16]		#Chiusura delle porte in alto
	OPEN_DOORS_DOWN = [20,21,22,23,24,25,26]		#Apertura delle porte in basso
	CLOSE_DOORS_DOWN = [30,31,32,33,34,35,36]		#Chiusura delle porte in basso
	SWITCH_PLAYER = 27		#Gira l'uscita per le palline verso il giocatore (per quando cadono)
	SWITCH_ELEN = 37		#Gira l'uscita per le palline verso la ascensore (per quando cadono)
	ELEV_UP = 48 			#Fa salire la ascensore (comprende la raccolta della pallina)
	ELEV_DOWN = 47			#Fa scendere la ascensore (comprende il rilascio della pallina (che non dovrebbe esserci))
	OPEN_ELEV_DOOR_DOWN = 40 	#Apre lo sportello per la ascensore basso
	CLOSE_ELEV_DOOR_DOWN = 41 	#Chiude lo sportello per la ascensore basso
	OPEN_ELEV_DOOR_UP = 42		#Apre lo sportello per la ascensore alto (da la spinta alla pallina)
	CLOSE_ELEV_DOOR_UP = 43		#Chiude lo sportello per la ascensore alto
	OPEN_COMB = 28 		#Apre il pettine (per cominciare a scaricare le palline)
	CLOSE_COMB = 38		#Chiude il pettine (lascia sotto il pettine una sola palla per colonna)
	CONTROL = 99	#Ricevi il numero della colonna appena passa la prossima palla


class Machine:
    def __init__(self):
        self.USB = "/dev/ttyACM0"
        self.ser = serial.Serial(self.USB)
        self.ser.isOpen()

    def close():
        self.ser.close()

    def elev_up(self):
        "Raccoglie una palla dal 'serbatoio', la porta in cima e la scalcia"
        self.run(Commands.OPEN_ELEV_DOOR_DOWN)
        sleep(TIME_CHECK)
        self.run(Commands.CLOSE_ELEV_DOOR_DOWN)
        sleep(TIME_CHECK)
        self.run(Commands.ELEV_UP)
        sleep(TIME_ELEV)
        self.run(Commands.OPEN_ELEV_DOOR_UP)
        sleep(TIME_CHECK)
        self.run(Commands.CLOSE_ELEV_DOOR_UP)
        sleep(TIME_CHECK)

    def elev_down(self):
        "Porta in basso la ascensore"
        self.run(Commands.ELEV_DOWN)
        sleep(TIME_ELEV)

    def scroll_comb(self):
        "Apre e chiude il pettine"
        self.run(Commands.OPEN_COMB)
        sleep(TIME_COMB)
        self.run(Commands.CLOSE_COMB)
        sleep(TIME_COMB)

    def run(self,value):
        self.ser.write(str(value)+"\n")

    def play_elev_up(self,x):
    	self.run(Commands.OPEN_DOORS_UP[x])
    	self.elev_up()

    def play_elev_down(self,x):
    	self.run(Commands.CLOSE_DOORS_UP[x])
    	self.elev_down()

    def wait_player(self):
    	self.run(Commands.OPEN_DOOR_PLAYER)
    	self.ser.flushInput(); self.ser.flushOutput()
    	sleep(1)
        self.run(Commands.CONTROL)
    	self.ser.flushInput(); self.ser.flushOutput()
    	while True:
            rest = self.ser.readline().strip()
            v = int(rest)-100
            if v in range(7): break
    	self.run(Commands.CLOSE_DOOR_PLAYER)
    	return v

    def switch(self,n):
    	if n: self.run(Commands.SWITCH_PLAYER)
    	else: self.run(Commands.SWITCH_ELEN)

    def open_ports_lists(self, liste):
    	for nLista in range(6):
    		self.open_ports_list(liste[5-nLista])

    def reset(self):
        self.run(Commands.CLOSE_DOOR_PLAYER)
        for p in range(1,7):
            self.run("1"+str(p))

    def open_ports_list(self,lista):
    	self.scroll_comb()		#Apre e chiude il pettine
    	self.switch(1)			#Gira l'uscita delle palline verso il giocatore
    	for pos in range(7):				#Lascia cadere le palline che devono finire dal giocatore
    		if lista[pos]==1:
    			self.run(OPEN_DOORS_DOWN[pos])

    	self.switch(0)			#Gira l'uscita delle palline verso la ascensore
    	for pos in range(7):				#Lascia cadere le palline che devono finire al ascensore
    		if lista[pos]==2:
    			self.run(OPEN_DOORS_DOWN[pos])

    	for pos in range(7):				#Chiude tutte le porte che sono state aperte
    		if lista[pos]!=0:
    			self.run(CLOSE_DOORS_DOWN[pos])
