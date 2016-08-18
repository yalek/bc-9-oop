import datetime
map_ = {"KE" : "kenya",
        "TE" : "Tanzania",
        "UG" : "Uganda",
        "NG" : "Nigeria"}
class Student(object):
    count = 0
    class_attendance = {}
    def __init__(self, fname, lname, cc = "KE"):
        Student.count = Student.count + 1
        self.__id = Student.count
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]
    #def attend_class(self, **kwargs):#**kwargs- key word arguments

    def attend_class(self, **kwargs):
        """ default values. 
            loc = "Hogwarts"
            time = current date
            teacher = alex 
            generate unique id"""
        
        loc = kwargs.get('loc', 'Hogwarts')
        teacher = kwargs.get('teacher', 'Alex')
        date = kwargs.get('date', str(datetime.date.today()))

        full_name = self.fname + " " + self.lname
        
        if date in Student.class_attendance.keys():
            Student.class_attendance[date].append(self.fname + " " + self.lname)
        else:
            Student.class_attendance[date] = [full_name]

    @staticmethod
    def get_attendance(date):
        # return Student.class_attendance[date]
        if date in Student.class_attendance.keys():
            print(Student.class_attendance[str(date)])
        else:
            print("no records")






