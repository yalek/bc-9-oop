import datetime
from student import Student
#create atleast 10 students

s1 = Student("Kevin", 'Chiteri')
s2 = Student ('Allan' , 'M.', 'UG')
s3 = Student ('Joy', 'Manono')
s4 = Student ('Jackie', 'Cherono')
s5 = Student("Julius", 'Howen')
s6 = Student ('James' , 'M.', 'TE')
s7 = Student ('Mathews', 'Batman')
s8 = Student ('Boswell', 'Man', 'KE')
s9 = Student("Allan", 'Kimani')
s10 = Student ('Ndegwa' , 'T.', 'UG')



s1.attend_class()
s2.attend_class()
s3.attend_class()
s4.attend_class()
s5.attend_class()
s6.attend_class()
s7.attend_class()
s8.attend_class()
s9.attend_class()
s10.attend_class()

Student.get_attendance(str(datetime.date.today()))
