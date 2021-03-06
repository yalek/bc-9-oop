class NotesApplication(object):

	def __init__(self, author):
		if type(author) is not str:
			raise TypeError
		else:
			self.author = author
		self.notes_list = []

	def create(self, note_content):
		self.notes_list.append(note_content)

	def list(self):
		for note in self.notes_list:
			note_id = self.notes_list(note)
			print("Note ID: " + str(note_id))
			print(note)
			print("By Author " + self.author)

	def get(self, note_id):
		if note_id in range(len(self.notes_list)):
			return self.notes_list[note_id]
		else:
			return "Note number not in list"

	def search(self, search_text):
		print("Showing results for search: " + search_text)
		for note in self.notes_list:
			if search_text in note:
				print("Note ID: " + self.notes_list.index(note))
			else:
				return "Text not in list"

		print("By Author " + self.author)

	def delete(self, note_id):
		if note_id in range(len(self.notes_list)):
			self.notes_list.remove(self.notes_list[note_id])
		else:
			return "invalid note_id"

	def edit(self, note_id, new_content):
		if note_id in range(len(self.notes_list)):
			self.notes_list[note_id] = new_content
		else:
			return "invalid note_id"
