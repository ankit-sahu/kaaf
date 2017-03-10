from unittest import TestCase

class BaseTest(TestCase):
	

	def __init__(self, *args, **kwargs):
		TestCase.__init__(self, *args, **kwargs)