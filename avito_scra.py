import scrapy


#class BashSpider(scrapy.Spider):
    # имя парсера
   # name = 'BashSpider'
    # список ссылок для парсинга
   # start_urls = ['http://bash.im']

    # функция парсингаs
    #def parse(self, responce):
        # итерирумся по div.quote
        #for item in responce.css('div.quote'):
            # выдёргиваем нужные блоки
        #    block = item.css('div.quote div.actions')
        #    span = block.css('span')
            # собираем данные в словарь
         #   yield {
             #   'title': block.css('a.id::text').extract_first(),
              # 'text': item.css('div.text::text').extract_first(),
             #   'rating': span.css('span.rating::text').extract_first(),
             #   'date': span.css('span.date::text').extract_first(),
            #   'url': block.css('a.id::attr(href)').extract_first()
           # }
        # итерируемся по url страниц
        #for next_page in responce.css('div.pager a::attr(href)'):
         #   yield responce.follow(next_page, self.parse)

class AvitoSpider (scrapy.Spider):
    # имя парсера
    name = 'AvitoSpider'
#список ссылок для парсинга
    start_urls=['http://avito.ru/volgograd/kvartiry']

#функция парсинга
    def parse(self, responce):
        item=responce.css('title-info-title')
    #собираем данные в словарь
        yield {
            'title': item.css('span.title-info-title-text::text').extract_first(),
            'contactFace':item.css('div.seller-info-value::text').extract_first()
             }
    #итерируемся по url страниц
        for next_page in responce.css('div.item_table-description div.item_table-header h3.item-description-title a.item-description-title-link::attr(href)'):
         yield responce.follow(next_page,self.parse)