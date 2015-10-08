from MidiPlayer import MIDIPlayer
from MusicTheory import Cmajor
from MusicTheory import Notes

class FibMelodyGen:

	def __init__(self, stop, start=0, key=Cmajor):
		self.key=key
		self.fib=__fib(start,stop)


	def generate(self):
		notes = Notes
		#1. use fib to generate melody
		#2. notes
		return []


	def __fib(self, start, stop):
		self.fib=[]
		int first=0
		int second=1
		for x in range(stop):
			self.fib.append(second)
			first,second=second,first+second
		return self.fib[start:stop]