from mysite.settings import DEBUG
from typing_extensions import Self


class TestDjango:
    def test_settings_ok(self: Self) -> None:
        assert DEBUG
