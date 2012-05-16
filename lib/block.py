""" """

class Block( object ):

	def __init__(self, blockType, position, damage, owner, seed, baseColor ):
		""" """

		from blockType import BlockType
		from player import Player
		from pandac.PandaModules import Vec3

		if not isinstance( blockType, BlockType ): raise TypeError( blockType )
		if not isinstance( owner, Player ): raise TypeError( owner )
		if not isinstance( position, Vec3 ): raise TypeError( position )
		if not isinstance( damage, int ): raise TypeError( damage )
		if not isinstance( seed, int ): raise TypeError( seed )
		if not isinstance( baseColor, tuple ): raise TypeError( baseColor )

		super(Block, self).__init__()

		self.identifier = blockType.identifier
		self.blockType = blockType
		self.position = position
		self.damage = damage
		self.owner = owner
		self.seed = seed
		self.baseColor = baseColor

		return None

	def damage(self, amount):
		""" """
		# Abuse the fact that int rounds down?
		self.damage += int( amount / self.blockType.rate )
		if self.damage > self.blockType.durability: return self.destroy()
		else: return self.damage

	def create(self, loader, environment):
		"""Add the block to the world. Do the actual construction of the model when
		necessary and add it to the environment (should actually be a chunk)."""

		cubeFile = self.blockType.modelPath
		self.cube = loader.loadModel( cubeFile )
		self.cube.setPos( self.position )
		self.cube.setColor( * self.baseColor )
		self.cube.reparentTo( render )

		print( 'loaded cube' )

		return self

	def destroy(self):
		"""See what items should be dropped, remove the block from the world, and handle
		everything else that should happens when a block breaks."""
		raise NotImplemented
