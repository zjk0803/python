# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:37:41 2018

@author: 抖抖飞
"""

from bs4 import BeautifulSoup
from pprint import pprint
broken_html='<ul class=country_or_district><li>Population</ul>'
#soup=BeautifulSoup(broken_html,'html.parser')
#fixed_html=soup.prettify()
#pprint(fixed_html)

soup=BeautifulSoup(broken_html,'html5lib')
fixed_html=soup.prettify()
pprint(fixed_html)