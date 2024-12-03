
class Student: 
    report = {
        'name': {
            'Subject': {
                'marks': ''
            }
        }
    }
    def __init__(self, name, roll_number, subject, marks, teacher):
        self.name = name 
        self.roll_number = roll_number 
        self.subject = subject
        self.teacher = teacher
        self.marks = marks

    def add_marks(self): 
        Student.report[self.name] = {
            self.subject: {
                'Enroll Number': self.roll_number,
                'marks': self.marks,
                'teacher': self.teacher
            }
    
        }
        print(f'successfully added the marks for {self.name}')
    
    def average_score(self):
        pass 

    def show_report(self): 
        # for key, value in Student.report.items(): 
        #         print(f'here is the report for {self.name}, {key}, {value}')
        print(Student.report)



student1 = Student('James Shuta', 454453, 'physics', 60/100, 'Isaac')
student2 = Student('Nkenganyi Clarence',344333,  'Biology', 95, 'Philip')
student3 = Student('Jingwa Laura',344333,  'Geography', 95, 'Philip')

student3.add_marks()
student1.add_marks()
student2.add_marks()

student2.show_report()




