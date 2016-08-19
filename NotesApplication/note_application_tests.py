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

	def test_delete_note(self):
		a1 = NotesApplication('Yusuf')
		a1.create('Bread')
		a1.create('Chips')
		a1.create('Water')
		self.assertEqual('invalid note_id', a1.delete(3), msg = "Note Id entered not in list")

	def test_edit_note(self):
		a1 = NotesApplication('Njoro')
		a1.create('Visa rules')
		a1.create('Passport rules')
		self.assertEqual('invalid note_id', a1.edit(2, 'Hoe to apply'), msg = "Note Id entered not found")

if __name__ == '__main__':
	unittest.main()