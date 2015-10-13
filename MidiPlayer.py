import pygame
import pygame.midi
import time
from MusicTheory import Notes

class MIDIPlayer:
	
	def __init__(self, device_id, instrument, tempo=60):
		pygame.midi.init()
		
		print "using device id %s" %device_id
		self.player=pygame.midi.Output(device_id)
		#piano
		self.player.tempo=60.0/tempo
		print "using instrument %s" %instrument
		self.player.set_instrument(instrument,device_id)
	# note less than means rest
	def playNote(self, note, duration, loudness=127):
		if note >= 21:
			self.player.note_on(note,loudness)
			time.sleep(self.player.tempo*duration)
			self.player.note_off(note,loudness)
		else:
			time.sleep(duration)

	def playChord(self, notes, duration, loudness=127):
		if notes >= 21:
			for n in notes:
				if(n>=21):
					self.player.note_on(n,loudness)
			time.sleep(self.player.tempo*duration)
			for n in notes:
				if(n>=21):
					self.player.note_off(n,loudness)
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