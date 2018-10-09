# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:48:27 2018

@author: 抖抖飞
"""
import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError
url='www.zhihu.com'
def Downloads(url):
    print('Downloading:',url)
    try:
        html=urllib.request.urlopen(url).read()
    except(URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
    return html 
import re
def download(url,user_agent='wswp',num_retries=2,charset='utf-8'):
    print('downloading:',url)
    request = urllib.request.Request(url)
    request.add_header('User-agent',user_agent)
    try:
        resp=urllib.request.urlopen(request)
        cs=resp.headers.get_content_charset()
        if not cs:
            cs=charset
        html=resp.read().decode(cs)
    except(URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return download(url,num_retries - 1)
    return html
def crawl_sitemap(url):
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html=download(link)
crawl_sitemap('http://example.python-scraping.com/sitemap.xml')

import re
def download(url,user_agent='wswp',num_retries=2,charset='utf-8'):
    print('downloading:',url)
    request = urllib.request.Request(url)
    request.add_header('User-agent',user_agent)
    try:
        resp=urllib.request.urlopen(request)
        cs=resp.headers.get_content_charset()
        if not cs:
            cs=charset
        html=resp.read().decode(cs)
    except(URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return download(url,num_retries - 1)
    return html
def crawl_sitemap(url):
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html=download(link)
crawl_sitemap('http://example.python-scraping.com/sitemap.xml')

import itertools
def crawl_site(url):
    for page in itertools.count(1):
        pg_url='{}{}'.format(url,page)
        html=download(pg_url)
        if html is None:
            break
crawl_site('http://example.python-scraping.com/view/-')


