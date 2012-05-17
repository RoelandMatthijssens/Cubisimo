""" """

from lib.encoder import Encoder
from lib.chunkGenerator import ChunkGenerator
from lib.chunk import Chunk
from mocks.fileObject import FileObjectMock
from mocks.playerFactory import PlayerFactoryMock
from mocks.blockTypeFactory import BlockTypeFactoryMock

from pandac.PandaModules import Vec3

from unittest import TestCase, TestSuite, TextTestRunner, main

class ChunkSetup( TestCase ):
	""" """

	def setUp(self):
		''' '''

		self.playerFactory = PlayerFactoryMock()
		self.blockTypeFactory = BlockTypeFactoryMock()
		self.chunkSize = 2

		self.encoder = Encoder( self.playerFactory, self.blockTypeFactory )
		self.generator = ChunkGenerator( self.encoder, self.playerFactory
				, self.blockTypeFactory, self.chunkSize
				)
		self.fileObj = FileObjectMock()
		self.position = Vec3( 0, 0, 0 )
		return None

	def it_should_initializing(self):
		''' '''
		self.assertIsInstance(
				Chunk( self.encoder, self.generator, self.fileObj,
						self.chunkSize, self.position
						)
				, Chunk
				)
		return None


suite = TestSuite()

suite.addTest( ChunkSetup( 'it_should_initializing' ) )


if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
