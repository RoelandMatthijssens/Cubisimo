""" """

from lib.player import Player
from factories.setup import Setup

class PlayerSetup( Setup ):
	''' '''

	identifier = 1
	name = 'Smith'

	@classmethod
	def create(cls, identifier=None, name=None):
		''' '''
		identifier = identifier or cls.identifier
		name = name or cls.name
		return Player( identifier, name )

	@classmethod
	def prepare(cls):
		''' '''
		return ( cls.identifier, cls.name )

