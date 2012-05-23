''' '''

from blockInterface import BlockIF
from blockType import BlockType
from player import Player

from pandac.PandaModules import Vec3

class BaseBlock( BlockIF ):
	''' '''

	def __init__(self, blockType, position, owner, damage, seed):
		''' '''

		if not isinstance( blockType, BlockType ): raise TypeError( blockType )
		if not isinstance( owner, Player ): raise TypeError( owner )
		if not isinstance( position, Vec3 ): raise TypeError( position )
		if not isinstance( damage, int ): raise TypeError( damage )
		if not isinstance( seed, int ): raise TypeError( seed )

		super(BaseBlock, self).__init__()

		self.identifier = blockType.identifier
		self.blockType = blockType
		self.position = position
		self.damage = damage
		self.owner = owner
		self.seed = seed

		return None

	def create( self, environment ): return self.load( environment )
	def load( self, environment ):
		''' '''

		self.cube = NodePath('cube')
		model = self.blockType.getModel()
		model.instanceTo( self.cube )
		self.cube.setPos( self.position )
		self.cube.reparentTo( environment )

		return self

	def unload( self ):
		''' '''
		self.cube.detachNode()
		return None

