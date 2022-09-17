from src.items import ChirodirectoryItem
from src.spiders.pages.base import ItemWebPage


class ProfiledPage(ItemWebPage):
    def to_item(self) -> ChirodirectoryItem:
        item = ChirodirectoryItem()
        item["title"] = self.response.css("h1::text").getall() or ""
        item["mail"] = self.response.xpath("//span/a[@href]").re(r"mailto:(.*@*)") or ""
        item["site"] = self.response.xpath("//span/a[@href]").re(r"http.*://(.*)") or ""
        item["info"] = self.response.xpath('//div[@class="cols-2"]/div[@class="col"]/p/text()').getall()[:4] or ""
        return item
