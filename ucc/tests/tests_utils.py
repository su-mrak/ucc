from django.test import TestCase
from ucc.utils import read_dataframe_from_json

import pandas as pd


class JsonToCsvTests(TestCase):
    def test_json_to_csv(self):
        json_data = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'

        expected_df = pd.read_json(json_data)

        result = read_dataframe_from_json(json_data)
        self.assertEqual(result, expected_df)
