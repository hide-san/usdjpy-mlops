import unittest
from fetch import fetch_data

class TestFetchData(unittest.TestCase):

    def test_fetch_data_success(self):
        response = fetch_data('valid_parameter')  # Replace with an actual valid parameter
        self.assertIsNotNone(response)
        self.assertEqual(response['status'], 'success')  # Adjust based on actual response structure

    def test_fetch_data_invalid_parameter(self):
        with self.assertRaises(ValueError):  # Adjust the exception based on actual implementation
            fetch_data('invalid_parameter')

    def test_fetch_data_no_internet_connection(self):
        with self.assertRaises(ConnectionError):  # Adjust based on actual implementation
            fetch_data('parameter_that_causes_no_connection')

if __name__ == '__main__':
    unittest.main()