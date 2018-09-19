#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Script creates search index for Tipue Search 7.0
# Check http://www.tipue.com/search/help/ for more info

import json
import os
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
        node['url'] = soup.link['href']
        node['text'] = soup.article.get_text(' ', strip=True).replace('^', '&#94;')
        tags = []
        for a in soup.find("p", class_="post-meta").find_all("a"):
            tags.append(a['href'].split('/')[-1])
        node['tags'] = ' '.join(tags)
        return node
    except Exception as e:
        #print(e)
        return None


# Json accumulator
def jsoner(nodes):
    jdata = {'pages': nodes}
    output = json.dumps(jdata)
    output = 'var tipuesearch = ' + output + ';'
    # This is hardcoded http://www.tipue.com/search/help/?d=2
    with open('public/tipuesearch/tipuesearch_content.js', 'w') as f:
        f.write(output)


# Sitemap generation
def sitemaper(nodes):
    xml = '''<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''
    url = '<url><loc>{0}</loc><changefreq>daily</changefreq><priority>0.5</priority></url>\n'
    for n in nodes:
        xml = xml + url.format(n['url'])
    xml = xml + '\n</urlset>'
    with open('public/search/sitemap.xml', 'w') as f:
        f.write(xml)


if os.path.exists('./public/tipuesearch'):
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
