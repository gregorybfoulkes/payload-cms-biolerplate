import requests

class ApiService:
    """
    A class to handle API interactions for the Payload CMS.
    """

    def __init__(self, api_key, base_url):
        """
        Initializes the ApiService with an API key and base URL.

        Args:
            api_key (str): The API key for authentication.
            base_url (str): The base URL for the API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_data(self, endpoint):
        """
        Fetches data from the specified endpoint.

        Args:
            endpoint (str): The API endpoint to fetch data from.

        Returns:
            dict: The JSON response from the API.
        """
        response = requests.get(f"{self.base_url}/{endpoint}", headers={"Authorization": f"Bearer {self.api_key}"})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def post_data(self, endpoint, data):
        """
        Sends data to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send data to.
            data (dict): The data to send in the request body.

        Returns:
            dict: The JSON response from the API.
        """
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers={"Authorization": f"Bearer {self.api_key}"})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()