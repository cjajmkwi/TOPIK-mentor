# models.py
class User:
    def __init__(self, username, password, topik_level):
        self.username = username
        self.password = password # В реальном проекте - хэш пароля!
        self.topik_level = topik_level
        self.score = 0

    def study(self, topic):
        print(f"Изучаем {topic}")
        self.score += 10

    def take_test(self, test):
        result = test.run_test()
        self.score += result #  Добавляем баллы за тест
        print(f"Результат теста: {result}/100")

class Vocabulary:
    def __init__(self, korean, english, topic):
        self.korean = korean
        self.english = english
        self.topic = topic

    def display(self):
        return f"{self.korean} - {self.english} ({self.topic})"

class GrammarPoint:
    def __init__(self, name, explanation, level):
        self.name = name
        self.explanation = explanation
        self.level = level

    def display(self):
        return f"{self.name}: {self.explanation} (Уровень: {self.level})"

class Question: # для большей гибкости вопросов
    def __init__(self, text, options, correct_answer, explanation=None):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation # Объяснение правильного ответа (необязательно)

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")

    def check_answer(self, user_answer):
        try:
            return int(user_answer) - 1 == self.correct_answer
        except ValueError:
            return False

    def get_explanation(self):
        return self.explanation

class Test:
    def __init__(self, name, questions, level):
        self.name = name
        self.questions = questions
        self.level = level # уровень сложности теста (TOPIK 1, TOPIK 2)

    def run_test(self):
        score = 0
        for i, question in enumerate(self.questions):
            print(f"\nВопрос {i + 1}:")
            question.display()
            user_answer = input("Ваш ответ (номер варианта): ")
            if question.check_answer(user_answer):
                score += 20  #  Пример: 20 баллов за каждый правильный ответ
                print("Правильно!")
                if question.get_explanation():
                    print(f"Объяснение: {question.get_explanation()}")
            else:
                print("Неправильно.")
                if question.get_explanation():
                     print(f"Объяснение: {question.get_explanation()}")

        return score