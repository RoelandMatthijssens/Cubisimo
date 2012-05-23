""" """

from panda3d.core import Filename
from pandac.PandaModules import Vec3
from blockInterface import BlockIF

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
		self.cube = loader.loadModel( self.modelPath )
		self.cube.setPos( 0, 0, 0 )
		self.cube.setColor( * self.baseColor )
		return None

	def newSeed(self): return 0

	def newBlock(self, owner):
		""" """
		position = Vec3(0, 0, 0)
		block = self.blockClass(blockType=self, position=position, damage=0
				, owner=owner, seed=self.newSeed()
				)
		return block

