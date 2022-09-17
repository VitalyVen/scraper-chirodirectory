import dataclasses

import scrapy
from scrapy.http import Response


class ItemWebPage:
    def __init__(self, response: Response) -> None:
        self.response = response

    def __getattr__(self, item: str):
        return getattr(self.response, item)

    def to_item(self) -> scrapy.Item | dict | dataclasses.dataclass:
        raise NotImplementedError()
