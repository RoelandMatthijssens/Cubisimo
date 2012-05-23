''' '''

from lib.drops import Drops
from factories.setup import Setup

class DropsSetup( Setup ):
	''' '''

	@classmethod
	def create(cls): return Drops()

	@classmethod
	def preprare(cls): return ()
