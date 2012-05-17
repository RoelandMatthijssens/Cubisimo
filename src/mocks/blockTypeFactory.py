""" """

from lib.blockTypeFactory import BlockTypeFactory

from mocks.config import ConfigMock

class BlockTypeFactoryMock( BlockTypeFactory ):
	''' '''

	def __init__(self, objectsConfig=None, idsConfig=None):
		''' '''
		objectsConfig = objectsConfig or self.createObjectConf()
		idsConfig = idsConfig or self.createIdsConf()
		super( BlockTypeFactoryMock, self ).__init__(objectsConfig, idsConfig)
		return None

	def createObjectConf( self ):
		''' '''
		return ConfigMock( '#comment'
				, '[air]'
				, 'name=air'
				, 'modelPath=path:models/eggs/air.egg'
				, 'texturePath=path:models/textures/air.png'
				, 'baseColor=(0, 0, 256)'
				, 'damageLimit=1'
				, 'damageAbsorption=0'
				, 'destructable=False'
				, 'transparent=False'
				, '[dirt]'
				, 'name=dirt'
				, 'modelPath=path:models/eggs/dirt.egg'
				, 'texturePath=path:models/textures/dirt.png'
				, 'baseColor=(0, 0, 256)'
				, 'damageLimit=50'
				, 'damageAbsorption=0'
				, '[stone]'
				, 'name=stone'
				, 'modelPath=path:models/eggs/stone.egg'
				, 'texturePath=path:models/textures/stone.png'
				, 'baseColor=(0, 256, 0)'
				, 'damageLimit=120'
				, 'damageAbsorption=5'
				)

	def createIdsConf( self ):
		''' '''
		return ConfigMock( '# the id\'s of the blocks above.'
				, '[ids]'
				, 'air=0'
				, 'dirt = 1'
				, 'stone=2'
				)

