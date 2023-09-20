class SchoolJournal:
    def __init__(self, subject, student):
        self.student = student
        self.subject = subject
        self.grade_list = []

    def grade(self, n):
        self.grade_list.append(n)
    
    def printer(self):
        print(subject, student, grade_list)
    
    def final_grade(self, grade_list):
        checks = sum(grade_list) / len(grade_list)
        print(checks)

schJ = SchoolJournal('Math', 'Georgiy')

schJ.grade(3)
schJ.grade(4)
schJ.grade(1)
schJ.grade(4)
print(schJ.subject)

print(schJ.student)

print(schJ.grade_list)

print(schJ.final_grade)

schJ.printer()
print(schJ.printer)