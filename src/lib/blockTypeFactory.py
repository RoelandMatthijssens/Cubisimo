""" """

from factory import Factory
from drops import Drops

from blockType import BlockType
from baseBlock import BaseBlock
from airBlock import AirBlock

blockClasses = { 'air': AirBlock }

class BlockTypeFactory( Factory ):
	''' '''

	def __init__(self, objectConfig, idConfig, loader):
		''' '''
		self.loader = loader
		super(BlockTypeFactory, self).__init__(objectConfig, idConfig)
		return None

	def createInstance(self, identifier, name, values):
		''' '''

		drops = Drops()
		blockClass = blockClasses.get( name, BaseBlock )

		blockType = BlockType( identifier, blockClass, name
				, values[ 'modelPath' ], values[ 'texturePath' ]
				, values[ 'baseColor' ], values[ 'damageLimit' ]
				, values[ 'damageAbsorption' ], drops
				)
		blockType.loadModel( self.loader )

		return blockType

