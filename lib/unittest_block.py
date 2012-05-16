""" """

from block import Block
from blockType import BlockType
from player import Player
from drops import Drops
from panda3d.core import Filename
from pandac.PandaModules import Vec3
from unittest import TestCase, TestSuite, TextTestRunner, main

class BlockSetup( TestCase ):

	def setUp(self):
		""" """
		self.blockType = BlockType( 1, 'dirt', Filename( 'models/eggs/dirt.egg' )
				, Filename( 'models/texture/dirt.png' ), (256, 0, 0), 20, 0
				, Drops()
				)
		self.player = Player( 1, 'Jhon' )
		return None

	def initializing(self):
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

	def getPlayer(self):
		""" """
		self.assertIsInstance( self.player, Player )
		return None

	def getBlockType(self):
		""" """
		self.assertIsInstance( self.blockType, BlockType )
		return None

	def damage(self): pass
	def create(self): pass


suite = TestSuite()

suite.addTest( BlockSetup( 'initializing' ) )

suite.addTest( BlockTest( 'getPlayer' ) )
suite.addTest( BlockTest( 'getBlockType' ) )

suite.addTest( BlockSetup( 'initializing' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
