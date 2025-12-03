import unittest
from unittest.mock import Mock, patch

from main import obter_dados_usuario


class TestDadosUsuario(unittest.TestCase):
    @patch('main.requests.get')
    def test_obter_dados_usuario(self, mock_get):
        # obter_dados_user(12)
        mock_response = Mock()
        response_dict = {
            "nome": "Anakin",
            "email": "anakin@example.com"
        }
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        dados_usuario = obter_dados_usuario(1)
        mock_get.assert_called_with("https://api.example.com/users/1")
        self.assertEqual(dados_usuario, response_dict)


if __name__ == "__main__":
    unittest.main()
