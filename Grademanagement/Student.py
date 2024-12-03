import csv

class Student: 
    reports = {
       
    }
    def __init__(self, name, roll_number, subject, marks, teacher):
        self.name = name 
        self.roll_number = roll_number 
        self.subject = subject
        self.teacher = teacher
        self.marks = marks

    def add_marks(self): 
        Student.reports[self.name] = {
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
        with open('results.csv', mode='w', encoding='utf-8', newline='') as file: 
                    writer = csv.writer(file)
                   
                    writer.writerow(['Student Name', 'Subject', 'Enroll Number', 'Marks', 'Teacher'])
                    for student, marks in Student.reports.items(): 
                        print(f'student: {student}')
                        for subject, details in marks.items(): 
                            print(f'subject: {subject}')            
                            print(f"Enrollment Number: {details['Enroll Number']}")
                            print(f"Marks: {details['marks']}")
                            print(f"Teacher: {details['teacher']}\n")
                            writer.writerow([student, subject, details['Enroll Number'], details['marks'], details['teacher']])
        
        print('successfully saved')


student1 = Student('James Shuta', 454453, 'physics', 60/100, 'Isaac')
student2 = Student('Nkenganyi Clarence',344333,  'Biology', 95, 'Philip')
student3 = Student('Jingwa Laura',344333,  'Geography', 95, 'Philip')
student4 = Student('Anyichap Sandra', 3944333,  'Programming 101', 65, 'Lechendem Stephen')
student5 = Student('Anyichap Sandra', 3944333,  'Frontend Development ', 65, 'Lechendem Stephen')




student3.add_marks()
student1.add_marks()
student2.add_marks()
student4.add_marks()
student5.add_marks()


student2.show_report()






