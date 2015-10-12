import pygame
import pygame.midi
import time
from MusicTheory import Notes

class MIDIPlayer:
	
	def __init__(self, port, instrument, tempo=60):
		pygame.midi.init()
		
		print "using port %s" %port
		self.player=pygame.midi.Output(port,0)
		#piano
		self.player.tempo=60.0/tempo
		print "using instrument %s" %instrument
		self.player.set_instrument(instrument,port)
	# note less than means rest
	def playNote(self, note, duration, loudness=127):
		if note >= 21:
			self.player.note_on(note,loudness)
			time.sleep(self.player.tempo*duration)
			self.player.note_off(note,loudness)
		else:
			time.sleep(duration)

if __name__ == '__main__':
	musicPlyr = MIDIPlayer(0, 0,90)
	notes=Notes
	fur=[(76,notes.quarter),(75,notes.quarter),(76,notes.quarter),(75,notes.quarter),(76,notes.quarter),(71,notes.quarter),(74,notes.quarter),(72,notes.quarter),(69,notes.whole)]
	for x in fur:
		musicPlyr.playNote(x[0],x[1].value)
	del musicPlyr
	pygame.midi.quit()