# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючий студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        if not (0 <= new_grade <= 100):
            raise ValueError("Середній бал повинен бути в межах 0-100")
        self.average_grade = new_grade

    def get_info(self):
        return (
            f"Ім'я: {self.first_name}\n"
            f"Прізвище: {self.last_name}\n"
            f"Вік: {self.age}\n"
            f"Середній бал: {self.average_grade}"
        )
# Створення об'єкта
student1 = Student("Людмила", "Череднюк", 32, 80)

    # Виведення початкової інформації
print("До оновлення:")
print(student1.get_info())

    # Оновлення середнього балу
student1.update_average_grade(100)

    # Виведення після змін
print("\nПісля оновлення:")
print(student1.get_info())