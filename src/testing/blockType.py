''' '''

from lib.blockType import BlockType
from factories.blockType import BlockTypeSetup

from panda3d.core import Filename

from unittest import TestCase, TestSuite, TextTestRunner, main


class Initializing( TestCase ):
	''' '''

	def it_should_initialize(self):
		'''It should initialize properly with good values.'''
		( identifier, name, modelPath, texturePath, baseColor, damageLimit
			, damageAbsorption, drops ) = BlockTypeSetup.prepare()

		self.assertIsInstance(
				BlockType(identifier, name, modelPath, texturePath, baseColor
						, damageLimit, damageAbsorption, drops
						)
				, BlockType
				)
		return None


class BlockTypeTest( TestCase ):
	''' '''

	def setUp(self):
		''' '''
		( self.identifier, self.name, self.modelPath, self.texturePath
				, self.baseColor, self.damageLimit, self.damageAbsorption
				, self.drops ) = BlockTypeSetup.prepare()
		return None

	def it_should_only_accept_filenames_for_modelPaths(self):
		'''It should only initialize if the modelPath is a path.'''
		self.assertRaises(TypeError, BlockType,
			( self.identifier, self.name, "/models/eggs/dirt.egg", self.texturePath
			, self.baseColor, self.damageLimit, self.damageAbsorption, self.drops
			)
		)
		return None

	def it_should_only_accept_filenames_for_texturePaths(self):
		'''It should only initialize if the texturePath is a path.'''
		self.assertRaises(TypeError, BlockType,
			( self.identifier, self.name, self.modelPath, "/models/textures/dirt.png"
			, self.baseColor, self.damageLimit, self.damageAbsorption
			, self.drops
			)
		)
		return None

	def it_should_only_accept_tuples_for_baseColor(self):
		'''It should only initialize if the baseColor is a color.'''
		# either it is a triple of integers between 0 and 256, or some kind of color
		# object. Unfortunately I don't know whether panda has such an object or not.
		pass

	def it_should_only_accept_integers_for_damageLimit(self):
		'''It should only initialize if the damageLimit is an integer.'''

		# test that strings are not accepted (when config files are parsed weirdly.
		self.assertRaises(TypeError, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, "4", self.damageAbsorption, self.drops
			)
		)

		# Don't allow floats
		self.assertRaises(TypeError, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, 4.3, self.damageAbsorption, self.drops
			)
		)

		return None

	def it_should_only_accept_integers_for_damageAbsorption(self):
		'''It should only initialize if the damageAbsorption is an integer.'''

		# test that strings are not accepted (when config files are parsed weirdly.
		self.assertRaises(TypeError, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, self.damageLimit, "8", self.drops
			)
		)

		# Don't allow floats
		self.assertRaises(TypeError, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, self.damageLimit, 2.9, self.drops
			)
		)

		return None

	def it_should_only_accept_intances_of_drops_for_drops(self):
		'''It should only initialize if the drops is an actual drop object.'''
		# Probabbly not worth the effort to figure out how to test this at this point?
		pass


suite = TestSuite()

suite.addTest( Initializing( 'it_should_initialize' ) )

suite.addTest( BlockTypeTest( 'it_should_only_accept_filenames_for_modelPaths' ) )
suite.addTest( BlockTypeTest( 'it_should_only_accept_filenames_for_texturePaths' ) )
suite.addTest( BlockTypeTest( 'it_should_only_accept_tuples_for_baseColor' ) )
suite.addTest( BlockTypeTest( 'it_should_only_accept_integers_for_damageLimit' ) )
suite.addTest( BlockTypeTest( 'it_should_only_accept_integers_for_damageAbsorption' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
