import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from src.spiders.pages.profiled import ProfiledPage

settings = get_project_settings()

BASE_URL = "https://www.chirodirectory.com"
HEADERS = {
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",  # noqa: E501
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Referer": BASE_URL,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36",  # noqa: E501
    "X-Requested-With": "XMLHttpRequest",
}


class Chir(scrapy.Spider):
    name = "chir"
    allowed_domains = [
        BASE_URL.removeprefix("https://"),
    ]
    start_urls = ["https://www.chirodirectory.com/chiropractors/"]

    def start_requests(self):
        for p in self.start_urls:
            yield scrapy.Request(url=p, callback=self.browse_state, headers=HEADERS)

    def browse_state(self, response):
        links = response.xpath('//div[@class="cols-4"]/div/*/a/@href').getall()
        for link in links:
            yield response.follow(
                url=link,
                headers=HEADERS,
                callback=self.browse_in_state,
            )

    def browse_in_state(self, response):
        links = response.xpath('//div[@class="cols-3"]/div/*/a/@href').getall()
        for link in links:
            yield response.follow(
                url=link,
                headers=HEADERS,
                callback=self.find_profiled,
            )

    def find_profiled(self, response):
        links = response.xpath('//div[@class="results profiled-results"]/div/a/@href').getall()
        if links is not None:
            for link in links:
                yield response.follow(url=link, callback=self.parse)

    def parse(self, response):
        page = ProfiledPage.from_response(response)
        yield page.to_item()


if __name__ == "__main__":
    # This part is not launched in production with scrapyd, used it for make your local development more productive
    dev_settings: dict[str, str | int | bool | dict[str, int]] = {
        "LOG_LEVEL": "DEBUG",
        # "HTTPCACHE_ENABLED": True,
    }
    process = CrawlerProcess(settings=settings)
    Chir.custom_settings = Chir.custom_settings or {} | dev_settings
    process.crawl(Chir)
    process.start()  # the script will block here until the crawling is finished
