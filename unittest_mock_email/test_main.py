import unittest
from unittest.mock import ANY, patch

from main import enviar_email


class TestEmail(unittest.TestCase):
    @patch("smtplib.SMTP")
    def test_enviar_email(self, mock_smtp):
        instance = mock_smtp.return_value

        enviar_email("smtp.example.com", 123, "gon@example.com",
                     "killua@example.com", "Assunto", "Conteúdo do e-mail")
        mock_smtp.assert_called_with("smtp.example.com", 123)
        instance.starttls.assert_called_with()
        instance.login.assert_called_with("gon@example.com", "password")
        instance.sendmail("gon@example.com", "killua@example.com", ANY)
        instance.quit.assert_called_with()


if __name__ == "__main__":
    unittest.main()
