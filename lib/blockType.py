""" """

from panda3d.core import Filename
from pandac.PandaModules import Vec3
from block import Block

class BlockType( object ):
	"""Basically just a container to keep all information relevant to all blocks with this
	type."""

	def __init__(self, identifier, name, modelPath, texturePath, baseColor
			, damageLimit, damageAbsorption, drops):
		""" """

		if not type( identifier ) == int: raise Exception
		if not type( modelPath ) == Filename: raise Exception
		if not type( texturePath ) == Filename: raise Exception
		if not type( name ) == str: raise Exception
		if not type( damageLimit ) == int: raise Exception
		if not type( damageAbsorption) == int: raise Exception

		super( BlockType, self ).__init__()

		self.identifier = identifier
		self.name = name

		self.modelPath = modelPath 
		self.texturePath = texturePath
		self.baseColor = baseColor

		self.damageLimit = damageLimit
		self.damageAbsorption = damageAbsorption

		self.drops = drops
		return None

	def newSeed(self): return 0

	def newBlock(self, owner):
		""" """
		position = Vec3(0, 0, 0)
		block = Block(blockType=self, position=position, damage=0
				, owner=owner, seed=self.newSeed()
				, baseColor=self.baseColor
				)
		return block

