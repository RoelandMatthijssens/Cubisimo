""" """

from lib.chunk import Chunk

from mocks.fileObject import FileObjectMock
from factories.setup import Setup
from factories.playerFactory import PlayerFactorySetup
from factories.blockTypeFactory import BlockTypeFactorySetup
from factories.encoder import EncoderSetup
from factories.chunkGenerator import ChunkGeneratorSetup

from pandac.PandaModules import Vec3

class ChunkSetup( Setup ):
	''' '''

	chunkSize = 16
	playerFactory = PlayerFactorySetup.create()
	blockTypeFactory = BlockTypeFactorySetup.create()

	encoder = EncoderSetup.create(playerFactory, blockTypeFactory)
	generator = ChunkGeneratorSetup.create(encoder, playerFactory
			, blockTypeFactory, chunkSize
			)
	fileObj = FileObjectMock()

	position = Vec3( 0, 0, 0 )

	@classmethod
	def create(cls, encoder=None, generator=None, fileObj=None, chunkSize=None
			, position=None):
		''' '''
		encoder = encoder or cls.encoder
		generator = generator or cls.generator
		fileObj = fileObj or cls.fileObj
		chunkSize = chunkSize or cls.chunkSize
		position = position or cls.position

		return Chunk( encoder, generator, fileObj, chunkSize, position )

	@classmethod
	def prepare(cls):
		''' '''
		return ( cls.encoder, cls.generator, cls.fileObj, cls.chunkSize, cls.position )
