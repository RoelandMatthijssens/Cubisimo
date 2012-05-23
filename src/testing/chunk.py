""" """

from lib.chunk import Chunk
from mocks.fileObject import FileObjectMock
from factories.playerFactory import PlayerFactorySetup
from factories.blockTypeFactory import BlockTypeFactorySetup
from factories.chunk import ChunkSetup

from pandac.PandaModules import Vec3
from pandac.PandaModules import NodePath

from unittest import TestCase, TestSuite, TextTestRunner, main

class Initialize( TestCase ):
	''' '''

	def it_should_initialise(self):
		''' '''
		encoder, generator, fileObj, chunkSize, position = ChunkSetup.prepare()
		self.assertIsInstance(
				Chunk( encoder, generator, fileObj, chunkSize, position)
				, Chunk
				)
		return None


class ChunkGenerationTest( TestCase ):
	''' '''

	def setUp(self):
		''' '''
		self.encoder, gen, self.fileObj, self.chunkSize, pos = ChunkSetup.prepare()
		self.chunk = ChunkSetup.create( fileObj = self.fileObj, encoder = self.encoder )
		return None

	def it_should_create_a_chunk(self):
		''' '''
		self.fileObj.setExists( False )
		node = NodePath()

		self.assertIsNone( self.chunk.load(node) )

		self.fileObj.open()
		self.fileObj.seek(0)
		blockLength = self.encoder.size()
		nrOfBlocks = self.chunkSize ** 3

		# check if something is wrinten to the file, and that it make some sence.
		self.assertEqual( len(self.fileObj.read()), blockLength * nrOfBlocks )

		self.fileObj.close() 
		return None


suite = TestSuite()

suite.addTest( Initialize( 'it_should_initialise' ) )

suite.addTest( ChunkGenerationTest( 'it_should_create_a_chunk' ) )


if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
