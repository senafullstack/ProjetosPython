import unittest
from unittest.mock import patch
from app import obterprevisao


class TestWeatherAPI(unittest.TestCase):

    @patch('app.request')
    def test_get_weather_with_valid_city(self, mock_request):
        mock_request.args = {'city': 'Aracaju'}
        response = obterprevisao()
        self.assertEqual(response["city"], "Aracaju")

if __name__ == '__main__':
    unittest.main()
