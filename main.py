class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        output = f'Имя: {self.name}\
        \nФамилия: {self.surname}\
        \nСредняя оценка за домашние задания: {average_grade(self.grades)}\
        \nКурсы в процессе изучения: {self.courses_in_progress}\
        \nЗавершенные курсы: {self.finished_courses}'
        return output

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Ошибка в методе оценки лекторов'

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)
        return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return output

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(other_lecturer.grades)
        return


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

    def rate_hw(self, specific_student, course, grade):
        if isinstance(specific_student, Student) \
                and course in self.courses_attached \
                and course in specific_student.courses_in_progress:

            if course in specific_student.grades:
                specific_student.grades[course] += [grade]
            else:
                specific_student.grades[course] = [grade]
        else:
            return 'Ошибка в методе оценки студентов'


def average_grade(all_grades):
    counter = 0
    grade = 0
    for value in all_grades.values():
        grade += round(sum(value) / len(value), 2)
        counter += 1
    return grade


def average_course_grade(all_persons, current_course):
    all_course_grades = []
    for person in all_persons:
        if person.grades.get(current_course):
            all_course_grades.extend(person.grades.get(current_course))
    return average_grade({current_course: all_course_grades})


student_one = Student('Alex', 'Hirsch', '36')
student_one.courses_in_progress += ['Python']
student_one.courses_in_progress += ['Java']
student_one.finished_courses += ['Git']
student_one.grades['Git'] = [5, 6, 7]
student_one.grades['Python'] = [10, 10, 10, 10, 10, 10]
student_one.grades['Java'] = [9, 3]


student_two = Student('John', 'Dorian', '28')
student_two.courses_in_progress += ['Python']
student_two.finished_courses += ['Git']
student_two.courses_in_progress += ['Java']
student_two.grades['Git'] = [8, 9, 10]
student_two.grades['Python'] = [3, 4]
student_two.grades['Java'] = [9, 3]

student_list = [student_one, student_two]

lecturer_one = Lecturer('Corey', 'Taylor')
lecturer_one.courses_attached += ['Python']
lecturer_one.courses_attached += ['Java']
lecturer_one.courses_attached += ['Git']

lecturer_two = Lecturer('William', 'Murray')
lecturer_two.courses_attached += ['Python']
lecturer_two.courses_attached += ['Java']
lecturer_two.courses_attached += ['Git']

lecturer_list = [lecturer_one, lecturer_two]

reviewer_one = Reviewer('Tom', 'York')
reviewer_one.courses_attached += ['Python']

reviewer_two = Reviewer('Clint', 'Eastwood')
reviewer_two.courses_attached += ['Git']
reviewer_two.courses_attached += ['Java']


reviewer_one.rate_hw(student_one, 'Python', 4)
reviewer_one.rate_hw(student_one, 'Python', 7)
reviewer_two.rate_hw(student_one, 'Java', 10)
reviewer_two.rate_hw(student_two, 'Java', 4)
reviewer_two.rate_hw(student_two, 'Java', 7)
reviewer_two.rate_hw(student_two, 'Java', 10)
print(f'Оценка студенту 1 {student_one.grades}')
print(f'Оценка студенту 2 {student_two.grades}')

student_one.rate_lecturer(lecturer_one, 'Python', 2)
student_one.rate_lecturer(lecturer_one, 'Python', 4)
print(f'Оценка преподавателям {lecturer_one.grades}')

student_two.rate_lecturer(lecturer_two, 'Java', 9)
student_two.rate_lecturer(lecturer_two, 'Java', 5)
print(f'Оценка преподавателю 2 {lecturer_two.grades}')


print('Печать классов')
print(lecturer_two)
print()
print(lecturer_one)
print()
print(student_one)
print()
print(student_two)
print()

print('Средний балл студентов по курсу Git')
print(average_course_grade(student_list, 'Python'))

print('Средний балл лекторов по курсам Python')
print(average_course_grade(lecturer_list, 'Python'))

print('Проверка функций сравнения')
print(student_one < student_two)
print(student_two < student_one)

print(lecturer_one < lecturer_two)
print(lecturer_one < lecturer_two)
