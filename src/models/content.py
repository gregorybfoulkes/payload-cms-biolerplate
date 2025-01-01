class Content:
    """
    A class to represent a content item in the Payload CMS.
    """

    def __init__(self, title, body):
        self.title = title  # Title of the content
        self.body = body    # Body of the content

    def __repr__(self):
        return f"Content(title={self.title}, body={self.body})"

    def to_dict(self):
        """Convert the content to a dictionary for easy serialization."""
        return {
            'title': self.title,
            'body': self.body
        }