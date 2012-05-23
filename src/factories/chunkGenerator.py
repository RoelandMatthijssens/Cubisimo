''' '''

from lib.chunkGenerator import ChunkGenerator
from factories.playerFactory import PlayerFactorySetup
from factories.blockTypeFactory import BlockTypeFactorySetup
from factories.encoder import EncoderSetup
from factories.setup import Setup

class ChunkGeneratorSetup( Setup ):
	''' '''

	playerFactory = PlayerFactorySetup.create()
	blockTypeFactory = BlockTypeFactorySetup.create()
	encoder = EncoderSetup.create( playerFactory, blockTypeFactory )
	chunkSize = 16

	@classmethod
	def create(cls, encoder=None, playerFactory=None, blockTypeFactory=None
			, chunkSize=None
			):
		''' '''

		encoder = encoder or cls.encoder
		playerFactory = playerFactory or cls.playerFactory
		blockTypeFactory = blockTypeFactory or cls.blockTypeFactory
		chunkSize = chunkSize or cls.chunkSize

		return ChunkGenerator( encoder, playerFactory, blockTypeFactory, chunkSize )

	@classmethod
	def prepare(cls):
		''' '''
		return ( cls.encoder, cls.playerFactory, cls.blockTypeFactory, cls.chunkSize )
