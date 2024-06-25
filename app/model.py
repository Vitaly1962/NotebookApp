import json
from datetime import datetime

class NoteModel:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open('data/notes.json', 'r', encoding='utf-8') as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open('data/notes.json', 'w', encoding='utf-8') as f:
            json.dump(self.notes, f, indent=4, ensure_ascii=False)

    def add_note(self, title, content):
        new_note = {
            'id': len(self.notes) + 1,
            'title': title,
            'content': content,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'active'  # Задаем статус 'active' для новой заметки
        }
        self.notes.append(new_note)
        self.save_notes()
        return new_note['id']  # Возвращаем ID новой заметки


    def note_exists(self, note_id):
        return any(note['id'] == note_id for note in self.notes)

    def edit_note(self, note_id, new_title, new_content):
        for note in self.notes:
            if note['id'] == note_id and note['status'] == 'active':
                note['title'] = new_title
                note['content'] = new_content
                note['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id and note['status'] == 'active':
                note['status'] = 'deleted'
                self.save_notes()
                return True
        return False

    def filter_notes_by_date(self, filter_date):
        filtered_notes = [
            note for note in self.notes
            if datetime.strptime(note['created_at'], "%Y-%m-%d %H:%M:%S").date() == datetime.strptime(filter_date, "%Y-%m-%d").date()
            and note['status'] == 'active'
        ]
        return filtered_notes

    def get_notes(self):
        return self.notes