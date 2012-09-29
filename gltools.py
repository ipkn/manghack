from abc import abstractmethod
from OpenGL.GL import *
#from OpenGL.GL import shaders
from OpenGL.GLUT import *

class BaseContext(object):
	def _Init(self):
		try:
			self.Init()
		except Exception as e:
			print e
			self.Exit()
	@abstractmethod
	def Init(self):
		pass
	def _Render(self):
		try:
			self.Render()
		except Exception as e:
			print e
			self.Exit()
	@abstractmethod
	def Render(self):
		pass

	def Exit(self):
		if self.window:
			glutDestroyWindow(self.window)
		print 'bye'
		import sys
		sys.exit(-1)

def RunContext(context):
	assert isinstance(context, BaseContext)

	glutInit()
	glutInitWindowSize(600, 400)
	context.window = glutCreateWindow("Hello, World")
	glutDisplayFunc(context._Render)
	context._Init()
	glutMainLoop()
