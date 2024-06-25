class UserInterface:
    def display_welcome_message(self):
        print("Привет! Это консольное приложение для работы с заметками.")

    def display_menu(self):
        print("\nМеню:")
        print("1. Просмотр заметок")
        print("2. Добавление заметки")
        print("3. Редактирование заметки")
        print("4. Удаление заметки")
        print("5. Фильтрация заметок по дате")
        print("q. Выход")

    def get_user_choice(self):
        return input("Введите команду: ").strip().lower()

    def get_note_details(self):
        title = input("Введите заголовок заметки: ").strip()
        content = input("Введите текст заметки: ").strip()
        return title, content

    def get_note_id(self):
        return int(input("Введите ID заметки: ").strip())

    def get_filter_date(self):
        return input("Введите дату для фильтрации (YYYY-MM-DD): ").strip()

    def display_notes(self, notes):
        active_notes = [note for note in notes if note.get('status') == 'active']
        if not active_notes:
            print("Список заметок пуст")
        else:
            for note in active_notes:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['content']}, Время создания: {note['created_at']}")

    def display_invalid_input_message(self):
        print("Неверный ввод. Попробуйте снова.")

    def display_error(self, message):
        print(f"Ошибка: {message}")

    def display_new_note_id(self, note_id):
        print(f"Новая заметка добавлена с ID: {note_id}")

    def display_message(self, message):
        print(message)