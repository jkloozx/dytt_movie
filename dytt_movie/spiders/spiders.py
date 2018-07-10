import scrapy
from ..items import DyttMovieItem
import json
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["loldytt.com"]
    # 各个类别列表头
    start_urls = [
        "https://www.loldytt.com/Dongzuodianying/top/1.html",
        "https://www.loldytt.com/Xijudianying/top/1.html",
        "https://www.loldytt.com/Aiqingdianying/top/1.html",
        "https://www.loldytt.com/Juqingdianying/top/1.html",
        "https://www.loldytt.com/Zhanzhengdianying/top/1.html",
        "https://www.loldytt.com/Anime/mark/1.html"
    ]

    def parse(self, response):
        #找到每个电影的详情页地址
        hrefs = response.css('#classpage > div.middle2aa1 > div.box3 > div > ul > li > div > a::attr(href)').extract()
        # num = 1

        #遍历详情页并爬取相应信息存入item
        for href in hrefs:
            # href = 'https://www.loldytt.com/Kehuandianying/fuchouzhelianmengdianying/'
            url = href
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            # title = sel.css('.articleTitle a::text').extract()[0]
            # feed = sel.css('.articleFeed::text').extract()[0]
            # tags = sel.css('.articleTags ul a::text').extract()
        netx_href = response.xpath('//a[contains(text(),"下一页")]/@href').extract()
        print(netx_href)
        if len(netx_href) > 0:
            url = 'https://www.loldytt.com' + netx_href[0]
            yield scrapy.Request(url, callback=self.parse)

    def parse_dir_contents(self, response):
            item = DyttMovieItem()
            item['cat'] = response.xpath('/html/body/center/div[7]/div[1]/h1/text()[1]').re('([\u4e00-\u9fa5]{2,4})')
            item['title'] = response.xpath('/html/body/center/div[7]/div[1]/h1/a/text()').extract()
            item['actor'] = response.xpath('/html/body/center/div[7]/div[2]/div[1]/div[2]/ul/li/text()').extract()
            # item['hot_point'] = response.xpath('//*[@id="allhits"]/text()').extract()[0]
            item['hot_point'] = '0'
            item['plot'] = response.xpath('//*[@id="juqing"]/div[2]/p/text()').extract()

            item['cat'] = item['cat'][0] if len(item['cat']) else ''
            item['title'] = item['title'][0] if len(item['title']) else ''
            item['actor'] = item['actor'][0] if len(item['actor']) else ''
            item['plot'] = item['plot'][0] if len(item['plot']) else ''


    # hot_page = response.xpath('//script[contains(@src,"transfer.asp")]/@src').extract()[0]
            # item['hot_point'] = scrapy.Request(hot_page, callback=self.get_all_hit)
            item['magnetic_link'] = ''
            item['thunder_link'] = ''
            item['bt_link'] = ''
            m_arr = {}
            t_arr = {}
            b_arr = {}
            # m_links = response.css('#ljishu .con4 .downurl li a::attr(href)').extract()
            m_links = response.css('#ljishu .con4 .downurl li a')
            for link in m_links:
                m_arr[link.css('a::text').extract()[0]] = link.css('a::attr(href)').extract()[0]
            item['magnetic_link'] = json.dumps(m_arr)

            t_link = response.css('#jishu .con4 .downurl li a')
            for link in t_link:
                t_arr[link.css('a::text').extract()[0]] = link.css('a::attr(href)').extract()[0]
            item['thunder_link'] = json.dumps(t_arr)

            b_link = response.css('#bt ul li a')
            for link in b_link:
                b_arr[link.css('a::text').extract()[0]] = link.css('a::attr(href)').extract()[0]
            item['bt_link'] = json.dumps(b_arr)

            yield item
    def get_all_hit(self,response):
            allhit = response.css('p').re("document.getElementById\(\"allhits\"\).innerHTML='(\d+)';")[0]
            return allhit