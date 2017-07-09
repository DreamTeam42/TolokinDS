import scrapy
import json

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
    start_urls=['http://avito.ru/volgograd/kvartiry/prodam']

#функция парсинга
    def parse(self, responce):
        item=responce.css('div.item-view-content')

    #собираем данные в словарь

        yield {
            'title': item.css('div.item-view-left div.title-info_mode-with-favorite div.title-info-main h1.title-info-title span.title-info-title-text::text').extract(),
            'seller':item.css('div.item-view-contacts.js-item-view-contacts div.item-view-seller-info div.seller-info.js-seller-info div.seller-info-prop.js-seller-info-prop_seller-name.seller-info-prop_layout-two-col div.seller-info-col div.seller-info-value div.seller-info-name a::text').extract(),
            'adress':item.css('div.item-view-contacts.js-item-view-contacts div.item-view-seller-info div.seller-info.js-seller-info div.seller-info-prop div.seller-info-value::text').extract()[4:],
            'number of rooms':item.css('div.item-view-main.js-item-view-main div.item-view-block div.item-params ul.item-params-list li.item-params-item::text').extract(),
            'floor': item.css('div.item-view-main.js-item-view-main div.item-view-block div.item-params ul.item-params-list li.item-params-list-item::text').extract()[5:6],
            'type':item.css('div.item-view-main.js-item-view-main div.item-view-block div.item-params ul.item-params-list li.item-params-list-item::text').extract()[7:8],
            'total area':item.css('div.item-view-main.js-item-view-main div.item-view-block div.item-params ul.item-params-list li.item-params-list-item::text').extract()[9:10],
            'kitchen area':item.css('div.item-view-main.js-item-view-main div.item-view-block div.item-params ul.item-params-list li.item-params-list-item::text').extract()[11:12],
            'living space':item.css('div.item-view-main.js-item-view-main div.item-view-block div.item-params ul.item-params-list li.item-params-list-item::text').extract()[13:14],
            'description':item.css('div.item-view-block div.item-description div.item-description-text p::text').extract(),
            'lat':item.css('div.b-search-map.expanded.item-map-wrapper.js-item-map-wrapper::attr(data-map-lat)').extract(),
            'lon': item.css('div.b-search-map.expanded.item-map-wrapper.js-item-map-wrapper::attr(data-map-lon)').extract(),
            'photo-list':item.css('div.gallery-list-wrapper ul.gallery-list.js-gallery-list li.gallery-list-item.js-gallery-list-item span.gallery-list-item-link::attr(style)').extract()
             }


    #итерируемся по url страниц
        for next_page in responce.css('a.pagination-page::attr(href)'):
         for next_page in responce.css('div.item_table-description div.item_table-header h3.item-description-title a.item-description-title-link::attr(href)'):
            yield responce.follow(next_page,self.parse)
