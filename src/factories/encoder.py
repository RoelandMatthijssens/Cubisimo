''' '''

from lib.encoder import Encoder
from factories.setup import Setup
from factories.playerFactory import PlayerFactorySetup
from factories.blockTypeFactory import BlockTypeFactorySetup

class EncoderSetup( Setup ):
	''' '''

	playerFactory = PlayerFactorySetup.create()
	blockTypeFactory = BlockTypeFactorySetup.create()

	@classmethod
	def create(cls, playerFactory=None, blockTypeFactory=None):
		''' '''
		playerFactory = playerFactory or cls.playerFactory
		blockTypeFactory = blockTypeFactory or cls.blockTypeFactory
		return Encoder( playerFactory, blockTypeFactory )

	@classmethod
	def prepare(cls):
		''' '''
		return ( cls.playerFactory, cls.blockTypeFactory )
