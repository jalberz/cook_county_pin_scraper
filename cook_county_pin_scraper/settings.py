# -*- coding: utf-8 -*-

# Scrapy settings for cook_county_pin_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cook_county_pins'

SPIDER_MODULES = ['cook_county_pin_scraper.spiders']
NEWSPIDER_MODULE = 'cook_county_pin_scraper.spiders'
DOWNLOAD_DELAY = 0.004
CONCURRENT_REQUESTS = 45
MEMDEBUG_ENABLED = True
COOKIES_DEBUG = False
DOWNLOAD_TIMEOUT = 1000
DUPEFILTER_CLASS = 'cook_county_pin_scraper.custom_filters.CustomFilter'
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'http://www.cookcountypropertyinfo.com'
}