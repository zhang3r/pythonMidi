from MidiPlayer import MIDIPlayer
from MusicTheory import Cmajor
from MusicTheory import Notes
import pygame
import pygame.midi

class FibMelodyGen:

	def __init__(self, stop, start=0, key=Cmajor):
		self.key=key
		self.fib=self.__fib(start,stop)
		self.tempo=90


	def generate(self):
		notes = Notes
		mNotes=[]
		#mDuration=[]
		mBpm=self.tempo
		mloudness=127
		#1. use fib to generate melody
		#things we can change
		#1. duration
		#2. pitch (notes)
		#3. bpm
		#4. loudness
		 
		#notes using fib
		for x in self.fib:
			mNotes.append((self.key.scale.value[x&7],notes.quarter))

		#duration for notes

		return mNotes


	def __fib(self, start, stop):
		self.fib=[]
		first=0
		second=1
		for x in range(stop):
			self.fib.append(second)
			first,second=second,first+second
		return self.fib[start:stop]


if __name__ == '__main__':
	#8 note melody in c major
	fibMelodyGenerator = FibMelodyGen(48)
	fibMelody=fibMelodyGenerator.generate()
	musicPlyr = MIDIPlayer(0, 0,fibMelodyGenerator.tempo)
	map(lambda x: musicPlyr.playNote(x[0],x[1].value), fibMelody)
		
	del musicPlyr
	pygame.midi.quit()