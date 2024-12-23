from dataclasses import dataclass

@dataclass
class Student:
    """
    Класс, представляющий информацию о студенте

    :param name: str: Имя студента
    :param age: int: Возраст студента
    :param major: str: Специальность студента
    :param: gpa: float|int: Средний балл студента
    """
    name: str
    age: int
    major: str
    gpa: float | int


    def display_info(self) -> str:
        """
        Метод, возвращающий информацию о студенте

        :return: str: Информация о студенте

        >>> student = Student('Alice', 22, 'Computer Science', 4.6)
        >>> student.display_info()
        'Имя: Alice, возраст: 22, специальность: Computer Science, средний балл: 4.6'
        """
        return f'Имя: {self.name}, возраст: {self.age}, специальность: {self.major}, средний балл: {self.gpa}'


    def calculate_grade(self) -> str:
        """
        Метод, возвращающий округленный средний балл в виде оценки студента

        :return: str: Оценка студента

        >>> student = Student('Alice', 22, 'Computer Science', 4.6)
        >>> student.calculate_grade()
        'Отлично'
        """
        round_grate = round(self.gpa)
        if round_grate <= 2:
            return 'Неудовлетворительно'
        elif round_grate == 3:
            return 'Удовлетворительно'
        elif round_grate == 4:
            return 'Хорошо'
        else:
            return 'Отлично'



def student_sorting(students) -> list[Student]:
    """
    Метод, сортирующий список студентов students по уменьшению среднего балла gpa

    :param students: list[Student]: Изначальный список студентов
    :return: list[Student]: Отсортированный список студентов

    >>> students = [Student("Alice", 20, "Computer Science", 3.8), Student("Charlie", 21, "Mathematics", 4.5)]
    >>> print(student_sorting(students))
    [Student(name='Charlie', age=21, major='Mathematics', gpa=4.5), Student(name='Alice', age=20, major='Computer Science', gpa=3.8)]
    """
    return sorted(students, key=lambda student: student.gpa, reverse=True)


# Создание списка студентов
students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
]

# Отображение информации о студентах
for student in students:
    student.display_info()

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")

print(student_sorting(students))

'''practicum7_annot.py'''