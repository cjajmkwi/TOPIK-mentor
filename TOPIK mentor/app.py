# app.py
from models import User, Vocabulary, GrammarPoint, Test
from data import vocabulary_words, grammar_rules, test1

def main():
    # 1. Регистрация/Вход (упрощено - создаем одного пользователя)
    user = User("testuser", "password", 1) # пароль в открытом виде - только для примера!
    print(f"Добро пожаловать, {user.username}!")

    # 2. Главное меню
    while True:
        print("\nВыберите действие:")
        print("1. Изучить лексику")
        print("2. Изучить грамматику")
        print("3. Пройти тест")
        print("4. Учиться") # Учимся
        print("5. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            print("\nЛексика:")
            for word in vocabulary_words:
                print(word.display())

        elif choice == '2':
            print("\nГрамматика:")
            for rule in grammar_rules:
                print(rule.display())

        elif choice == '3':
            print(f"\nПрохождение теста: {test1.name}")
            user.take_test(test1)

        elif choice == '4':
            user.study("корейский")
        elif choice == '5':
            print("Выход из приложения.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()