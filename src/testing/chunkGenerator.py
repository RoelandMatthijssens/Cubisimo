""" """

from lib.chunkGenerator import ChunkGenerator
from mocks.fileObject import FileObjectMock
from factories.playerFactory import PlayerFactorySetup
from factories.blockTypeFactory import BlockTypeFactorySetup
from factories.encoder import EncoderSetup
from factories.chunkGenerator import ChunkGeneratorSetup

from pandac.PandaModules import Vec3

from unittest import TestCase, TestSuite, TextTestRunner


class Initialize( TestCase ):
	''' '''

	def it_should_initialize( self ):
		''' '''
		encoder, playerFactory, blockTypeFactory, chunkSize = ChunkGeneratorSetup.prepare()

		self.assertIsInstance(
				ChunkGenerator( encoder, playerFactory, blockTypeFactory, chunkSize )
				, ChunkGenerator
				)
		return None


class ChunkGeneratorTest( TestCase ):
	''' '''

	def setUp( self ):
		''' '''
		self.fileObj = FileObjectMock()
		self.position = Vec3( 0, 0, 0 )

		self.encoder = EncoderSetup.create()
		self.playerFactory = PlayerFactorySetup.create()
		self.blockTypeFactory = BlockTypeFactorySetup.create()
		self.chunkSize = 16

		self.generator = ChunkGeneratorSetup.create( encoder = self.encoder
				, playerFactory = self.playerFactory
				, blockTypeFactory = self.blockTypeFactory
				, chunkSize = self.chunkSize
				)
		return None

	def it_should_generate_properly( self ):
		''' '''
		self.assertIsNone( self.generator.generate(self.fileObj, self.position) )

		world = self.playerFactory.fromName( '__WORLD__' )
		air = self.blockTypeFactory.fromName( 'air' ).newBlock( world )
		string = self.encoder.encodeBlock( air ) * ( self.chunkSize ** 3 )

		self.fileObj.open()
		self.fileObj.seek( 0 )

		self.assertEqual( self.fileObj.read(), string )

		self.fileObj.close()
		return None


suite = TestSuite()

suite.addTest( Initialize( 'it_should_initialize' ) )

suite.addTest( ChunkGeneratorTest( 'it_should_generate_properly' ) )


if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
