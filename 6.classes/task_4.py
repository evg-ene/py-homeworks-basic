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
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and rate <= 10:
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
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and grade <= 10:
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

best_student_two = Student('Den', 'Marius', 'male')
best_student_two.courses_in_progress += ['Python', 'C++']
best_student_two.finished_courses += ['Введение в программирование']

best_lector_one = Lecturer('Lecter', 'Hannibal')
best_lector_one.courses_attached += ['Python']

best_lector_one = Lecturer('Lecter', 'Hannibal')
best_lector_one.courses_attached += ['Python', 'Git']
best_lector_two = Lecturer('Das', 'Wsad')
best_lector_two.courses_attached += ['C++']

reviewer_students = Reviewer('Rev', 'Ewer')
reviewer_students.courses_attached += ['Python', 'Git', 'C++']
reviewer_students.rate_hw(best_student_one, 'Python', 10)
reviewer_students.rate_hw(best_student_one, 'Python', 9)
reviewer_students.rate_hw(best_student_one, 'Git', 7)
reviewer_students.rate_hw(best_student_one, 'Git', 5)
reviewer_students.rate_hw(best_student_two, 'Python', 8)
reviewer_students.rate_hw(best_student_two, 'Python', 3)
reviewer_students.rate_hw(best_student_two, 'C++', 5)
reviewer_students.rate_hw(best_student_two, 'C++', 6)

rate_lector_one = best_student_one
rate_lector_one.rate_hw(best_lector_one, 'Python', 10)
rate_lector_one.rate_hw(best_lector_one, 'Python', 1)
rate_lector_one.rate_hw(best_lector_one, 'Git', 10)
rate_lector_one.rate_hw(best_lector_one, 'Git', 10)

rate_lector_two = best_student_two
rate_lector_two.rate_hw(best_lector_two, 'C++', 10)
rate_lector_two.rate_hw(best_lector_two, 'C++', 1)

list_stds = []
list_stds.append(best_student_one)
list_stds.append(best_student_two)

list_lcrs = []
list_lcrs.append(best_lector_one)
list_lcrs.append(best_lector_two)

list_crs = ['Python', 'C++', 'Git']


def average_rate_students(list_students, course_students):
    for cource in course_students:
        list_rates = []
        for std in list_students:
            if cource in std.courses_in_progress:
                list_rates += std.grades.get(cource)
        print(cource, ': ', (sum(list_rates) / len(list_rates)))


def average_rate_lecturers(list_lecturers, course_lecturers):
    for cource in course_lecturers:
        list_rates = []
        for lcr in list_lecturers:
            if cource in lcr.courses_attached:
                list_rates += lcr.rates.get(cource)
        print(cource, ': ', (sum(list_rates) / len(list_rates)))


print('Средняя оценка за домашние задания по всем студентам в рамках конкретного курса')
average_rate_students(list_stds, list_crs)
print('Средняя оценка за лекции всех лекторов в рамках курса')
average_rate_lecturers(list_lcrs, list_crs)
