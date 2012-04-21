from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import *
from direct.task import Task
from panda3d.core import WindowProperties

class World(ShowBase):
	""" """
	
	keyMap = {"left":0, "right":0, "back":0, "space":0}

	def __init__(self):
		ShowBase.__init__(self)
		self.hideMouse()
		self.renderEnvironment()
		self.addCharacter()
		self.addFloater()
		self.setupCamera()
		self.addMouseTracker()

	def renderEnvironment(self):
		""" puts in an underground to play on """
		self.environ = self.loader.loadModel("models/world")
		self.environ.reparentTo(self.render)
		self.environ.setPos(0, 0, 0)

	def addCharacter(self):
		""" adds a model to play with in the world """
		charStartPos = self.environ.find("**/start_point").getPos()
		print charStartPos
		self.char = Actor("models/ralph",
				{"run":"models/ralph-run",
				"walk":"models/ralph-walk"})
		self.char.reparentTo(self.render)
		self.char.setScale(.2)
		self.char.setPos(charStartPos)

	def addFloater(self):
		""" the camera will look at a point above the head of the caracter.
		This will look over the head, instead of at it, which will look better
		"""
		self.floater = NodePath(PandaNode("floater"))
		self.floater.reparentTo(self.render)
		self.floater.setPos(self.char.getPos())
		self.floater.setZ(self.char.getZ()+1.2)

	def setupCamera(self):
		""" Sets the camera to the correct posision, and angle (looking at the floater """
		base.camera.setPos(self.char.getX(), self.char.getY()+1.3, 0.8)
		base.disableMouse()
		base.camera.lookAt(self.floater)
	def mouseTrack(self, task): 
		"""Use mouse to control orientation 
		similar to a video game:""" 
		try: 
			# X is in relative coordinates ( distance from 0 ) 
			# Y is in absolute coordinates ( -1 to 1 ) 
			x=base.mouseWatcherNode.getMouseX() 
			y=base.mouseWatcherNode.getMouseY() 
			# Invert Y to invert pitch if desired 
			# Reset cursor position to the horizontal center (x=0) 
			#   but don't adjust the height (y value) 
			base.win.movePointer(0, base.win.getProperties().getXSize() / 2, base.win.getProperties().getYSize()/2 ) 
			# *** For debugging, print out results 
			self.moveCamera(x, y)	
			print base.camera.getHeading()
			return Task.cont 
		except: 
			return Task.cont 
	def moveCamera(self, mouseXDelta, mouseYDelta):
		hpr = base.camera.getHpr()
		heading = hpr[0]
		pitch = hpr[1]
		newHeading = (( (heading + (-mouseXDelta * 70)) + 180) %360) -180 
		newPitch = (( (pitch + (mouseYDelta * 70)) + 180) %360) -180 
		base.camera.setHpr(newHeading, newPitch, 0)

	def addMouseTracker(self):
		""" add the mousetracking task to the world """
		taskMgr.add(self.mouseTrack, 'mouseTracker')

	def hideMouse(self):
		""" hide the mouse pointer, we will add a crosshairs later. """
		props = WindowProperties()
		props.setCursorHidden(True) 
		base.win.requestProperties(props)

app = World()
app.run()

