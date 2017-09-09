#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from bs4 import BeautifulSoup


# Takes Hugo public directory and returns all html files
def walker(path):
    pages = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                pages.append('/'.join((root, file)))
    return pages


# Takes html page and outputs json object
def parser(page):
    soup = BeautifulSoup(open(page, 'r'))
    node = {}
    try:
        node['title'] = soup.title.get_text(' ', strip=True).replace('&nbsp;', ' ').replace('^', '&#94;')
        node['loc'] = soup.link['href']
        node['text'] = soup.article.get_text(' ', strip=True).replace('^', '&#94;')
        tags = ['nonetags']
        #for a in soup.find("p", id='tags').find_all("a"):
        #    tags.append(a['href'].split('/')[-1])
        node['tags'] = ' '.join(tags)
        return node
    except:
        return None


# Json accumulator
def jsoner(nodes):
    jdata = {'pages': nodes}
    with open('public/tipuesearch_content.json', 'w') as f:
        json.dump(jdata, f)


# Sitemap generation
def sitemaper(nodes):
    xml = '''<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''
    url = '<url><loc>{0}</loc><changefreq>daily</changefreq><priority>0.5</priority></url>\n'
    for n in nodes:
        xml = xml + url.format(n['loc'])
    xml = xml + '\n</urlset>'
    with open('public/search/sitemap.xml', 'w') as f:
        f.write(xml)

if os.path.exists('./public'):
    pages = walker('.')
    nodes = []
    for p in pages:
        node = parser(p)
        if node:
            nodes.append(node)
    jsoner(nodes)
    sitemaper(nodes)
else:
    print 'Error: place this script in hugo site root'
