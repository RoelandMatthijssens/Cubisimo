""" """

from lib.block import Block
from lib.blockType import BlockType
from lib.player import Player
from lib.drops import Drops

from panda3d.core import Filename
from pandac.PandaModules import Vec3

from unittest import TestCase, TestSuite, TextTestRunner, main

class BlockSetup( TestCase ):

	def setUp(self):
		""" """

		self.blockTypeId = 1
		self.name = 'dirt'
		self.modelPath = Filename('models/eggs/dirt.egg')
		self.texturePath = Filename('models/textures/dirt.png')
		self.baseColor = (255, 0, 0)
		self.damageLimit = 20
		self.damageReduction = 0
		self.drops = Drops()

		self.player = Player( 1, 'Jhon' )

		self.blockType = BlockType( self.blockTypeId, self.name, self.modelPath
				, self.texturePath, self.baseColor, self.damageLimit
				, self.damageReduction, self.drops
				)
		return None

	def it_should_initializing(self):
		""" """
		self.assertIsInstance(
				Block( self.blockType, Vec3( 0, 0, 0 ), 0, self.player
						, 110, self.blockType.baseColor
						)
				, Block
				)
		return None

class BlockTest( BlockSetup ):
	""" """

	def setUp(self):
		""" """
		BlockSetup.setUp( self )
		self.block = Block( self.blockType, Vec3( 0, 0, 0 ) , 0
				, self.player, 110, self.blockType.baseColor
				)
		return None

	def it_should_have_the_right_owner(self):
		""" """
		self.assertIsInstance( self.player, Player )
		return None

	def it_should_have_the_right_block_type(self):
		""" """
		self.assertIsInstance( self.blockType, BlockType )
		return None

	def damage(self): pass
	def create(self): pass


suite = TestSuite()

suite.addTest( BlockSetup( 'it_should_initializing' ) )

suite.addTest( BlockTest( 'it_should_have_the_right_owner' ) )
suite.addTest( BlockTest( 'it_should_have_the_right_block_type' ) )


if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
