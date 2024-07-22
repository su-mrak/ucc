from typing_extensions import Self
import app
import pandas as pd


class TestAlgoritm:
    def test_no_unique_failes_with_exception(self: Self) -> None:
        df = pd.DataFrame([{"a": 1}, {"a": 1}])

        try:
            app.find_unique_column_combinations(df)
        except Exception:
            ...
        else:
            assert False, "should fail"

    def test_one_unique_found_ok(self: Self) -> None:
        df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 1, "b": 3}])

        res = app.find_unique_column_combinations(df)

        assert {"Признаки": {0: "b"}} == res.to_dict()

    def test_two_unique_found_ok(self: Self) -> None:
        df = pd.DataFrame(
            [
                {"a": 1, "b": 2, "c": 4},
                {"a": 1, "b": 2, "c": 5},
                {"a": 1, "b": 3, "c": 4},
            ]
        )

        res = app.find_unique_column_combinations(df)

        assert {"Признаки": {0: "b", 1: "c"}} == res.to_dict()

    def test_one_unique_found_when_there_is_more_options_ok(self: Self) -> None:
        df = pd.DataFrame(
            [
                {"a": 1, "b": 2, "c": 4, "d": 1},
                {"a": 1, "b": 2, "c": 5, "d": 2},
                {"a": 1, "b": 3, "c": 4, "d": 3},
            ]
        )

        res = app.find_unique_column_combinations(df)

        assert {"Признаки": {0: "d"}} == res.to_dict()
