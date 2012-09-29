from OpenGL.GL import *
from OpenGL.GLUT import *
import gltools

class Context(gltools.BaseContext):
	def Init(self):
		print 'hello?'
		glutKeyboardFunc(self.OnKey)
		glutKeyboardUpFunc(self.OnKeyUp)

	def OnKeyUp(self, key, x, y):
		print 'keyup',ord(key)

	def OnKey(self, key, x, y):
		print 'keydown',ord(key)
		if key == chr(27):
			self.Exit()

	def Render(self):
		glClearColor(255,0,0,255)
		glClear(GL_COLOR_BUFFER_BIT);

		glutSwapBuffers()

gltools.RunContext(Context())
