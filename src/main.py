from services.api_services import ApiService
from models.content import Content

def main():
    # Initialize your services and models here
    api_service = ApiService(api_key='your_api_key', base_url='https://api.example.com')
    
    # Example usage of the Content model
    content_item = Content(title='Sample Title', body='This is a sample body.')
    print(content_item.to_dict())

if __name__ == '__main__':
    main()