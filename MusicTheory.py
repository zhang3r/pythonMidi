from enum import Enum

class Cmajor(Enum):
	sharps=[]
	scale=[60,62,64,65,67,69,71,72]
	chords=[(60,64,67),(62,65,69),(64,67,71),(65,69,72),(67,71,74),(69,72,76),(71,74,77),(72,76,79)]
	base=60

class Dmajor(Enum):
	sharps=[66,73 ]
	scale=[62,64,66,67,69,71,73,74]
	base=62
class Notes(Enum):
	sixtyforth=0.015625
	thirtysecondth=0.03125
	sixteenth=0.0625
	eighth=0.125
	quarter=0.25
	half=0.5
	whole=1

class Emajor(Enum):
	#TODO
	pass

class Fmajor(Enum):
	#TODO
	pass

class Gmajor(Enum):
	#TODO
	pass

class Amajor(Enum):
	#TODO
	pass

class Bmajor(Enum):
	#TODO
	pass


