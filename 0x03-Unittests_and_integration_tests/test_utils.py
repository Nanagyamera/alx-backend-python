#!/usr/bin/env python3
"""
Model for testing the utils.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: dict,
        path: tuple,
        expected_result: Union[dict, int],
    ) -> None:
        """
        Tests `access_nested_map`'s output.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple):
        """
        Tests `access_nested_map`'s exception raising.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"KeyError: '{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    Tests the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
        self,
        test_url: str,
        test_payload: dict,
        mock_requests_get,
    ):
        """
        Tests get_json's output.
        """
        mock_response = mock_requests_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Tests the memoize function.
    """

    def test_memoize(self):
        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        test_class_instance = TestClass()

        with patch.object(test_class_instance, 'a_method', return_value=42) \
                as mock_method:
            result_1 = test_class_instance.a_property()
            result_2 = test_class_instance.a_property()

            mock_method.assert_called_once()
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)


if __name__ == '__main__':
    unittest.main()
