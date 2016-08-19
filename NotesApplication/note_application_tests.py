import unittest
from note_application import NotesApplication

class NotesApplicationTests(unittest.TestCase):
	# def test_instance_class(self):
	# 	s1 = NotesApplication('kevin Chiteri')
	# 	self.assertIsInstance(s1, NotesApplication, msg = " ")
	def test_getNoteNo(self):
		a1 = NotesApplication('Kevin')
		a1.create('Note 1') 
		a1.create('Note 2') 
		self.assertEqual('Note 2', a1.get(1), msg = (Wrong ))


if __name__ == '__main__':
	unittest.main()