def text_to_binary(text: str) -> str:
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result
def binary_to_text(binary_string: str) -> str:
    try:
        binary_values = binary_string.split(' ')
        text_result = ''.join(chr(int(binary, 2)) for binary in binary_values)
        return text_result
    except ValueError:
        return "Ошибка"
    except Exception as e:
        return f"ошибка {e}"
def main():
    while True:
        print("\n--- Переводчик текста и двоичного кода ---")
        print("1. Перевести текст в двоичный код")
        print("2. Перевести двоичный код в текст")
        print("3. Выход")
        choice = input("Выберите опцию (1, 2 или 3): ")
        if choice == '1':
            print("Введите текст:")
            lines = []
            while True:
                line_input = input()
                if not line_input:
                    break
                lines.append(line_input)
            input_text = '\n'.join(lines)
            binary_code = text_to_binary(input_text)
            print(f"\nДвоичный код:\n{binary_code}")
        elif choice == '2':
            input_binary = input("Введите двоичный код: ")
            text_result = binary_to_text(input_binary)
            print(f"\nРезультат:\n{text_result}")
        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Введите 1, 2 или 3.")
if __name__ == "__main__":
    main()
