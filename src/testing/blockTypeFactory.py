""" """

import os

from lib.blockTypeFactory import BlockTypeFactory
from lib.blockType import BlockType
from factories.blockTypeFactory import BlockTypeFactorySetup

from unittest import TestCase, TestSuite, TextTestRunner, main


class Initializing( TestCase ):
	''' '''

	def it_should_initialize(self):
		''' '''
		objectsConfig, idsConfig, loader = BlockTypeFactorySetup.prepare()

		self.assertIsInstance(
				BlockTypeFactory(objectsConfig, idsConfig, loader)
				, BlockTypeFactory
				)

		return None

	def it_should_process_its_config_files(self):
		''' '''
		blockTypeFactory = BlockTypeFactorySetup.create()
		self.assertIsNone( blockTypeFactory.process() )
		return None


class BasicTests( TestCase ):
	''' '''

	def setUp( self ):
		''' '''
		self.blockTypeFactory = BlockTypeFactorySetup.create()
		return None

	def it_should_figure_out_the_right_id_size(self):
		''' '''
		self.assertEqual( self.blockTypeFactory.idSize(), 1 )
		return None


class LookUps( BasicTests ):
	''' '''

	def it_should_look_up_blocks_by_name(self):
		''' '''
		self.assertIn( 'dirt', self.blockTypeFactory.objects.keys() )
		dirt = self.blockTypeFactory.fromName( 'dirt' )
		self.assertIsInstance( dirt, BlockType )
		self.assertEqual( dirt.name, 'dirt' )
		return None

	def it_should_look_up_blocks_by_id(self):
		''' '''
		self.assertIn( 1, self.blockTypeFactory.ids )
		dirt = self.blockTypeFactory.fromId( 1 )
		self.assertIsInstance( dirt, BlockType)
		self.assertEqual( dirt.name, 'dirt' )
		self.assertEqual( dirt, self.blockTypeFactory.fromName('dirt') )
		return None


suite = TestSuite()

suite.addTest( Initializing( 'it_should_initialize' ) )
suite.addTest( Initializing( 'it_should_process_its_config_files' ) )

suite.addTest( BasicTests( 'it_should_figure_out_the_right_id_size' ) )

suite.addTest( LookUps( 'it_should_look_up_blocks_by_name' ) )
suite.addTest( LookUps( 'it_should_look_up_blocks_by_id' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
