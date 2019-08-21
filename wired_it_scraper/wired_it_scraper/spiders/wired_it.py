# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider


class WiredItSpider(SitemapSpider):
    name = 'wired_it'

    sitemap_urls = ['https://www.wired.it/sitemap_index.xml']
    sitemap_follow = ['/post']

    def parse(self, response):
    	#print "==============> URL: " + response.request.url

    	breadcrumbs = response.xpath("//nav[@class = 'breadcrumbs']//span/a")
    	title = response.xpath("//header[@class = 'article-header']/h1/text()").get()
    	if (len(breadcrumbs) > 0 and title is not None):
    		paragraphsElements = response.xpath("//header[@class = 'article-header']/parent::div//div[contains(@class, 'col-content')]/p//text()")
    		paragraphs = [paragraphElement.get().strip() for paragraphElement in paragraphsElements]
    		text = " ".join([paragraph for paragraph in paragraphs if not paragraph.startswith('adsJSCode') and not "function($)" in paragraph and not "window." in paragraph]).strip()

    		category = "_".join([breadcrumb.xpath('./text()').get().strip().lower() for breadcrumb in breadcrumbs])
    		titleNormalized = title.strip().lower()
    		copyright = " ".join([license.get().strip() for license in response.xpath("//a[@rel = 'license']//text()")]).strip()

    		yield {
    			"category": category,
    			"title": titleNormalized,
    			"url": response.request.url,
    			"copyright": copyright,
    			"text": text
    		}