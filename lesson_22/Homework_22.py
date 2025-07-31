import random
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Асоціативна таблиця для багато-багато зв’язку Студент-Курс
student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship('Course', secondary=student_course, back_populates='students')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    students = relationship('Student', secondary=student_course, back_populates='courses')

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"


# --- Налаштування БД та сесії ---
engine = create_engine('sqlite:///students_courses.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# --- Створення 5 курсів ---
course_titles = ["Math", "Physics", "Chemistry", "Biology", "History"]
courses = [Course(title=title) for title in course_titles]
session.add_all(courses)
session.commit()

# --- Створення 20 студентів ---
student_names = [f"Student{i}" for i in range(1, 21)]
students = [Student(name=name) for name in student_names]
session.add_all(students)
session.commit()

# --- Рандомно розподіляємо студентів по курсах ---
for student in students:
    # Кожен студент записується на 1-3 курси випадково
    selected_courses = random.sample(courses, random.randint(1, 3))
    student.courses.extend(selected_courses)

session.commit()


# --- Функція для додавання нового студента і додавання до курсу ---
def add_student(name, course_title):
    student = Student(name=name)
    # Шукаємо курс
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print(f"Курс '{course_title}' не знайдено")
        return
    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"Додано студента {name} до курсу {course_title}")


# --- Запити ---

# 1. Студенти, зареєстровані на певний курс
def students_in_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print(f"Курс '{course_title}' не знайдено")
        return
    print(f"Студенти на курсі {course_title}:")
    for s in course.students:
        print(s)


# 2. Курси, на які зареєстрований певний студент
def courses_of_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if not student:
        print(f"Студент '{student_name}' не знайдено")
        return
    print(f"Курси студента {student_name}:")
    for c in student.courses:
        print(c)


# --- Оновлення ---

def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if not student:
        print(f"Студент '{old_name}' не знайдено")
        return
    student.name = new_name
    session.commit()
    print(f"Ім'я студента оновлено з {old_name} на {new_name}")


def update_course_title(old_title, new_title):
    course = session.query(Course).filter_by(title=old_title).first()
    if not course:
        print(f"Курс '{old_title}' не знайдено")
        return
    course.title = new_title
    session.commit()
    print(f"Назва курсу оновлена з {old_title} на {new_title}")


# --- Видалення ---

def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if not student:
        print(f"Студент '{name}' не знайдено")
        return
    session.delete(student)
    session.commit()
    print(f"Студента {name} видалено")


# --- Приклад використання ---

if __name__ == "__main__":
    add_student("Олександр", "Math")
    students_in_course("Math")
    courses_of_student("Student1")
    update_student_name("Student1", "Іван")
    update_course_title("History", "World History")
    delete_student("Student2")