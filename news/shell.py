from scrapy import cmdline
if __name__ == '__main__':
    # cmdline.execute('scrapy crawl sinaNews -o item.json'.split())
    # cmdline.execute('scrapy crawl sinaNews'.split())
    cmdline.execute('scrapy crawl sinaNews -o item.xml'.split())
