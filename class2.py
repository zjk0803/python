# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:05:07 2018

@author: 抖抖飞
"""

#class1 的环境下

import re
from class1.advanced_link_crawler import download
url='http://example.python-scraping.com/view/UnitedKingdom-239'
html= download(url)
re.findall(r'<td class="w2p_fw">(.*?)</td>',html)
['<img src="/places/static/img/flags/gb.png"/>',
 '244,820 square kilometres'
 ]
re.findall(r'<td class="w2p_fw">(.*?)</td>',html)[1]