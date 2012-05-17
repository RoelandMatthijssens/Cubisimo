""" """

from player import Player
from factory import Factory

class PlayerFactory( Factory ):
	""" """

	def createInstance(self, identifier, name, values):
		""" """

		player = Player( identifier, name )
		return player

