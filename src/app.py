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
