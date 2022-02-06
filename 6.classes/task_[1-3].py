from ast import Pass

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0
    def rate_hw(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and rate <=10:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'
    def __str__(self):
        result = (f'Имя: {self.name} \n'
                 f'Фамилия: {self.surname} \n'
                 f'Средняя оценка за домашние задания: {sum(self.grades[self.courses_in_progress[0]]) / len(self.grades[self.courses_in_progress[0]])} \n'
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                 f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.avg_grade < other.avg_grade    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}
        self.avg_rate = 0
    def get_list(self):
        return [self.name, self.surname, self.courses_attached, self.rates]
    def __str__(self):
        result = (f'Имя: {self.name} \n'
                 f'Фамилия: {self.surname} \n'
                 f'Средняя оценка за лекции: {self.avg_rate}')
        return result
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.avg_rate < other.avg_rate

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade <=10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        result = (f'Имя: {self.name} \n'
                 f'Фамилия: {self.surname}')
        return result

best_student_one = Student('Arisa', 'Faned', 'female')
best_student_one.courses_in_progress += ['Python', 'Git']
best_student_one.finished_courses += ['Введение в программирование']

best_student_two = Student('Men', 'Homo', 'male')
best_student_two.courses_in_progress += ['Python', 'Git']
best_student_two.finished_courses += ['Введение в программирование']

best_lector_one = Lecturer('Lecter', 'Hannibal')
best_lector_one.courses_attached += ['Python']

best_lector_two = Lecturer('Hid', 'Aswer')
best_lector_two.courses_attached += ['Python']

reviewer_students = Reviewer('Rev', 'Ewer')
reviewer_students.courses_attached += ['Python']
reviewer_students.rate_hw(best_student_one, 'Python', 5)
reviewer_students.rate_hw(best_student_one, 'Python', 4)
reviewer_students.rate_hw(best_student_two, 'Python', 7)
reviewer_students.rate_hw(best_student_two, 'Python', 5)

rate_lector = best_student_one
rate_lector.rate_hw(best_lector_one, 'Python', 8)
rate_lector.rate_hw(best_lector_one, 'Python', 3)
best_lector_one.avg_rate = sum(best_lector_one.rates[best_lector_one.courses_attached[0]]) / len(best_lector_one.rates[best_lector_one.courses_attached[0]])
rate_lector.rate_hw(best_lector_two, 'Python', 7)
rate_lector.rate_hw(best_lector_two, 'Python', 5)
best_lector_two.avg_rate = sum(best_lector_two.rates[best_lector_two.courses_attached[0]]) / len(best_lector_two.rates[best_lector_two.courses_attached[0]])

print(best_lector_one.__lt__(best_lector_two))

print(reviewer_students, '\n')
print(best_lector_one, '\n')
print(best_student_one, '\n')


print("Сравнение лекторов между собой по средней оценке:")
print(best_lector_one.__lt__(best_lector_two))

print("Сравнение студентов между собой по средней оценке:")
print(best_student_two.__lt__(best_student_one))