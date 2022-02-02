from ast import Pass

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
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
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}
    def get_list(self):
        return [self.name, self.surname, self.courses_attached, self.rates]
    def __str__(self):
        result = (f'Имя: {self.name} \n'
                 f'Фамилия: {self.surname} \n'
                 f'Средняя оценка за лекции: {sum(self.rates[self.courses_attached[0]]) / len(self.rates[self.courses_attached[0]])}')
        return result

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

best_student = Student('Arisa', 'Faned', 'female')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_lector = Lecturer('Lecter', 'Hannibal')
best_lector.courses_attached += ['Python']

reviewer_students = Reviewer('Rev', 'Ewer')
reviewer_students.courses_attached += ['Python']
reviewer_students.rate_hw(best_student, 'Python', 10)
reviewer_students.rate_hw(best_student, 'Python', 9)

rate_lector = best_student
rate_lector.rate_hw(best_lector, 'Python', 10)
rate_lector.rate_hw(best_lector, 'Python', 1)

print(reviewer_students, '\n')
print(best_lector, '\n')
print(best_student, '\n')