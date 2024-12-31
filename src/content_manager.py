import json

class ContentManager:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.load_content()

    def load_content(self):
        try:
            with open(self.filename, 'r') as file:
                self.content = json.load(file)
        except FileNotFoundError:
            self.content = []

    def save_content(self):
        with open(self.filename, 'w') as file:
            json.dump(self.content, file, indent=4)

    def create_content(self, title, body):
        new_entry = {'title': title, 'body': body}
        self.content.append(new_entry)
        self.save_content()

    def read_content(self):
        return self.content

    def update_content(self, index, title, body):
        if 0 <= index < len(self.content):
            self.content[index] = {'title': title, 'body': body}
            self.save_content()

    def delete_content(self, index):
        if 0 <= index < len(self.content):
            del self.content[index]
            self.save_content()
