from app.model import NoteModel
from app.view import UserInterface

class NoteController:
    def __init__(self):
        self.model = NoteModel()
        self.view = UserInterface()

    def run(self):
        self.view.display_welcome_message()
        while True:
            self.view.display_menu()
            choice = self.view.get_user_choice()
            if choice == '1':
                notes = self.model.get_notes()
                self.view.display_notes(notes)
            elif choice == '2':
                title, content = self.view.get_note_details()
                new_note_id = self.model.add_note(title, content)
                self.view.display_new_note_id(new_note_id)
            elif choice == '3':
                note_id = self.view.get_note_id()
                if self.model.note_exists(note_id):
                    title, content = self.view.get_note_details()
                    success = self.model.edit_note(note_id, title, content)
                    if success:
                        self.view.display_message("Заметка успешно отредактирована.")
                    else:
                        self.view.display_error("Произошла ошибка при редактировании заметки.")
                else:
                    self.view.display_error("Заметка не найдена.")
            elif choice == '4':
                note_id = self.view.get_note_id()
                if self.model.note_exists(note_id):
                    self.model.delete_note(note_id)
                    self.view.display_message("Заметка успешно удалена.")
                else:
                    self.view.display_error("Заметка не найдена.")
            elif choice == '5':
                filter_date = self.view.get_filter_date()
                filtered_notes = self.model.filter_notes_by_date(filter_date)
                self.view.display_notes(filtered_notes)
            elif choice.lower() == 'q':
                break
            else:
                self.view.display_invalid_input_message()

    def delete_note(self):
        note_id = self.view.get_note_id()
        if self.model.delete_note(note_id):
            self.view.display_message(f"Заметка с ID {note_id} помечена как удаленная.")
        else:
            self.view.display_error("Ошибка: Заметка не найдена.")