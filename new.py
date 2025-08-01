from unittest.mock import patch

def get_data_from_api():
    # Предположим, что здесь HTTP-запрос
    return "real data"

def test_mocked_api():
    with patch("__main__.get_data_from_api") as mock_api:
        mock_api.return_value = "fake data"
        result = get_data_from_api()
        assert result == "fake data"