
from scrapy_probe.__main__ import main


def test_main():
    assert main([]) == 0
