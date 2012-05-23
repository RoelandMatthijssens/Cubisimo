""" """

from lib.block import Block

from factories.player import PlayerSetup
from factories.blockType import BlockTypeSetup
from factories.setup import Setup

from pandac.PandaModules import Vec3


class BlockSetup( Setup ):
	''' '''

	blockType = BlockTypeSetup.create()
	position = Vec3( 0, 0, 0 )
	owner = PlayerSetup.create()
	damage = 0
	seed = 0
	baseColor = (255, 255, 255)

	@classmethod
	def create(cls, blockType=None, position=None, owner=None, damage=None
			, seed=None, baseColor=None
			):
		''' '''
		blockType = blockType or cls.blockType
		position = position or cls.position
		owner = owner or cls.owner
		damage = damage or cls.damage
		seed = seed or cls.seed
		baseColor = baseColor or cls.baseColor

		return Block( blockType, position, owner, damage, seed, baseColor )

	@classmethod
	def prepare(cls):
		''' '''
		return ( cls.blockType, cls.position, cls.owner, cls.damage, cls.seed, cls.baseColor )
