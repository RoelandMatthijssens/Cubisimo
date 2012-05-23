""" """

import sys
sys.path.append( 'src/' )

from panda3d.core import Filename
from pandac.PandaModules import Vec3, Loader

from lib.config import Config
from lib.world import World
from lib.scene import Scene
from lib.fileObject import FileObject
from lib.playerFactory import PlayerFactory
from lib.blockTypeFactory import BlockTypeFactory

if __name__ == '__main__':

	savePath = Filename( 'saveData/' )

	files = { 'main': Filename('config/settings.cfg') }
	configs = {}

	for s in ['players', 'playerIds', 'blockTypes', 'blockTypeIds']:
		files[ s ] = savePath + s + '.dat'

	for name, filename in files.items(): files[name] = FileObject( filename )
	for name, fileObj in files.items(): configs[ name ] = Config( fileObj )
	for config in configs.values(): config.process()

	scene = Scene()

	playerFactory = PlayerFactory( configs['players'], configs['playerIds'] )
	blockTypeFactory = BlockTypeFactory( configs['blockTypes']
			, configs['blockTypeIds'], scene.loader
			)

	playerFactory.process()
	blockTypeFactory.process()

	world = World( configs['main'], playerFactory, blockTypeFactory )
	world.setup()

	# assume we are at position (0, 0, 0)
	for chunk in world.getChunks( Vec3(0, 0, 0) ): chunk.load( scene.render )

	scene.run()
