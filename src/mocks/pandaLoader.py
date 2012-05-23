''' '''

from pandac.PandaModules import NodePath

class PandaLoader( object ):
	''' '''

	def __init__(self):
		''' '''
		super( PandaLoader, self ).__init__()
		return None

	def loadModel(self, filename): return NodePath(str(filename))
