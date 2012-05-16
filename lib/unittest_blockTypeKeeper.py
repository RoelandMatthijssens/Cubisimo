""" """

from fileObjectMock import FileObjectMock
from config import Config
from blockTypeFactory import BlockTypeFactory
from blockType import BlockType
from unittest import TestCase, TestSuite, TextTestRunner, main


class BlockTypeFactorySetup( TestCase ):
	""" """

	def setUp(self):
		""" """
		self.blockText = [ '# some test config file.'
				, '[dirt]'
				, 'name=dirt'
				, 'modelPath=path:models/eggs/dirt.egg'
				, 'texturePath=path:models/textures/dirt.png'
				, 'baseColor=(0, 0, 256)'
				, 'damageLimit=50'
				, 'damageAbsorption=0'
				, '[stone]'
				, 'name=stone'
				, 'modelPath=path:models/eggs/stone.egg'
				, 'texturePath=path:models/textures/stone.png'
				, 'baseColor=(0, 256, 0)'
				, 'damageLimit=120'
				, 'damageAbsorption=5'
				]
		self.blockIdText = [ '# the id\'s of the blocks above.'
				, '[ids]'
				, '# air=0'
				, 'dirt = 1'
				, 'stone=2'
				]

		self.blockFile = FileObjectMock( '\n'.join( self.blockText ) )
		self.idFile = FileObjectMock( '\n'.join( self.blockIdText ) )
		self.blockConfig = Config( self.blockFile )
		self.idConfig = Config( self.idFile )
		self.blockConfig.process()
		self.idConfig.process()
		return None

	def initialize(self):
		""" """
		self.assertIsInstance( BlockTypeFactory( self.blockConfig, self.idConfig )
				, BlockTypeFactory
				, 'BlockTypeFactory did not initialize properly.' )
		return None

	def process(self):
		""" """
		self.btk = BlockTypeFactory( self.blockConfig, self.idConfig )
		self.assertIsNone( self.btk.process(), '' )
		return None


class BlockTypeFactoryTest( BlockTypeFactorySetup ):
	""" """

	def setUp( self ):
		""" """
		BlockTypeFactorySetup.setUp(self)
		self.btk = BlockTypeFactory( self.blockConfig, self.idConfig )
		self.btk.process()
		return None

	def idsize(self):
		""" """
		self.assertEqual( self.btk.idSize(), 1)
		return None


class BlockTypeFactoryLookUps( BlockTypeFactoryTest ):
	""" """

	def lookUpByName(self):
		""" """
		self.assertIn( 'dirt', self.btk.objects.keys()
				, 'BlockTypeFactory did not properly remember blockTypes.'
				)
		self.assertIsInstance( self.btk.fromName('dirt'), BlockType
				, 'BlockTypeFactory did not properly construct blockTypes.'
				)
		return None

	def lookUpById(self):
		self.assertIn( 1, self.btk.ids
				, 'BlockTypeFactory did not properly remember typeIds.'
				)
		self.assertIsInstance( self.btk.fromId( 1 ), BlockType
				, 'BlockTypeFactory did not bind id\'s to blockTypes.'
				)
		self.assertEqual( self.btk.fromId( 1 ), self.btk.fromName('dirt')
				, 'lookup by id and by name did not match.'
				)
		return None



suite = TestSuite()

suite.addTest( BlockTypeFactorySetup( 'initialize' ) )
suite.addTest( BlockTypeFactorySetup( 'process' ) )

suite.addTest( BlockTypeFactoryTest( 'idsize' ) )

suite.addTest( BlockTypeFactoryLookUps( 'lookUpByName' ) )
suite.addTest( BlockTypeFactoryLookUps( 'lookUpById' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
