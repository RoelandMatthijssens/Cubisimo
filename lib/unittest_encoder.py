""" """

from encoder import Encoder
from block import Block
from blockTypeFactory import BlockTypeFactory
from playerFactory import PlayerFactory
from configMock import ConfigMock
from pandac.PandaModules import Vec3
from unittest import TestCase, TestSuite, TextTestRunner

class EncoderSetup( TestCase ):
	""" """

	def setUp(self):
		""" """
		self.blockTypeConfig = ConfigMock( "#comment"
				, '[dirt]'
				, 'name=dirt'
				, 'modelPath=path:models/eggs/dirt.egg'
				, 'texturePath=path:models/textures/dirt.png'
				, 'baseColor=(0, 0, 256)'
				, 'damageLimit=50'
				, 'damageAbsorption=0'
				)
		self.blockTypeIdConfig = ConfigMock( "[ids]", "dirt=1" )
		self.playerConfig = ConfigMock( "[Jhon]", "hp=100" )
		self.playerIdConfig = ConfigMock( "[ids]", "Jhon=1" )

		self.btf = BlockTypeFactory(self.blockTypeConfig, self.blockTypeIdConfig)
		self.playerFactory = PlayerFactory( self.playerConfig, self.playerIdConfig )
		self.btf.process()
		self.playerFactory.process()
		
		return None

	def initializing(self):
		""" """
		self.assertIsInstance( Encoder(self.playerFactory, self.btf ), Encoder )
		return None


class EncoderTest( EncoderSetup ):
	""" """

	def setUp(self):
		""" """
		EncoderSetup.setUp(self)
		self.encoder = Encoder( self.playerFactory, self.btf)
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
		dirt = self.btf.fromName( 'dirt' )
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
				, self.btf.fromName( 'dirt' )
				)
		return None

suite = TestSuite()
suite.addTest( EncoderSetup( "initializing" ) )

suite.addTest( EncoderTest( "size" ) )
suite.addTest( EncoderTest( "intToBytesConversion" ) )
suite.addTest( EncoderTest( "bytesToIntConversion" ) )
suite.addTest( EncoderTest( "encoding" ) )
suite.addTest( EncoderTest( "decoding" ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
