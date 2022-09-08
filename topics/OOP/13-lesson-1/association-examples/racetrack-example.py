
from time import time


class TrackSection():
	def __init__(self, name: str) -> None:
		self.name = name
	
	def __str__(self) -> str:
		return self.name

class RaceTrack():
	def __init__(self, trackSectionNames: list=None) -> None:
		self.trackSections = [TrackSection(name) for name in trackSectionNames] if trackSectionNames is not None else []
	
	def addTrackSection(self, trackSectionName: str):
		self.tractSections.append(TrackSection(trackSectionName))
	
	def nuke(self):
		print('Dropping environmentally friendly semi-nuclear bomb (reusable variant) in 3, 2, 1...')
		time.sleep(3)
		print('It malfunctioned.')
	
	def __str__(self) -> str:
		return f'Race track that takes this route: {" then a ".join([str(TrackPiece) for TrackPiece in self.trackSections ])}'

aTinyRaceTrack = RaceTrack(['moderately sized start', 'tiny curve', 'straight line', 'loop de loop', 'big finish'])

aTinyRaceTrack.addTrackSection('small jump')

print(aTinyRaceTrack)

del aTinyRaceTrack

