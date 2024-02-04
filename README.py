class Student:
    def __init__(self, name, surname, gender, lecturer):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
        self.lecturer = lecturer
        self.course = None
    
    def enroll_course(self, course):
        self.course = course
        self.lecturer.add_course(course)
    
    def rate_lecturer(self, rating):
        if self.course is None:
            print("Студент не записан на курс")
            return
        
        if self.course not in self.lecturer.courses:
            print("Лектор не преподает данный курс")
            return
        
        if self.course not in self.lecturer.ratings:
            self.lecturer.ratings[self.course] = []
        
        self.lecturer.ratings[self.course].append(rating)
        
        print("Оценка успешно добавлена")
    def __str__(self):
        avg_grade = sum(self.grades.values()) / len(self.grades) if len(self.grades) > 0 else 0
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
    return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {avg_grade}\n Курсы в процессе изучения: {in_progress_courses}\n Завершенные курсы: {finished_courses}"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __eq__(self, other):
        if isinstance(other, Mentor):
    return self.name == other.name and self.surname == other.surname
    return False

def __ne__(self, other):
    return not self.__eq__(other)

def __lt__(self, other):
    if isinstance(other, Mentor):
        return self.name < other.name or (self.name == other.name and self.surname < other.surname)
    return NotImplemented

def __le__(self, other):
    return self.__lt__(other) or self.__eq__(other)

def __gt__(self, other):
    return not self.__le__(other)

def __ge__(self, other):
    return self.__eq__(other) or self.__gt__(other)
        
    
class Mentor(Lecturer):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.ratings = {}
    
    def add_course(self, course):
        if course not in self.courses_attached:
            self.courses_attached.append(course)
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.name == other.name and self.surname == other.surname
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.name < other.name or (self.name == other.name and self.surname < other.surname)
        return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
        
    def __str__(self):
        full_name = f"Имя: {self.name}\n Фамилия: {self.surname}"
        average_rating = sum(sum(rating) for rating in self.ratings.values()) / len(self.ratings) if self.ratings else 0
        return f"{full_name}\n Средняя оценка за лекции: {average_rating:.1f}"

class Mentor(Reviewer)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}"
        

def average_grade_by_course(students, course):
    total_grade = 0
    count = 0
    
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    
    if count > 0:
        return total_grade / count
    else:
        return 0


def average_grade_by_lecture(lecturers, course):
    total_grade = 0
    count = 0
    
    for lecturer in lecturers:
        if course in lecturer.ratings:
            total_grade += sum(lecturer.ratings[course])
            count += len(lecturer.ratings[course])
    
    if count > 0:
        return total_grade / count
    else:
        return 0
lecturer1 = Lecturer("Ann", "Puk")
lecturer2 = Lecturer("Adam", "Smith")

student1 = Student("Alfred", "Trump", lecturer1)
student2 = Student("Alice", "Smith", lecturer2)

reviewer1 = Reviewer("Vlad", "Dud", lecturer1)
reviewer2 = Reviewer("Aziz", "Vovk", lecturer2)
                     

