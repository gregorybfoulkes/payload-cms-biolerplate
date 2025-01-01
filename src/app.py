# Basic application structure
from content_manager import ContentManager

content_manager = ContentManager()

# Example usage
if __name__ == '__main__':
    print('Welcome to the Payload CMS Boilerplate!')
    # Add your application logic here
    
    # Create content
    content_manager.create_content('First Post', 'This is the body of the first post.')
    
    # Read content
    all_content = content_manager.read_content()
    print('All Content:', all_content)
    
    # Update content
    content_manager.update_content(0, 'Updated Post', 'This is the updated body.')
    
    # Delete content
    content_manager.delete_content(0)
    
    print('Content after deletion:', content_manager.read_content())
{{ ... }}
import sqlite3

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.payload_config = self.load_config()
        self.db_path = self.get('DB_PATH')  # Add database path to config

    def load_config(self):
        with open(self.config_file) as f:
            return json.load(f)

    def get(self, key):
        return self.payload_config.get(key)

config = Config()

# Database initialization
def init_db():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    # Create tables if they do not exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS payload (
        id INTEGER PRIMARY KEY,
        data TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

init_db()
{{ ... }}