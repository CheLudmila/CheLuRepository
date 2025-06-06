while True:
    word = input("Введіть слово, що містить літеру 'h' або 'H': ")
    if 'h' in word.lower():
        print("Дякуємо! Ви ввели правильне слово:", word)
        break
    else:
        print("Помилка: слово не містить літери 'h'. Спробуйте ще раз.")


