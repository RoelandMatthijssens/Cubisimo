""" """

from lib.chunk import Chunk
from mocks.fileObject import FileObjectMock
from factories.playerFactory import PlayerFactorySetup
from factories.blockTypeFactory import BlockTypeFactorySetup
from factories.encoder import EncoderSetup
from factories.chunkGenerator import ChunkGeneratorSetup
from factories.chunk import ChunkSetup
from factories.chunkFile import ChunkFileSetup

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


class Generating( TestCase ):
	''' '''

	def setUp(self):
		''' '''
		self.chunkSize = 16
		self.playerFactory = PlayerFactorySetup.create()
		self.blockTypeFactory = BlockTypeFactorySetup.create()

		self.encoder = EncoderSetup.create( blockTypeFactory = self.blockTypeFactory
				, playerFactory = self.playerFactory
				)
		self.generator = ChunkGeneratorSetup.create( chunkSize = self.chunkSize
				, playerFactory = self.playerFactory
				, blockTypeFactory = self.blockTypeFactory
				)
		self.position = Vec3( 0, 0, 0 )
		self.fileObj = FileObjectMock()

		self.chunk = ChunkSetup.create( fileObj = self.fileObj, encoder = self.encoder
				, generator = self.generator, chunkSize = self.chunkSize
				, position = self.position
				)
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


class FilePositions( Generating ):
	''' '''

	def it_should_calculate_the_file_index_of_blocks(self):
		''' '''
		blockSize = self.encoder.size()
		chunkSize = self.chunkSize

		pos = Vec3( 0, 0, 0 )
		# first block in the file, so at position 0
		self.assertEqual( self.chunk.getIdx( pos ), 0 )

		pos = Vec3( 1, 0, 0 )
		# second block in the file, so skip blockSize positions (start counting from 0)
		self.assertEqual( self.chunk.getIdx( pos ), blockSize)

		pos = Vec3( 2, 0, 0 )
		# skip two blockSize positions
		self.assertEqual( self.chunk.getIdx( pos ), 2 * blockSize )

		pos = Vec3( 0, 1, 0 )
		# for every x index there is a block before this one. So chunkSize amount of
		# blocks.
		self.assertEqual( self.chunk.getIdx( pos ), blockSize * chunkSize )

		pos = Vec3( 0, 2, 0 )
		self.assertEqual( self.chunk.getIdx( pos ), 2 * blockSize * chunkSize )

		pos = Vec3( 0, 0, 1 )
		# for every x, y combination there is a block before this one. So chunkSize ** 2
		# amount of blocks.
		self.assertEqual( self.chunk.getIdx( pos ), blockSize * chunkSize ** 2 )

		pos = Vec3( 0, 0, 2 )
		self.assertEqual( self.chunk.getIdx( pos ), 2 * blockSize * chunkSize ** 2 )

		return None


class BlockPlacing( TestCase ):
	''' '''

	def setUp(self):
		''' '''

		self.chunkSize = 4
		self.playerFactory = PlayerFactorySetup.create()
		self.blockTypeFactory = BlockTypeFactorySetup.create()

		self.encoder = EncoderSetup.create( blockTypeFactory = self.blockTypeFactory
				, playerFactory = self.playerFactory
				)
		self.generator = ChunkGeneratorSetup.create( chunkSize = self.chunkSize
				, playerFactory = self.playerFactory
				, blockTypeFactory = self.blockTypeFactory
				)
		self.position = Vec3( 0, 0, 0 )
		self.fileObj = ChunkFileSetup.create()

		self.chunk = ChunkSetup.create( fileObj = self.fileObj, encoder = self.encoder
				, generator = self.generator, chunkSize = self.chunkSize
				, position = self.position
				)

		node = NodePath()
		self.chunk.load( node )

		world = self.playerFactory.fromName( '__WORLD__' )
		dirtType = self.blockTypeFactory.fromName( 'dirt' )
		self.dirt = dirtType.newBlock( world )

		return None

	def it_should_replace_blocks(self):
		''' '''

		position = Vec3( 4, 4, 4 )
		self.assertIsNone( self.chunk.place( self.dirt, position ) )

		blockSize = self.encoder.size()
		dirtIdx = self.chunk.getIdx( position )
		self.fileObj.open()
		self.fileObj.seek( dirtIdx )
		block = self.encoder.decodeBlock( self.fileObj.read( blockSize ), position )

		dirtType = self.blockTypeFactory.fromName( 'dirt' )
		self.assertEqual( block.blockType, dirtType )

		self.fileObj.close() 

		return None

	def it_should_not_alter_the_file_length_after_placing_a_block(self):
		''' '''

		self.fileObj.open()
		self.fileObj.seek(0)
		fileLength = len( self.fileObj.read() )
		self.fileObj.close()

		position = Vec3( 4, 4, 4 )
		self.assertIsNone( self.chunk.place( self.dirt, position ) )

		self.fileObj.open()
		self.fileObj.seek(0)
		self.assertEqual( len(self.fileObj.read()), fileLength )
		self.fileObj.close()

		return None


suite = TestSuite()

suite.addTest( Initialize( 'it_should_initialise' ) )
suite.addTest( Generating( 'it_should_create_a_chunk' ) )
suite.addTest( FilePositions( 'it_should_calculate_the_file_index_of_blocks' ) )
suite.addTest( BlockPlacing( 'it_should_replace_blocks' ) )
suite.addTest( BlockPlacing( 'it_should_not_alter_the_file_length_after_placing_a_block' ) )



if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
