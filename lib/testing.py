from fileObject import FileObject
from panda3d.core import Filename

f = FileObject( Filename( 'testing.txt') )
del f
f = None

print( f )

exit()
