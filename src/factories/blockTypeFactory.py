""" """

from lib.blockTypeFactory import BlockTypeFactory
from factories.config import ConfigSetup
from mocks.pandaLoader import PandaLoader

class BlockTypeFactorySetup( object ):
	''' '''

	objectsText = [ '# some test config file.'
			, '[air]'
			, 'name=air'
			, 'modelPath=path:models/eggs/air.egg'
			, 'texturePath=path:models/textures/air.png'
			, 'baseColor=(255, 255, 255)'
			, 'damageLimit=50'
			, 'damageAbsorption=0'

			, '[dirt]'
			, 'name=dirt'
			, 'modelPath=path:models/eggs/dirt.egg'
			, 'texturePath=path:models/textures/dirt.png'
			, 'baseColor=(0, 0, 255)'
			, 'damageLimit=50'
			, 'damageAbsorption=0'

			, '[stone]'
			, 'name=stone'
			, 'modelPath=path:models/eggs/stone.egg'
			, 'texturePath=path:models/textures/stone.png'
			, 'baseColor=(0, 255, 0)'
			, 'damageLimit=120'
			, 'damageAbsorption=5'
			]
	idsText = [ '# the id\'s of the blocks above.'
			, '[ids]'
			, 'air=0'
			, 'dirt = 1'
			, 'stone=2'
			]

	@classmethod
	def create(cls, objectsConfig=None, idsConfig=None, loader=None):
		''' '''
		objectsConfig = objectsConfig or cls.createObjectsConfig()
		idsConfig = idsConfig or cls.createIdsConfig()
		loader = loader or PandaLoader()
		btf =  BlockTypeFactory( objectsConfig, idsConfig, loader )
		btf.process()
		return btf

	@classmethod
	def prepare( cls ): return cls.createObjectsConfig, cls.createIdsConfig, PandaLoader()

	@classmethod
	def createObjectsConfig( cls ): return ConfigSetup.create( * cls.objectsText )

	@classmethod
	def createIdsConfig( cls ): return ConfigSetup.create( * cls.idsText )

