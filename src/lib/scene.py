""" """

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.task import Task
from panda3d.core import WindowProperties
from panda3d.core import Filename

class Scene(ShowBase):
	""" """

	keyMap = {"left":0, "right":0, "back":0, "space":0}

	def __init__(self):
		""" """
		ShowBase.__init__(self)
		self.addCube()
		self.setupCamera()
		self.addMouseTracker()

		return None

	def setupCamera(self):
		"""Sets the camera to the correct posision, and angle (looking at the floater)."""
		base.camera.setPos(0, 0, 0)
		base.disableMouse()
		base.camera.lookAt(self.cuby)
		return None

	def mouseTrack(self, task): 
		"""Use mouse to control orientation similar to a video game:"""
		try:
			# X is in relative coordinates ( distance from 0 )
			# Y is in absolute coordinates ( -1 to 1 )
			x = base.mouseWatcherNode.getMouseX()
			y = base.mouseWatcherNode.getMouseY()
			# Invert Y to invert pitch if desired
			# Reset cursor position to the horizontal center (x=0)
			#   but don't adjust the height (y value)
			base.win.movePointer(0
				, base.win.getProperties().getXSize() / 2
				, base.win.getProperties().getYSize() / 2
				)
			# *** For debugging, print out results
			self.moveCamera(x, y)
			print base.camera.getHeading()
			return Task.cont
		except: return Task.cont 

	def moveCamera(self, mouseXDelta, mouseYDelta):
		hpr = base.camera.getHpr()
		heading = hpr[0]
		pitch = hpr[1]
		newHeading = (( (heading + (-mouseXDelta * 70)) + 180) % 360) -180
		newPitch = (( (pitch + (mouseYDelta * 70)) + 180) %360) -180
		base.camera.setHpr(newHeading, newPitch, 0)

	def addMouseTracker(self):
		""" add the mousetracking task to the world """
		taskMgr.add(self.mouseTrack, 'mouseTracker')

	def addCube(self):
		"""Add a cube in front of the characters just as a test."""

		cubyFile = Filename( "models/cube" )

		self.cuby = self.loader.loadModel( cubyFile )
		self.cuby.setPos( 5, 0, 0 )
		self.cuby.setColor(255, 0, 0)
		self.cuby.reparentTo(self.render)

		return None

	def hideMouse(self):
		"""Hide the mouse pointer, we will add a crosshairs later."""
		props = WindowProperties()
		props.setCursorHidden(True) 
		base.win.requestProperties(props)

