""" """

from blockInterface import BlockIF

from panda3d.core import Filename
from pandac.PandaModules import Vec3

class BlockType( object ):
	"""Basically just a container to keep all information relevant to all blocks with this
	type."""

	def __init__(self, identifier, blockClass, name, modelPath, texturePath, baseColor
			, damageLimit, damageAbsorption, drops):
		""" """

		if not isinstance( identifier, int ): raise TypeError( identifier )
		if not issubclass( blockClass, BlockIF ): raise TypeError( blockClass )
		if not isinstance( modelPath, Filename ): raise TypeError( modelPath )
		if not isinstance( texturePath, Filename ): raise TypeError( texturePath )
		if not isinstance( name, str ): raise TypeError( name )
		if not isinstance( damageLimit, int ): raise TypeError( damageLimit )
		if not isinstance( damageAbsorption, int ): raise TypeError( damageAbsorption )

		super( BlockType, self ).__init__()

		self.identifier = identifier
		self.blockClass = blockClass
		self.name = name

		self.modelPath = modelPath 
		self.texturePath = texturePath
		self.baseColor = baseColor

		self.damageLimit = damageLimit
		self.damageAbsorption = damageAbsorption

		self.drops = drops
		return None

	def getModel(self): return self.cube

	def loadModel(self, loader):
		""" """

		red = self.baseColor[0] / 255.0
		green = self.baseColor[1] / 255.0
		blue = self.baseColor[2] / 255.0

		self.cube = loader.loadModel( self.modelPath )
		self.cube.setPos( 0, 0, 0 )
		self.cube.setColor( red, green, blue )

		return None

	def newSeed(self): return 0

	def newBlock(self, owner, position=None, damage=None, seed=None):
		""" """

		position = position or Vec3(0, 0, 0)
		damage = damage or 0
		seed = seed or self.newSeed()

		block = self.blockClass(blockType=self, position=position, damage=damage
				, owner=owner, seed=seed
				)
		return block

