import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator  # Используем библиотеку deep_translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        # Отправляем запрос
        response = requests.get(url)
        response.raise_for_status()  # Проверяем статус ответа

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")

        # Получаем слово и описание
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Возвращаем результат в виде словаря
        return {
            "english_word": english_words,  # Исправлено название ключа
            "word_definition": word_definition
        }

    except Exception as e:
        # Обработка ошибок
        print(f"Произошла ошибка: {e}")
        return None  # Возвращаем None в случае ошибки


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        # Получаем данные из функции
        word_dict = get_english_words()

        # Проверяем, что данные удалось получить
        if not word_dict:
            print("Не удалось получить данные о слове. Попробуйте позже.")
            break

        word = word_dict.get("english_word")  # Исправлен ключ
        word_definition = word_dict.get("word_definition")  # Убрали ошибку с переносом строки

        # Перевод слова на русский
        try:
            translation = GoogleTranslator(source="en", target="ru").translate(word)
        except Exception as e:
            print(f"Ошибка перевода: {e}")
            translation = "(невозможно перевести)"

        # Начинаем игру
        print(f"Значение слова: {word_definition}")
        print(f"Подсказка: перевод слова - {translation}")
        user = input("Что это за слово? ")

        if user.lower() == word.lower():  # Сравнение без учёта регистра
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано слово: {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

# Запускаем игру
if __name__ == "__main__":
    word_game()