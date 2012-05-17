""" """

from drops import Drops
from blockType import BlockType
from factory import Factory

class BlockTypeFactory( Factory ):
	""" """

	def createInstance(self, identifier, name, values):
		""" """

		drops = Drops()

		blockType = BlockType( identifier, name, values[ 'modelPath' ]
				, values[ 'texturePath' ], values[ 'baseColor' ]
				, values[ 'damageLimit' ], values[ 'damageAbsorption' ]
				, drops
				)

		return blockType

