""" """

from lib.encoder import Encoder
from lib.block import Block
from factories.blockTypeFactory import BlockTypeFactorySetup
from factories.playerFactory import PlayerFactorySetup
from factories.config import ConfigSetup

from pandac.PandaModules import Vec3

from unittest import TestCase, TestSuite, TextTestRunner

class Initializing( TestCase ):
	''' '''

	def it_should_initialize(self):
		''' '''
		playerFactory = PlayerFactorySetup.create()
		blockTypeFactory = BlockTypeFactorySetup.create()
		self.assertIsInstance( Encoder( playerFactory, blockTypeFactory ), Encoder )
		return None


class EncoderTest( TestCase ):
	""" """

	def setUp(self):
		""" """
		self.playerFactory = PlayerFactorySetup.create()
		self.blockTypeFactory = BlockTypeFactorySetup.create()
		self.encoder = Encoder( self.playerFactory, self.blockTypeFactory )
		return None

	def size(self):
		""" """
		# there is only one block so the block id fits in one byte, same for the player
		# id, then an additional byte for the damage and an additional byte for the seed,
		# giving a total of 4
		self.assertEqual( self.encoder.size(), 4 )
		return None

	def intToBytesConversion(self):
		""" """
		self.assertEqual( self.encoder.intToByteList( 256 ), [1, 0] )
		self.assertEqual( self.encoder.intToByteList( 512 ), [2, 0] )
		self.assertEqual( self.encoder.intToByteList( 110 ), [ 110 ] )
		return None

	def bytesToIntConversion(self):
		""" """
		self.assertEqual( self.encoder.byteListToInt([1, 1]), 257 )
		self.assertEqual( self.encoder.byteListToInt([110]), 110 )
		return 

	def encoding(self):
		""" """
		player = self.playerFactory.fromName( 'Jhon' )
		dirt = self.blockTypeFactory.fromName( 'dirt' )
		block = dirt.newBlock( player )
		block.seed = 110

		self.assertIsInstance( self.encoder.encodeBlock(block), str )
		self.assertEqual( self.encoder.encodeBlock( block ), "\x01\x01\x00n" )
		return None

	def decoding(self):
		""" """
		pos = Vec3( 0, 0, 0 )
		self.assertIsInstance( self.encoder.decodeBlock( "\x01\x01\x00n", pos ), Block )
		self.assertEqual( self.encoder.decodeBlock( "\x01\x01\x00n", pos ).blockType
				, self.blockTypeFactory.fromName( 'dirt' )
				)
		return None

suite = TestSuite()
suite.addTest( Initializing( "it_should_initialize" ) )

suite.addTest( EncoderTest( "size" ) )
suite.addTest( EncoderTest( "intToBytesConversion" ) )
suite.addTest( EncoderTest( "bytesToIntConversion" ) )
suite.addTest( EncoderTest( "encoding" ) )
suite.addTest( EncoderTest( "decoding" ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
