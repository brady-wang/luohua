import scrapy
from scrapy import Request
from jav.items import JavItem

class FirstSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['iqq1.fun', 'jp.netcdn.space']

    start_urls = ['https://avmoo.casa/cn/actresses/page/1']



    def start_requests(self):

        cookie = {'theme': 'auto', 'over18': '1', '_ym_uid': '1635847009406407938', '_ym_d': '1635847009', 'locale': 'zh', '_ym_isad': '2', '_jdb_session': 'd7ZdU%2FavfWLVXK9awNa7EMjxfLBzfMVzNGvc%2Ben0coKs5HLkhTx0ccudYHC64tahW80QoNySgBDBAloluO8j2nx7QVAOfdwTMPcXy%2FLiTVnzR4ZnoRUue3KAhy0d%2BfU7BnucgbQBsL4dWT3sXC%2Fo9pPNIB6JTq7J0zzHwyVQXrD82fT%2FWbh4fDkigs8h9BqX3MVG7p%2BWLu%2F%2BlEhAY1JVVilMXT7ojntHQNfJliLVuGp%2FaIrB32%2Bq0PmLfCLyICuo3qzUPWtOntj6FKUCWxkjNH1J0Ogf3NoESNWZgQJ1Afd8NweAWQQb84LZqbwS3XrG7VvRgOY1EFsIrkphS%2Ba4ij18ozHKriengUU0I2gNVZfQYeNBZuzTQ%2FqLxwYLt924FMA%3D--Z2aIizgjyA1RvpLH--%2BdCJUjvThBIUKi3WlBz52Q%3D%3D'}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
            "Referer": "https://javdb.com/",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "authority": "javdb.com",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }
        start_url = 'https://iqq1.fun/?cat=jp'
        yield scrapy.Request(url=start_url, headers=headers, cookies=cookie)

    def parse(self, response):
        print(response.status)

        print("----------crawl page " + response.url)

        if response.status == 200:
            ul = response.xpath('//div[@class="type_movie_clips"]//li[@class="one_type"]')
            item = JavItem()
            if len(ul) > 0 :
                for li in ul:
                    title = li.xpath(".//h3/text()").extract_first()
                    img = li.xpath(".//img/@src").extract_first()

                    item['image_name'] = title
                    item['image_urls'] = img
                    yield item

            nextPage = response.xpath('//a[contains(text(),">")]//@href').extract_first()
            if nextPage is not None:
                url = response.urljoin(nextPage)
                yield scrapy.Request(url, self.parse)