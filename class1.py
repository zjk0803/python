# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:48:27 2018

@author: pyer
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

def crawl_site(url,max_errors=5):
    for page in itertools.count(1):
        pg_url='{}{}'.format(url,page)
        html=download(pg_url)
        if html is None:
            num_errors+=1
            break
        else:
            num_errors=0
crawl_site('http://example.python-scraping.com/view/-')






import golb
import os
from PIL import Image

def make_thumbnail(filename):
    base_filename,file_extension = os.path.splitext(filename)
    thumbnail_filename = f"{base_filename}_thumbnail{file_extension}"
    image = Image.open(filename)
    image.thumbnail(size=(128,128))
    image.save(thumbnail_filename,"JPEG")
    return thumbnail_filename
for image_file in glob.glob("*.jpg"):
    thumnail_file = make_image_thumbnail(image_file)
print(f"A thumbnail for {image_file} was save as {thumbnail_file}")
