""" """

from lib.block import Block
from lib.player import Player
from lib.blockType import BlockType
from factories.player import PlayerSetup
from factories.block import BlockSetup
from factories.blockType import BlockTypeSetup

from unittest import TestCase, TestSuite, TextTestRunner, main

class Initializing( TestCase ):

	def it_should_initializing(self):
		""" """
		blockType, position, owner, damage, seed, baseColor = BlockSetup.prepare()

		self.assertIsInstance(
				Block( blockType, position, owner, damage, seed, baseColor )
				, Block
				)
		return None

class BlockTest( TestCase ):
	""" """

	def setUp(self):
		""" """
		self.player = PlayerSetup.create()
		self.blockType = BlockTypeSetup.create()
		self.block = BlockSetup.create( owner = self.player, blockType = self.blockType )
		return None

	def it_should_have_the_right_owner(self):
		""" """
		self.assertIsInstance( self.block.owner, Player )
		self.assertEqual( self.block.owner, self.player )
		return None

	def it_should_have_the_right_block_type(self):
		""" """
		self.assertIsInstance( self.block.blockType, BlockType )
		self.assertEqual( self.block.blockType, self.blockType )
		return None

	def damage(self): pass
	def create(self): pass


suite = TestSuite()

suite.addTest( Initializing( 'it_should_initializing' ) )

suite.addTest( BlockTest( 'it_should_have_the_right_owner' ) )
suite.addTest( BlockTest( 'it_should_have_the_right_block_type' ) )


if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
