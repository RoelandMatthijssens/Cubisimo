""" """

from lib.chunkGenerator import ChunkGenerator
from lib.encoder import Encoder
from lib.blockTypeFactory import BlockTypeFactory
from lib.playerFactory import PlayerFactory

from mocks.config import ConfigMock

from unittest import TestCase, TestSuite, TextTestRunner

class ChunkGeneratorSetup( TestCase ):
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

		self.encoder = Encoder( self.playerFactory, self.btf )
		return None

	def initializing(self):
		""" """
		self.assertIsInstance(
				ChunkGenerator( self.encoder, self.playerFactory, self.btf, 32 )
				, ChunkGenerator
		)
		return None


class ChunkGeneration( ChunkGeneratorSetup ):
	""" """

	def setUp(self):
		""" """
		ChunkGeneratorSetup.setUp( self )
		self.generator = ChunkGenerator( self.encoder, self.playerFactory, self.btf, 32 )
		return None

	def generation(self):
		""" """
		pass

suite = TestSuite()

suite.addTest( ChunkGeneratorSetup( "initializing" ) )

suite.addTest( ChunkGeneration( "generation" ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
