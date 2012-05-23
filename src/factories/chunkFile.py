''' '''

from mocks.fileObject import FileObjectMock
from factories.setup import Setup
from factories.blockTypeFactory import BlockTypeFactorySetup
from factories.playerFactory import PlayerFactorySetup
from factories.encoder import EncoderSetup



class ChunkFileSetup( Setup ):
	''' '''

	playerFactory = PlayerFactorySetup.create()
	blockTypeFactory = BlockTypeFactorySetup.create()
	chunkSize = 16

	@classmethod
	def create(cls, encoder=None, playerFactory=None, blockTypeFactory= None
			, chunkSize=None
			):
		''' '''

		playerFactory = playerFactory or cls.playerFactory
		blockTypeFactory = blockTypeFactory or cls.blockTypeFactory
		encoder = encoder or EncoderSetup.create( playerFactory, blockTypeFactory )
		chunkSize = chunkSize or cls.chunkSize

		world = playerFactory.fromName( '__WORLD__' )
		airType = blockTypeFactory.fromName( 'air' )
		air = airType.newBlock( owner = world )
		string = encoder.encodeBlock( air )
		string = string * (chunkSize ** 3)

		return FileObjectMock( string )

	@classmethod
	def prepare(cls): return ()
