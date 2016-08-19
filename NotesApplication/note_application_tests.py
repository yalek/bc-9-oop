import unittest
from note_application import NotesApplication

class NotesApplicationTests(unittest.TestCase):
	
	def test_author_empty(self):
		self.assertRaises(TypeError, NotesApplication)

	def test_author_is_number(self):
		self.assertRaises(TypeError, NotesApplication, 1)
		
	def test_getNoteNo(self):
		a1 = NotesApplication('Kevin')
		a1.create('Note 1') 
		a1.create('Note 2') 
		self.assertEqual('Note 1', a1.get(0), msg = "Wrong")

	def test_getIdNo_out_of_range(self):
		a1 = NotesApplication('Kevin')
		a1.create('Note 1') # 0
		a1.create('Note 2') # 1
		self.assertEqual('Note number not in list', a1.get(3), msg = "Note number entered not in range list")

	def test_getIdNo_in_range(self):
		a1 = NotesApplication('Kevin')
		a1.create('Note 1') # 0
		a1.create('Note 2') # 1
		self.assertNotEqual('Note number not in list', a1.get(0), msg = "Note number entered not in range list")

	def test_search_text_not_in(self):
		a1 = NotesApplication('Anna')
		a1.create('ann')
		self.assertEqual('Text not in list', a1.search('tt'), msg = "Search text not in list")

if __name__ == '__main__':
	unittest.main()