import pygame
import pygame.midi
import time
from enum import Enum

class MIDIPlayer:
	
	class Notes(Enum):
		sixteenth=.0625
		eighth=.125
		quarter=.25
		half=.5
		whole=1


	def __init__(self, port, instrument):
		pygame.midi.init()
		
		print "using port %s" %port
		self.player=pygame.midi.Output(port,0)
		#piano
		print "using instrument %s" %instrument
		self.player.set_instrument(instrument,port)

	def playNote(self, note, duration):
		self.player.note_on(note,127)
		time.sleep(duration)
		self.player.note_off(note,127)

if __name__ == '__main__':
	musicPlyr = MIDIPlayer(0, 0)
	notes=MIDIPlayer.Notes
	fur=[(76,notes.quarter),(75,notes.quarter),(76,notes.quarter),(75,notes.quarter),(76,notes.quarter),(71,notes.quarter),(74,notes.quarter),(72,notes.quarter),(69,notes.whole)]
	for x in fur:
		musicPlyr.playNote(x[0],x[1].value)
	del musicPlyr
	pygame.midi.quit()