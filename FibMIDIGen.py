from MidiPlayer import MIDIPlayer
from MusicTheory import Cmajor
from MusicTheory import Notes
import pygame
import pygame.midi

class FibMelodyGen:

	def __init__(self, stop, start=0, key=Cmajor):
		self.key=key
		self.fib=self.__fib(start,stop)
		self.tempo=60


	def generateMelody(self):
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
		map(lambda x: mNotes.append((self.key.scale.value[x&7],1.0/(2<<(x&3)))),self.fib)

		#duration for notes

		return mNotes

	def generateHarmony(self):
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
		mNotes=[(self.key.chords.value[x&7],notes.half.value) if x % 2==0 else ((-1,),0) for x in self.fib]
		#map(lambda x: mNotes.append((self.key.scale.value[x&7],notes.half.value)),self.fib)

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
	fibMelody=fibMelodyGenerator.generateMelody()
	fibHarmony=fibMelodyGenerator.generateHarmony()
	# print fibHarmony
	melodyPlyr = MIDIPlayer(0, 0,fibMelodyGenerator.tempo)
	#harmonyPlyr = MIDIPlayer(port=2, instrument=0,tempo=fibMelodyGenerator.tempo)
	for x,y in zip(fibMelody, fibHarmony):
		
		melodyPlyr.playChord(y[0]+(x[0],),x[1])
		#melodyPlyr.playChord(y[0],y[1])
	
	del melodyPlyr
	#del harmonyPlyr
	pygame.midi.quit()