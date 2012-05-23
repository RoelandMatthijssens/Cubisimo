""" """

from factories.setup import Setup
from factories.drops import DropsSetup

from lib.blockType import BlockType
from lib.baseBlock import BaseBlock

from panda3d.core import Filename

class BlockTypeSetup( Setup ):
	''' '''

	blockTypeId = 0
	name = 'air'
	modelPath = Filename('models/eggs/air.egg')
	texturePath = Filename('models/textures/air.png')
	baseColor = (255, 0, 0)
	damageLimit = 20
	damageReduction = 0
	drops = DropsSetup.create()
	blockClass = BaseBlock

	@classmethod
	def create(cls, blockTypeId=None, blockClass=None, name=None, modelPath=None
			, texturePath=None, baseColor=None, damageLimit=None
			, damageReduction=None, drops=None
			):
		''' '''

		blockTypeId = blockTypeId or cls.blockTypeId
		blockClass = blockClass or cls.blockClass
		name = name or cls.name
		modelPath = modelPath or cls.modelPath
		texturePath = texturePath or cls.texturePath
		baseColor = baseColor or cls.baseColor
		damageLimit = damageLimit or cls.damageLimit
		damageReduction = damageReduction or cls.damageReduction
		drops = drops or cls.drops

		return BlockType( blockTypeId, blockClass, name, modelPath, texturePath
				, baseColor , damageLimit, damageReduction, drops
				)

	@classmethod
	def prepare(cls): 
		''' '''
		return ( cls.blockTypeId, cls.blockClass, cls.name, cls.modelPath, cls.texturePath
				, cls.baseColor, cls.damageLimit, cls.damageReduction, cls.drops
				)
