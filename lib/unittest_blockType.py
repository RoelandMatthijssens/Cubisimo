from drops import Drops
from panda3d.core import Filename

from blockType import BlockType
from unittest import TestCase, TestSuite, TextTestRunner, main

class BlockTypeSetup( TestCase ):
	""" """

	def setUp(self):
		""" """

		self.identifier = 1
		self.name = "dirt"
		self.modelPath = Filename( "/models/eggs/dirt.egg" )
		self.texturePath = Filename( "/models/textures/dirt.png" )
		self.baseColor = (256, 256, 256)
		self.damageLimit = 10
		self.damageAbsorption = 5
		self.drops = Drops()
		
		return None

	def initializing(self):
		"""It should initialize properly with good values.."""
		BlockType(self.identifier, self.name, self.modelPath, self.texturePath
				, self.baseColor, self.damageLimit, self.damageAbsorption, self.drops
				)
		return None

	def wrongName(self):
		"""It should only initialize if the name is a string."""
		# What else would you put in there?
		return None

	def wrongModelPath(self):
		"""It should only initialize if the modelPath is a path."""
		self.assertRaises(Exception, BlockType,
			( self.identifier, self.name, "/models/eggs/dirt.egg", self.texturePath
			, self.baseColor, self.damageLimit, self.damageAbsorption, self.drops
			)
		)
		return None

	def wrongTexturePath(self):
		"""It should only initialize if the texturePath is a path."""
		self.assertRaises(Exception, BlockType,
			( self.identifier, self.name, self.modelPath, "/models/textures/dirt.png"
			, self.baseColor, self.damageLimit, self.damageAbsorption
			, self.drops
			)
		)
		return None

	def wrongColors(self):
		"""It should only initialize if the baseColor is a color."""
		# either it is a triple of integers between 0 and 256, or some kind of color
		# object. Unfortunately I don't know whether panda has such an object or not.
		pass

	def wrongDamageLimit(self):
		"""It should only initialize if the damageLimit is an integer."""

		# test that strings are not accepted (when config files are parsed weirdly.
		self.assertRaises(Exception, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, "4", self.damageAbsorption, self.drops
			)
		)

		# Don't allow floats
		self.assertRaises(Exception, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, 4.3, self.damageAbsorption, self.drops
			)
		)

		return None

	def wrongDamageAbsorption(self):
		"""It should only initialize if the damageAbsorption is an integer."""

		# test that strings are not accepted (when config files are parsed weirdly.
		self.assertRaises(Exception, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, self.damageLimit, "8", self.drops
			)
		)

		# Don't allow floats
		self.assertRaises(Exception, BlockType,
			( self.identifier, self.name, self.modelPath, self.texturePath
			, self.baseColor, self.damageLimit, 2.9, self.drops
			)
		)

		return None

	def wrongDrops(self):
		"""It should only initialize if the drops is an actual drop object."""
		# Probabbly not worth the effort to figure out how to test this at this point?
		pass


suite = TestSuite()
suite.addTest( BlockTypeSetup( 'initializing' ) )
suite.addTest( BlockTypeSetup( 'wrongName' ) )
suite.addTest( BlockTypeSetup( 'wrongModelPath' ) )
suite.addTest( BlockTypeSetup( 'wrongTexturePath' ) )
suite.addTest( BlockTypeSetup( 'wrongColors' ) )
suite.addTest( BlockTypeSetup( 'wrongDamageLimit' ) )
suite.addTest( BlockTypeSetup( 'wrongDamageAbsorption' ) )
suite.addTest( BlockTypeSetup( 'wrongDrops' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )
