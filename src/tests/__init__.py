"""
tests.__init__ - A package for unit and integration tests for the Payload CMS.

This package contains various test cases that verify the functionality of the application.
"""

__version__ = "1.0.0"  # Version of the tests package

# Importing test cases for easy access
from .test_app import TestApp  # Example of importing a test case for the main application
from .test_api_services import TestApiService  # Example of importing a test case for the API service